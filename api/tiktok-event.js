/**
 * TikTok Events API (servidor) — função serverless da Vercel.
 *
 * O navegador envia o evento para cá com o mesmo event_id usado no pixel;
 * esta função repassa ao TikTok com o token, que fica só na Vercel
 * (Settings → Environment Variables → TIKTOK_ACCESS_TOKEN).
 * O TikTok descarta a cópia duplicada (mesmo pixel + evento + event_id).
 *
 * Opcional: TIKTOK_TEST_EVENT_CODE envia os eventos como "teste"
 * (aba Test Events do Events Manager), sem contar nas campanhas.
 */

const PIXEL_ID = "DAVSCSBC77U3L5980EV0";
const ENDPOINT = "https://business-api.tiktok.com/open_api/v1.3/event/track/";
const ALLOWED_EVENTS = new Set(["Contact", "ViewContent"]);
const ALLOWED_HOSTS = new Set(["www.guilhermeborborema.com.br", "guilhermeborborema.com.br"]);

const parseCookies = (header = "") =>
  Object.fromEntries(
    header
      .split(";")
      .map((part) => part.trim().split("="))
      .filter(([key, value]) => key && value)
      .map(([key, ...rest]) => [key, decodeURIComponent(rest.join("="))])
  );

const cleanText = (value, max = 120) =>
  typeof value === "string" && value.trim() ? value.trim().slice(0, max) : undefined;

const isAllowedUrl = (value) => {
  try {
    return ALLOWED_HOSTS.has(new URL(value).hostname);
  } catch {
    return false;
  }
};

module.exports = async (req, res) => {
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST");
    return res.status(405).json({ ok: false, error: "method_not_allowed" });
  }

  const token = process.env.TIKTOK_ACCESS_TOKEN;
  if (!token) {
    console.error("TikTok Events API: variável TIKTOK_ACCESS_TOKEN não configurada");
    return res.status(500).json({ ok: false, error: "missing_token" });
  }

  // sendBeacon pode chegar como texto; fetch chega como JSON já interpretado
  let body = req.body;
  if (typeof body === "string") {
    try {
      body = JSON.parse(body);
    } catch {
      body = null;
    }
  }

  const event = body && body.event;
  const eventId = body && cleanText(body.event_id, 100);
  if (!ALLOWED_EVENTS.has(event) || !eventId) {
    return res.status(400).json({ ok: false, error: "invalid_event" });
  }

  // Só aceita eventos vindos das páginas do próprio site
  const origin = req.headers.origin;
  if (!isAllowedUrl(body.url) || (origin && !isAllowedUrl(origin))) {
    return res.status(403).json({ ok: false, error: "forbidden_origin" });
  }

  const cookies = parseCookies(req.headers.cookie);
  const pageUrl = new URL(body.url);
  const forwardedFor = req.headers["x-forwarded-for"] || "";

  const user = {
    ip: forwardedFor.split(",")[0].trim() || undefined,
    user_agent: cleanText(req.headers["user-agent"], 512),
    ttp: cleanText(cookies._ttp, 100),
    ttclid: cleanText(pageUrl.searchParams.get("ttclid") || cookies.ttclid, 200),
  };

  const properties = {
    content_id: cleanText(body.properties && body.properties.content_id),
    content_name: cleanText(body.properties && body.properties.content_name),
  };

  const payload = {
    event_source: "web",
    event_source_id: PIXEL_ID,
    data: [
      {
        event,
        event_time: Math.floor(Date.now() / 1000),
        event_id: eventId,
        user,
        page: { url: body.url, referrer: cleanText(body.referrer, 2048) },
        properties,
      },
    ],
  };
  if (process.env.TIKTOK_TEST_EVENT_CODE) payload.test_event_code = process.env.TIKTOK_TEST_EVENT_CODE;

  try {
    const response = await fetch(ENDPOINT, {
      method: "POST",
      headers: { "Access-Token": token, "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const result = await response.json().catch(() => ({}));
    const ok = response.ok && result.code === 0;

    if (!ok) console.error("TikTok Events API recusou o evento:", response.status, result.code, result.message);
    return res.status(ok ? 200 : 502).json({ ok, code: result.code, message: ok ? undefined : result.message });
  } catch (error) {
    console.error("TikTok Events API indisponível:", error.message);
    return res.status(502).json({ ok: false, error: "upstream_unavailable" });
  }
};
