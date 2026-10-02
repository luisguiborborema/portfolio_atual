/* ==========================================================================
   Guilherme Borborema — Portfólio
   Interações: navegação, scroll reveal, contadores, filtros e micro-interações
   ========================================================================== */

(() => {
  "use strict";

  const root = document.documentElement;
  const isEnglish = root.lang.toLowerCase().startsWith("en");
  const t = isEnglish
    ? { openMenu: "Open menu", closeMenu: "Close menu", locale: "en-US" }
    : { openMenu: "Abrir menu", closeMenu: "Fechar menu", locale: "pt-BR" };
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const hasFinePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

  root.classList.add("js");

  /* ---------- Ano no rodapé ---------- */
  document.querySelectorAll("[data-year]").forEach((el) => {
    el.textContent = new Date().getFullYear();
  });

  /* ---------- Fotos: mostra o placeholder enquanto a imagem não existir ---------- */
  document.querySelectorAll("[data-photo]").forEach((img) => {
    const markMissing = () => img.closest(".photo").classList.add("is-missing");
    if (img.complete && img.naturalWidth === 0) markMissing();
    else img.addEventListener("error", markMissing, { once: true });
  });

  /* ---------- Navegação: estado ao rolar ---------- */
  const nav = document.querySelector("[data-nav]");

  const updateNav = () => nav.classList.toggle("is-scrolled", window.scrollY > 16);
  updateNav();
  window.addEventListener("scroll", updateNav, { passive: true });

  /* ---------- Navegação: menu mobile ---------- */
  const toggle = document.querySelector("[data-nav-toggle]");
  const menu = document.getElementById("nav-menu");

  const setMenu = (open) => {
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? t.closeMenu : t.openMenu);
    menu.classList.toggle("is-open", open);
    document.body.style.overflow = open ? "hidden" : "";
  };

  toggle.addEventListener("click", () => {
    setMenu(toggle.getAttribute("aria-expanded") !== "true");
  });

  menu.addEventListener("click", (event) => {
    if (event.target.closest("a")) setMenu(false);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && menu.classList.contains("is-open")) {
      setMenu(false);
      toggle.focus();
    }
  });

  window.matchMedia("(min-width: 861px)").addEventListener("change", (event) => {
    if (event.matches) setMenu(false);
  });

  /* ---------- Navegação: link ativo por seção ---------- */
  // Só links para seções desta página (as páginas de case também apontam para a inicial)
  const navLinks = [...document.querySelectorAll("[data-nav-link]")].filter((link) =>
    link.getAttribute("href").startsWith("#")
  );
  const sections = navLinks
    .map((link) => document.querySelector(link.getAttribute("href")))
    .filter(Boolean);

  const sectionObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const id = `#${entry.target.id}`;
        navLinks.forEach((link) => {
          const active = link.getAttribute("href") === id;
          link.classList.toggle("is-active", active);
          if (active) link.setAttribute("aria-current", "true");
          else link.removeAttribute("aria-current");
        });
      });
    },
    { rootMargin: "-45% 0px -50% 0px" }
  );

  sections.forEach((section) => sectionObserver.observe(section));

  /* ---------- Botão flutuante: some quando o contato já está visível ---------- */
  const waFloat = document.querySelector(".wa-float");
  const contact = document.querySelector("[data-contact]");

  if (waFloat && contact) {
    new IntersectionObserver(([entry]) => {
      waFloat.classList.toggle("is-hidden", entry.isIntersecting);
    }, { threshold: 0.15 }).observe(contact);
  }

  /* ---------- Scroll reveal (com escalonamento entre irmãos) ---------- */
  const revealEls = document.querySelectorAll(".reveal");

  revealEls.forEach((el) => {
    const siblings = [...el.parentElement.children].filter((child) => child.classList.contains("reveal"));
    const index = siblings.indexOf(el);
    el.style.setProperty("--reveal-delay", `${Math.min(index, 6) * 90}ms`);
  });

  if (prefersReducedMotion || !("IntersectionObserver" in window)) {
    revealEls.forEach((el) => el.classList.add("is-visible"));
  } else {
    const revealObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );

    revealEls.forEach((el) => revealObserver.observe(el));
  }

  /* ---------- Contadores animados ---------- */
  const formatNumber = (value, format) =>
    format === "thousands" ? value.toLocaleString(t.locale) : String(value);

  const animateCount = (el) => {
    const target = Number(el.dataset.count);
    const format = el.dataset.format;

    if (prefersReducedMotion) {
      el.textContent = formatNumber(target, format);
      return;
    }

    const duration = 1600;
    const start = performance.now();
    const easeOut = (t) => 1 - Math.pow(1 - t, 4);

    const tick = (now) => {
      const progress = Math.min((now - start) / duration, 1);
      el.textContent = formatNumber(Math.round(target * easeOut(progress)), format);
      if (progress < 1) requestAnimationFrame(tick);
    };

    requestAnimationFrame(tick);
  };

  const counterObserver = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        animateCount(entry.target);
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.6 }
  );

  document.querySelectorAll("[data-count]").forEach((el) => {
    el.textContent = "0";
    counterObserver.observe(el);
  });

  /* ---------- Filtro de projetos ---------- */
  const filterButtons = document.querySelectorAll("[data-filter]");
  const projects = document.querySelectorAll("[data-projects] .project");

  filterButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const filter = button.dataset.filter;

      filterButtons.forEach((btn) => {
        const active = btn === button;
        btn.classList.toggle("is-active", active);
        btn.setAttribute("aria-pressed", String(active));
      });

      projects.forEach((project, i) => {
        const match = filter === "all" || project.dataset.category === filter;
        project.classList.toggle("is-hidden", !match);
        project.classList.remove("is-filtering");

        if (match) project.classList.add("is-visible");

        if (match && !prefersReducedMotion) {
          // força reflow para reiniciar a animação de entrada
          void project.offsetWidth;
          project.style.animationDelay = `${i * 40}ms`;
          project.classList.add("is-filtering");
        }
      });
    });
  });

  /* ---------- TikTok Pixel: cliques de contato viram evento "Contact" ---------- */
  document.addEventListener("click", (event) => {
    const link = event.target.closest('a[href^="https://wa.me"], a[href^="mailto:"]');
    if (!link || typeof window.ttq?.track !== "function") return;
    window.ttq.track("Contact", {
      content_name: link.href.startsWith("mailto:") ? "email" : "whatsapp",
    });
  });

  /* ---------- Efeitos de ponteiro (apenas desktop) ---------- */
  if (!hasFinePointer || prefersReducedMotion) return;

  // Brilho que segue o mouse nos cards
  document.querySelectorAll(".spotlight").forEach((card) => {
    card.addEventListener("pointermove", (event) => {
      const rect = card.getBoundingClientRect();
      card.style.setProperty("--mx", `${event.clientX - rect.left}px`);
      card.style.setProperty("--my", `${event.clientY - rect.top}px`);
    });
  });

  // Inclinação 3D do cartão de código
  document.querySelectorAll("[data-tilt]").forEach((card) => {
    const maxTilt = 8;

    card.addEventListener("pointermove", (event) => {
      const rect = card.getBoundingClientRect();
      const x = (event.clientX - rect.left) / rect.width - 0.5;
      const y = (event.clientY - rect.top) / rect.height - 0.5;
      card.style.transition = "transform 0.12s linear";
      card.style.transform = `rotateY(${x * maxTilt}deg) rotateX(${-y * maxTilt}deg) translateZ(0)`;
    });

    card.addEventListener("pointerleave", () => {
      card.style.transition = "";
      card.style.transform = "";
    });
  });

  // Botões magnéticos
  document.querySelectorAll(".magnetic").forEach((btn) => {
    const strength = 0.25;

    btn.addEventListener("pointermove", (event) => {
      const rect = btn.getBoundingClientRect();
      const x = event.clientX - (rect.left + rect.width / 2);
      const y = event.clientY - (rect.top + rect.height / 2);
      btn.style.transform = `translate(${x * strength}px, ${y * strength}px)`;
    });

    btn.addEventListener("pointerleave", () => {
      btn.style.transform = "";
    });
  });
})();
