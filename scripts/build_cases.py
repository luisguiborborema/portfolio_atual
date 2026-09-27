#!/usr/bin/env python3
"""Gera as páginas de case do portfólio (PT e EN).

Uso:  python3 scripts/build_cases.py

Para editar um case, altere o conteúdo em CASES abaixo e rode o script de novo.
Saída: cases/<slug>.html (português) e en/cases/<slug>.html (inglês).
"""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EMAIL = "gui.borborema.it@gmail.com"
WHATSAPP = {
    "pt": "https://wa.me/5527988171917?text=Ol%C3%A1%2C%20Guilherme!%20Vi%20seu%20portf%C3%B3lio%20e%20quero%20conversar%20sobre%20um%20projeto.",
    "en": "https://wa.me/5527988171917?text=Hi%20Guilherme!%20I%20saw%20your%20portfolio%20and%20would%20like%20to%20talk%20about%20a%20project.",
}
LINKEDIN = "https://www.linkedin.com/in/guilherme-borborema/"
INSTAGRAM = "https://www.instagram.com/guilherme_borborema/"

# --------------------------------------------------------------------------
# Conteúdo dos cases (na mesma ordem da grade da página inicial)
# --------------------------------------------------------------------------
CASES = [
    {
        "slug": "agente-ia-sdr",
        "name": "Agente de IA SDR",
        "name_en": "AI SDR Agent",
        "hue": 88,
        "mono": "SDR",
        "url": None,
        "domain": None,
        "screens": False,
        "pt": {
            "tag": "Inteligência Artificial",
            "segment": "Vendas e atendimento",
            "deliverable": "Agente de IA",
            "title": "Agente de IA SDR: mais de 3.000 conversas e R$ 30 mil em vendas",
            "lead": "Um agente de inteligência artificial que desenvolvi para atuar como pré-vendedor: conversa com os contatos, qualifica, recupera clientes descartados e agenda reuniões sozinho.",
            "sections": [
                ("O objetivo", "Automatizar a linha de frente comercial com um agente de IA atuando como SDR (pré-vendedor): conversar com os contatos, qualificar o interesse, retomar clientes que haviam sido descartados e entregar reuniões agendadas para o time de vendas — sem depender de alguém disponível a todo momento."),
            ],
            "list_title": "O que o agente faz",
            "list": [
                "Conversa com os leads de forma natural, respondendo dúvidas sobre o produto ou serviço.",
                "Qualifica cada contato antes de ocupar o tempo do time comercial.",
                "Recupera clientes descartados, retomando conversas com contatos que tinham sido deixados de lado.",
                "Agenda reuniões automaticamente com quem demonstra interesse real.",
            ],
            "results_title": "Resultados",
            "results": [("+3.000", "conversas realizadas"), ("+150", "reuniões agendadas automaticamente"), ("R$ 30 mil", "em vendas diretas geradas")],
            "results_text": "Além dos números, o agente passou a recuperar clientes que haviam sido descartados, transformando contatos antes perdidos em novas oportunidades de venda.",
        },
        "en": {
            "tag": "Artificial Intelligence",
            "segment": "Sales & customer service",
            "deliverable": "AI agent",
            "title": "AI SDR Agent: over 3,000 conversations and R$ 30k in sales",
            "lead": "An artificial intelligence agent I built to work as a sales development rep: it talks to leads, qualifies them, wins back lost customers and books meetings on its own.",
            "sections": [
                ("The goal", "Automate the front line of sales with an AI agent working as an SDR: talk to leads, qualify their interest, re-engage customers who had been dropped and hand booked meetings to the sales team — without depending on someone being available at all times."),
            ],
            "list_title": "What the agent does",
            "list": [
                "Talks to leads naturally, answering questions about the product or service.",
                "Qualifies every contact before taking up the sales team's time.",
                "Wins back lost customers by restarting conversations with contacts that had been left aside.",
                "Automatically books meetings with people who show real interest.",
            ],
            "results_title": "Results",
            "results": [("+3,000", "conversations held"), ("+150", "meetings booked automatically"), ("R$ 30k", "in direct sales generated")],
            "results_text": "Beyond the numbers, the agent started winning back customers who had been dropped, turning previously lost contacts into new sales opportunities.",
        },
    },
    {
        "slug": "bnex",
        "name": "BNEX",
        "hue": 200,
        "logo": "bnex.svg",
        "url": "https://bnex-site.web.app/",
        "domain": "bnex-site.web.app",
        "screens": True,
        "pt": {
            "tag": "Site institucional",
            "segment": "Sportstech",
            "deliverable": "Site institucional",
            "title": "BNEX: site institucional para sportstech de alta performance",
            "lead": "Site institucional que desenvolvi para a BNEX, plataforma que une ciência do esporte e machine learning para clubes, clínicas, academias e atletas de alto rendimento.",
            "sections": [
                ("O objetivo", "Explicar um produto técnico — a análise de biomarcadores com inteligência artificial para prevenir lesões e orientar treinos — de forma clara para clubes, clínicas, academias e atletas, e transmitir a credibilidade científica que esse público exige."),
            ],
            "list_title": "O que o site entrega",
            "list": [
                "Proposta de valor por público, com as dores da operação (custo de atletas lesionados, decisão sem evidência) e os ganhos.",
                "Seções de soluções, ciência e parceiros, apresentando a metodologia e a base científica.",
                "Vídeos mostrando a plataforma em funcionamento.",
                "Perguntas frequentes que explicam conceitos técnicos (carga interna e externa, coleta point-of-care, WBS) em linguagem acessível.",
                "Páginas legais (privacidade, termos de uso, LGPD e ANVISA) e contato pelo WhatsApp.",
            ],
        },
        "en": {
            "tag": "Corporate website",
            "segment": "Sportstech",
            "deliverable": "Corporate website",
            "title": "BNEX: corporate website for a high-performance sportstech",
            "lead": "Corporate website I built for BNEX, a platform that combines sports science and machine learning for clubs, clinics, gyms and high-performance athletes.",
            "sections": [
                ("The goal", "Explain a technical product — AI-powered biomarker analysis to prevent injuries and guide training — clearly to clubs, clinics, gyms and athletes, while conveying the scientific credibility this audience expects."),
            ],
            "list_title": "What the website delivers",
            "list": [
                "Value proposition by audience, covering operational pain points (the cost of injured athletes, decisions without evidence) and the gains.",
                "Solutions, science and partners sections presenting the methodology and its scientific foundation.",
                "Videos showing the platform in action.",
                "An FAQ that explains technical concepts (internal and external load, point-of-care testing, WBS) in plain language.",
                "Legal pages (privacy, terms of use, LGPD and ANVISA) and contact via WhatsApp.",
            ],
        },
    },
    {
        "slug": "dizcoteka",
        "name": "Dizcoteka",
        "hue": 320,
        "logo": "dizcoteka.png",
        "url": "https://dizcoteka.com/",
        "domain": "dizcoteka.com",
        "screens": True,
        "pt": {
            "tag": "E-commerce",
            "segment": "Moda",
            "deliverable": "Loja online",
            "title": "Dizcoteka: e-commerce de moda para festa",
            "lead": "Loja online que desenvolvi para a Dizcoteka, marca de moda para festa — tops, saias, calças e vestidos, com entrega para todo o Brasil.",
            "sections": [
                ("O objetivo", "Levar a identidade da marca para uma loja online com foco em conversão: fazer a cliente encontrar rápido a peça certa para a ocasião e concluir a compra sem atrito."),
            ],
            "list_title": "O que a loja entrega",
            "list": [
                "Navegação por tipo de peça (tops, bottoms, vestidos) e por faixa de preço, para quem já sabe quanto quer gastar.",
                "Coleções por ocasião, como looks para sair com as amigas, o básico da festa e o dia seguinte.",
                "Vitrines de novidades e de última chance, que estimulam a compra.",
                "Tabela de medidas do PP ao G, carrinho, conta da cliente e atendimento pelo WhatsApp.",
                "Entrega para todo o Brasil e banner de condições especiais no topo.",
            ],
        },
        "en": {
            "tag": "E-commerce",
            "segment": "Fashion",
            "deliverable": "Online store",
            "title": "Dizcoteka: partywear fashion e-commerce",
            "lead": "Online store I built for Dizcoteka, a partywear fashion brand — tops, skirts, pants and dresses, shipping nationwide across Brazil.",
            "sections": [
                ("The goal", "Bring the brand's identity to a conversion-focused online store: help customers quickly find the right piece for the occasion and complete the purchase without friction."),
            ],
            "list_title": "What the store delivers",
            "list": [
                "Browsing by garment type (tops, bottoms, dresses) and by price range, for shoppers who already know their budget.",
                "Collections by occasion, such as going-out looks, party basics and the day after.",
                "New-in and last-chance showcases that encourage purchases.",
                "Size chart from XS to L, cart, customer account and support via WhatsApp.",
                "Nationwide shipping and a special-offers banner at the top.",
            ],
        },
    },
    {
        "slug": "memo",
        "name": "MEMO",
        "hue": 262,
        "logo": "memo.svg",
        "url": "https://painel-memo.vercel.app/",
        "domain": "painel-memo.vercel.app",
        "screens": False,
        "pt": {
            "tag": "Sistema · CRM",
            "segment": "Produtora de vídeos de casamento",
            "deliverable": "Sistema sob medida",
            "title": "MEMO: CRM e gestão para produtora de vídeos de casamento",
            "lead": "Um sistema sob medida que desenvolvi para a MEMO, produtora de vídeos de casamento: CRM comercial e de operação, contratos gerados e enviados automaticamente e DRE calculada sem planilha.",
            "sections": [
                ("O desafio", "Uma produtora de vídeos de casamento acompanha muitos casais ao mesmo tempo, e cada um passa por várias etapas: a negociação comercial, o contrato, a operação do grande dia e das entregas, e o controle financeiro. Quando tudo isso depende de trabalho manual, crescer significa mais horas de escritório em vez de mais casamentos atendidos."),
            ],
            "list_title": "A solução",
            "list_intro": "Desenvolvi para a MEMO um sistema de gestão sob medida que reúne a parte comercial, a operação e o financeiro num lugar só:",
            "list": [
                "<strong>CRM comercial:</strong> acompanhamento das negociações com os casais, do primeiro contato ao fechamento.",
                "<strong>CRM de operação:</strong> acompanhamento de cada casamento depois de fechado, para a equipe saber o que precisa ser feito em cada projeto.",
                "<strong>Contratos automáticos:</strong> o sistema gera o contrato e faz o envio, sem montar documento por documento.",
                "<strong>DRE automática:</strong> o cálculo do resultado financeiro (Demonstração do Resultado) sai pronto, sem planilha paralela.",
                "<strong>Acesso seguro:</strong> sistema online, com login restrito à equipe da MEMO.",
            ],
            "cta_label": "Acessar o sistema",
            "results_title": "Resultados",
            "results": [("+30", "casamentos gerenciados pelo sistema"), ("Mais escala", "para atender mais casais com a mesma estrutura"), ("Menos tempo", "gasto em contratos, controles e planilhas")],
            "results_text": "Com contratos e DRE automatizados e cada casamento acompanhado do comercial à operação, a produtora ganhou escala e economia de tempo, e passou a gerenciar mais de 30 casamentos pelo sistema.",
        },
        "en": {
            "tag": "System · CRM",
            "segment": "Wedding video production",
            "deliverable": "Custom system",
            "title": "MEMO: CRM and management for a wedding video production company",
            "lead": "A custom system I built for MEMO, a wedding video production company: sales and operations CRM, contracts generated and sent automatically, and a P&L statement calculated without spreadsheets.",
            "sections": [
                ("The challenge", "A wedding video production company follows many couples at once, and each one goes through several stages: the sales negotiation, the contract, the operation of the big day and the deliveries, and financial control. When all of that depends on manual work, growing means more office hours instead of more weddings."),
            ],
            "list_title": "The solution",
            "list_intro": "I built MEMO a custom management system that brings sales, operations and finance together in one place:",
            "list": [
                "<strong>Sales CRM:</strong> tracking negotiations with couples, from first contact to closing.",
                "<strong>Operations CRM:</strong> tracking each wedding after closing, so the team knows what needs to be done on every project.",
                "<strong>Automatic contracts:</strong> the system generates and sends the contract, with no document-by-document assembly.",
                "<strong>Automatic P&amp;L:</strong> the income statement is calculated automatically, with no side spreadsheet.",
                "<strong>Secure access:</strong> an online system with login restricted to the MEMO team.",
            ],
            "cta_label": "Open the system",
            "results_title": "Results",
            "results": [("+30", "weddings managed in the system"), ("More scale", "to serve more couples with the same team"), ("Less time", "spent on contracts, controls and spreadsheets")],
            "results_text": "With automated contracts and P&amp;L, and every wedding tracked from sales to operations, the company gained scale and saved time — and now manages more than 30 weddings in the system.",
        },
    },
    {
        "slug": "refugios-pedra-azul",
        "name": "Refúgios Pedra Azul",
        "hue": 172,
        "logo": "refugios-pedra-azul.png",
        "logo_plate": True,
        "url": "https://refugiospedraazul.com.br/",
        "domain": "refugiospedraazul.com.br",
        "screens": True,
        "pt": {
            "tag": "Landing page",
            "segment": "Mercado imobiliário",
            "deliverable": "Landing page",
            "title": "Refúgios Pedra Azul: landing page de curadoria imobiliária",
            "lead": "Landing page que desenvolvi para o Refúgios Pedra Azul, selo de curadoria que apresenta terrenos validados em Pedra Azul, Domingos Martins (ES).",
            "sections": [
                ("O objetivo", "Apresentar terrenos urbanos independentes, com matrícula individual e perto da Rota do Lagarto, transmitindo credibilidade — o selo funciona como chancela de curadoria — e levando os interessados a falar com um consultor."),
            ],
            "list_title": "O que a página entrega",
            "list": [
                "Primeira tela com vídeo da região e chamada direta para conhecer as propriedades.",
                "Galeria de fotos e vídeos que abre em tela cheia ao clicar, para o visitante sentir o lugar.",
                "Chancela de qualidade: seção que explica o selo e os critérios de curadoria dos terrenos.",
                "Mapa de localização integrado.",
                "Contato com consultor pelo WhatsApp e links para Instagram e Facebook.",
            ],
        },
        "en": {
            "tag": "Landing page",
            "segment": "Real estate",
            "deliverable": "Landing page",
            "title": "Refúgios Pedra Azul: real estate curation landing page",
            "lead": "Landing page I built for Refúgios Pedra Azul, a curation seal that presents vetted land plots in Pedra Azul, Domingos Martins (Espírito Santo, Brazil).",
            "sections": [
                ("The goal", "Present independent urban plots with individual deeds near the Rota do Lagarto, conveying credibility — the seal works as a curation endorsement — and leading prospects to talk to a consultant."),
            ],
            "list_title": "What the page delivers",
            "list": [
                "Hero section with a video of the region and a direct call to explore the properties.",
                "Photo and video gallery that opens full screen on click, so visitors can feel the place.",
                "Quality endorsement: a section explaining the seal and the curation criteria for the plots.",
                "Integrated location map.",
                "Contact with a consultant via WhatsApp and links to Instagram and Facebook.",
            ],
        },
    },
    {
        "slug": "vallorem",
        "name": "Vallorem",
        "hue": 40,
        "logo": "vallorem.png",
        "url": None,
        "domain": "vallorem.com.br",
        "screens": True,
        "pt": {
            "tag": "Landing page",
            "segment": "Contabilidade",
            "deliverable": "Landing page",
            "title": "Vallorem: landing page para escritório de contabilidade",
            "lead": "Landing page que desenvolvi para a Vallorem, escritório de contabilidade estratégica e consultiva em Vitória (ES), em operação desde 2009.",
            "sections": [
                ("O objetivo", "Mostrar que a Vallorem une processos digitais com a proximidade de um consultor dedicado, reforçar a tradição de mais de 15 anos de mercado e transformar visitantes em reuniões agendadas."),
            ],
            "list_title": "O que a página entrega",
            "list": [
                "Primeira tela com proposta clara e chamada para um diagnóstico estratégico.",
                "Vídeo institucional apresentando a forma de atendimento.",
                "História e credibilidade: fundação em 2009 e mais de 15 anos de operação contínua.",
                "Áreas de atuação: contábil e fiscal, pessoal e recursos humanos, atos e registro.",
                "Mapa do escritório em Vitória e formulário para agendar reunião.",
            ],
        },
        "en": {
            "tag": "Landing page",
            "segment": "Accounting",
            "deliverable": "Landing page",
            "title": "Vallorem: landing page for an accounting firm",
            "lead": "Landing page I built for Vallorem, a strategic and advisory accounting firm in Vitória (Espírito Santo, Brazil), operating since 2009.",
            "sections": [
                ("The goal", "Show that Vallorem combines digital processes with the closeness of a dedicated advisor, reinforce its 15+ years in the market and turn visitors into booked meetings."),
            ],
            "list_title": "What the page delivers",
            "list": [
                "Hero section with a clear proposition and a call to book a strategic assessment.",
                "Institutional video presenting how the firm works with clients.",
                "History and credibility: founded in 2009, with over 15 years of continuous operation.",
                "Practice areas: accounting and tax, payroll and HR, corporate filings and registration.",
                "Map of the office in Vitória and a form to book a meeting.",
            ],
        },
    },
    {
        "slug": "transcapixaba",
        "name": "Transcapixaba",
        "hue": 12,
        "logo": "transcapixaba.png",
        "logo_tall": True,
        "url": "https://transcapixabahikeandfly.com.br/",
        "domain": "transcapixabahikeandfly.com.br",
        "screens": True,
        "pt": {
            "tag": "Site institucional",
            "segment": "Esporte e eventos",
            "deliverable": "Site bilíngue",
            "title": "Transcapixaba: site da maior competição de Hike & Fly das Américas",
            "lead": "Site institucional que desenvolvi para a Transcapixaba Hike & Fly, a travessia do Espírito Santo caminhando e voando de parapente — cerca de 600 km, com atletas de vários países.",
            "sections": [
                ("O objetivo", "Apresentar uma competição única — uma corrida por terra e ar, inspirada no Red Bull X-Alps — para atletas, equipes e público do Brasil e do exterior, reunindo em um só lugar tudo o que acontece antes, durante e depois da prova."),
            ],
            "list_title": "O que o site entrega",
            "list": [
                "Site bilíngue, em português e inglês, para atender atletas de vários países.",
                "Contagem regressiva para a largada e chamada direta para as inscrições.",
                "Rota interativa em mapa, com os turnpoints (cilindros e placas) da edição.",
                "Resultados e classificação de cada edição, com o pódio em destaque.",
                "Galeria de fotos por ano, regulamento, perguntas frequentes e acompanhamento ao vivo.",
            ],
            "results_title": "A prova em números",
            "results": [("600 km", "de travessia"), ("7", "países representados"), ("12", "dias de prova")],
        },
        "en": {
            "tag": "Corporate website",
            "segment": "Sports & events",
            "deliverable": "Bilingual website",
            "title": "Transcapixaba: website for the largest Hike & Fly race in the Americas",
            "lead": "Website I built for Transcapixaba Hike & Fly, a crossing of the state of Espírito Santo on foot and by paraglider — around 600 km, with athletes from several countries.",
            "sections": [
                ("The goal", "Present a one-of-a-kind race — run on land and in the air, inspired by the Red Bull X-Alps — to athletes, support teams and fans in Brazil and abroad, bringing together everything that happens before, during and after the race."),
            ],
            "list_title": "What the website delivers",
            "list": [
                "Bilingual website, in Portuguese and English, for athletes from many countries.",
                "Countdown to the start and a direct call to registration.",
                "Interactive route map with the edition's turnpoints (cylinders and signs).",
                "Results and rankings for every edition, with the podium highlighted.",
                "Photo gallery by year, rules, FAQ and live tracking.",
            ],
            "results_title": "The race in numbers",
            "results": [("600 km", "crossing"), ("7", "countries represented"), ("12", "days of racing")],
        },
    },
    {
        "slug": "viofilme-sistema",
        "name": "Viofilme — Sistema",
        "name_en": "Viofilme — System",
        "hue": 225,
        "logo": "viofilme.svg",
        "url": "https://www.viofilme.com.br/",
        "domain": "viofilme.com.br",
        "screens": True,
        "pt": {
            "tag": "Sistema · CRM",
            "segment": "Marketing e audiovisual",
            "deliverable": "Sistema e painel do cliente",
            "title": "Viofilme: sistema de gestão e painel do cliente para agência de marketing",
            "lead": "Sistema que desenvolvi para a Viofilme, agência de marketing e audiovisual: centraliza a operação da agência e dá a cada cliente um painel para acompanhar campanhas, conteúdo e resultados.",
            "sections": [
                ("O objetivo", "Tirar a operação da agência de ferramentas espalhadas e dar aos clientes visibilidade sobre o trabalho entregue — campanhas, conteúdo e resultados de Instagram e Facebook — com a mesma clareza que a Viofilme entrega no dia a dia."),
            ],
            "list_title": "O que o sistema entrega",
            "list": [
                "Gestão de CRM para acompanhar o relacionamento comercial com cada cliente.",
                "Painel do cliente com campanhas, conteúdo e resultados de Instagram e Facebook em um só lugar.",
                "Acesso com login individual para cada cliente.",
                "Instalação na tela inicial do celular ou computador, para abrir como um aplicativo.",
            ],
            "cta_label": "Acessar o sistema",
        },
        "en": {
            "tag": "System · CRM",
            "segment": "Marketing & audiovisual",
            "deliverable": "System and client portal",
            "title": "Viofilme: management system and client portal for a marketing agency",
            "lead": "System I built for Viofilme, a marketing and audiovisual agency: it centralizes the agency's operations and gives each client a portal to follow campaigns, content and results.",
            "sections": [
                ("The goal", "Move the agency's operations off scattered tools and give clients visibility into the work delivered — Instagram and Facebook campaigns, content and results — with the same clarity Viofilme delivers day to day."),
            ],
            "list_title": "What the system delivers",
            "list": [
                "CRM management to track the sales relationship with each client.",
                "Client portal with Instagram and Facebook campaigns, content and results in one place.",
                "Individual login for each client.",
                "Installable on the phone or computer home screen, opening like an app.",
            ],
            "cta_label": "Open the system",
        },
    },
    {
        "slug": "agencia-viofilme",
        "name": "Agência Viofilme",
        "hue": 285,
        "logo": "viofilme.svg",
        "url": "https://www.agenciaviofilme.com.br/",
        "domain": "agenciaviofilme.com.br",
        "screens": True,
        "pt": {
            "tag": "Site institucional",
            "segment": "Marketing e audiovisual",
            "deliverable": "Site institucional",
            "title": "Agência Viofilme: site institucional para agência de performance e branding",
            "lead": "Site institucional que desenvolvi para a Viofilme, agência boutique de marketing e audiovisual que une performance, branding e comunicação com processo estruturado.",
            "sections": [
                ("O objetivo", "Posicionar a Viofilme como parceira de empresas que querem crescer com método, explicando de forma clara como as frentes da agência — performance, comunicação e desenvolvimento — se conectam, e levando o visitante a agendar uma conversa."),
            ],
            "list_title": "O que o site entrega",
            "list": [
                "Primeira tela de impacto com o posicionamento “Make it happen.” e chamada para agendar uma conversa.",
                "Seção de ecossistema mostrando como performance, branding e desenvolvimento se conectam.",
                "Serviços recorrentes e pontuais, resultados e método de trabalho apresentados em sequência.",
                "Animações de rolagem suaves e contadores que dão ritmo à navegação.",
                "Chamadas para agendar conversa ao longo de toda a página.",
            ],
        },
        "en": {
            "tag": "Corporate website",
            "segment": "Marketing & audiovisual",
            "deliverable": "Corporate website",
            "title": "Agência Viofilme: corporate website for a performance and branding agency",
            "lead": "Corporate website I built for Viofilme, a boutique marketing and audiovisual agency that combines performance, branding and communication with a structured process.",
            "sections": [
                ("The goal", "Position Viofilme as a partner for companies that want to grow methodically, clearly explaining how the agency's areas — performance, communication and development — connect, and leading visitors to book a call."),
            ],
            "list_title": "What the website delivers",
            "list": [
                "High-impact hero with the “Make it happen.” positioning and a call to book a conversation.",
                "Ecosystem section showing how performance, branding and development connect.",
                "Recurring and one-off services, results and working method presented in sequence.",
                "Smooth scroll animations and counters that give the page rhythm.",
                "Calls to book a conversation throughout the page.",
            ],
        },
    },
]

# --------------------------------------------------------------------------
# Textos fixos da interface
# --------------------------------------------------------------------------
UI = {
    "pt": {
        "html_lang": "pt-BR",
        "og_locale": "pt_BR",
        "skip": "Pular para o conteúdo",
        "home_label": "Guilherme Borborema — início",
        "open_menu": "Abrir menu",
        "nav_label": "Principal",
        "lang_label": "Idioma",
        "nav": [("inicio", "Início"), ("sobre", "Sobre"), ("servicos", "Serviços"), ("projetos", "Projetos")],
        "contact": "Contato",
        "lets_talk": "Vamos conversar",
        "all_cases": "Todos os cases",
        "category": "Categoria",
        "segment": "Segmento",
        "deliverable": "Entrega",
        "visit": "Visitar site",
        "talk": "Quero um projeto assim",
        "screens_caption": "Primeira tela do site no computador e no celular.",
        "desktop_alt": "Página inicial do site {name} no computador",
        "mobile_alt": "Site {name} no celular",
        "logo_alt": "Logo {name}",
        "next": "Próximo case",
        "cta_kicker": "Contato",
        "cta_title": "Quer um resultado parecido<br />no <span class=\"gradient-text\">seu negócio?</span>",
        "cta_text": "Me conta como funciona a sua operação hoje e eu mostro como um agente de IA, um sistema sob medida ou um site que converte pode ajudar.",
        "cta_whatsapp": "Chamar no WhatsApp",
        "cta_email": "Enviar e-mail",
        "wa_label": "Conversar no WhatsApp",
        "footer": "Feito com código e café.",
        "footer_email": "E-mail",
        "back_top": "Voltar ao topo ↑",
        "title_suffix": "Case | Guilherme Borborema",
        "results_aria": "Resultados",
    },
    "en": {
        "html_lang": "en",
        "og_locale": "en_US",
        "skip": "Skip to content",
        "home_label": "Guilherme Borborema — home",
        "open_menu": "Open menu",
        "nav_label": "Main",
        "lang_label": "Language",
        "nav": [("home", "Home"), ("about", "About"), ("services", "Services"), ("projects", "Projects")],
        "contact": "Contact",
        "lets_talk": "Let's talk",
        "all_cases": "All case studies",
        "category": "Category",
        "segment": "Industry",
        "deliverable": "Deliverable",
        "visit": "Visit website",
        "talk": "I want a project like this",
        "screens_caption": "Home screen on desktop and mobile.",
        "desktop_alt": "{name} website home page on desktop",
        "mobile_alt": "{name} website on mobile",
        "logo_alt": "{name} logo",
        "next": "Next case study",
        "cta_kicker": "Contact",
        "cta_title": "Want similar results<br />for <span class=\"gradient-text\">your business?</span>",
        "cta_text": "Tell me how your operation works today and I'll show you how an AI agent, a custom system or a website that converts can help.",
        "cta_whatsapp": "Message on WhatsApp",
        "cta_email": "Send an email",
        "wa_label": "Chat on WhatsApp",
        "footer": "Made with code and coffee.",
        "footer_email": "Email",
        "back_top": "Back to top ↑",
        "title_suffix": "Case study | Guilherme Borborema",
        "results_aria": "Results",
    },
}

ICON_ARROW_LEFT = '<svg class="btn__icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>'
ICON_EXTERNAL = '<svg class="btn__icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>'
ICON_CHAT = '<svg class="btn__icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></svg>'
ICON_MAIL = '<svg class="btn__icon" viewBox="0 0 24 24" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>'
ICON_CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
ICON_WHATSAPP = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.04 2a9.93 9.93 0 0 0-8.53 15.02L2 22l5.1-1.46A9.94 9.94 0 1 0 12.04 2zm5.8 14.1c-.24.68-1.42 1.3-1.95 1.36-.5.06-1.13.09-1.82-.11-.42-.13-.96-.31-1.65-.61-2.9-1.25-4.8-4.18-4.94-4.37-.14-.2-1.18-1.57-1.18-3s.75-2.13 1.02-2.42c.26-.29.57-.36.77-.36h.55c.18 0 .42-.07.65.5.24.58.82 2 .89 2.15.07.14.12.31.02.5-.1.2-.14.31-.29.48-.14.17-.3.38-.43.5-.14.15-.29.3-.13.59.17.29.74 1.22 1.58 1.97 1.09.97 2 1.27 2.29 1.41.29.15.46.12.62-.07.17-.2.72-.84.91-1.13.19-.29.38-.24.65-.14.26.1 1.68.79 1.97.94.29.14.48.22.55.34.07.12.07.7-.17 1.37z"/></svg>'
FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='%2307080c'/%3E%3Ctext x='50%25' y='56%25' text-anchor='middle' dominant-baseline='middle' font-family='Arial' font-weight='700' font-size='28' fill='%23c8ff4d'%3EGB%3C/text%3E%3C/svg%3E"


def display_name(case, lang):
    return case.get("name_en", case["name"]) if lang == "en" else case["name"]


def render_cover(case, lang, base):
    """Capa sem prints (projetos sem site público): logo ou sigla sobre gradiente."""
    t = UI[lang]
    if case.get("logo"):
        classes = "project__logo case-cover__logo"
        if case.get("logo_plate"):
            classes += " project__logo--plate"
        visual = f'<img class="{classes}" src="{base}assets/logos/{case["logo"]}" alt="{escape(t["logo_alt"].format(name=display_name(case, lang)))}" />'
    else:
        visual = f'<span class="project__mono case-cover__mono">{case["mono"]}</span>'
    return f'''      <div class="case-cover reveal" style="--hue: {case["hue"]}">
        {visual}
      </div>'''


def render_screens(case, lang, base):
    t = UI[lang]
    name = display_name(case, lang)
    return f'''      <figure class="case-showcase reveal" style="--hue: {case["hue"]}">
        <div class="device device--desktop">
          <div class="project__browser device__bar"><span></span><span></span><span></span><em>{case["domain"]}</em></div>
          <img src="{base}assets/cases/{case["slug"]}-desktop.webp" alt="{escape(t["desktop_alt"].format(name=name))}" width="1200" height="750" />
        </div>
        <div class="device device--mobile">
          <img src="{base}assets/cases/{case["slug"]}-mobile.webp" alt="{escape(t["mobile_alt"].format(name=name))}" width="520" height="1125" loading="lazy" />
        </div>
        <figcaption class="case-showcase__caption">{t["screens_caption"]}</figcaption>
      </figure>'''


def render_page(case, lang, index):
    t = UI[lang]
    c = case[lang]
    base = "../" if lang == "pt" else "../../"          # raiz do site
    home = "../"                                        # página inicial do mesmo idioma
    other_lang = f"../en/cases/{case['slug']}.html" if lang == "pt" else f"../../cases/{case['slug']}.html"
    nxt = CASES[(index + 1) % len(CASES)]
    name = display_name(case, lang)
    projects_anchor = t["nav"][3][0]

    nav_links = "\n".join(
        f'          <li><a href="{home}#{anchor}" class="nav__link" data-nav-link>{label}</a></li>'
        for anchor, label in t["nav"]
    )
    contact_id = "contato" if lang == "pt" else "contact"
    nav_links += f'\n          <li><a href="#{contact_id}" class="nav__link" data-nav-link>{t["contact"]}</a></li>'

    if lang == "pt":
        lang_switch = f'''        <a href="{case['slug']}.html" class="nav__lang-link is-active" aria-current="page" hreflang="pt-BR" lang="pt-BR" title="Português">PT</a>
        <a href="{other_lang}" class="nav__lang-link" hreflang="en" lang="en" title="English version">EN</a>'''
    else:
        lang_switch = f'''        <a href="{other_lang}" class="nav__lang-link" hreflang="pt-BR" lang="pt-BR" title="Versão em português">PT</a>
        <a href="{case['slug']}.html" class="nav__lang-link is-active" aria-current="page" hreflang="en" lang="en" title="English">EN</a>'''

    actions = []
    if case.get("url"):
        label = c.get("cta_label", t["visit"])
        actions.append(f'''          <a href="{case["url"]}" target="_blank" rel="noopener noreferrer" class="btn btn--primary magnetic">
            {label}
            {ICON_EXTERNAL}
          </a>''')
    actions.append(f'''          <a href="#{contact_id}" class="btn btn--glass magnetic">{t["talk"]}</a>''')

    meta = f'''        <dl class="case-meta reveal">
          <div><dt>{t["category"]}</dt><dd>{escape(c["tag"])}</dd></div>
          <div><dt>{t["segment"]}</dt><dd>{escape(c["segment"])}</dd></div>
          <div><dt>{t["deliverable"]}</dt><dd>{escape(c["deliverable"])}</dd></div>
        </dl>'''

    visual = render_screens(case, lang, base) if case["screens"] else render_cover(case, lang, base)

    sections = "\n".join(
        f'''        <section class="case-block reveal">
          <h2 class="case-block__title">{title}</h2>
          <p class="case-block__text">{text}</p>
        </section>'''
        for title, text in c["sections"]
    )

    intro = f'\n          <p class="case-block__text">{c["list_intro"]}</p>' if c.get("list_intro") else ""
    items = "\n".join(f"            <li>{ICON_CHECK}<span>{item}</span></li>" for item in c["list"])
    list_block = f'''        <section class="case-block reveal">
          <h2 class="case-block__title">{c["list_title"]}</h2>{intro}
          <ul class="automation__list case-list">
{items}
          </ul>
        </section>'''

    results_block = ""
    if c.get("results"):
        cards = "\n".join(
            f'            <li class="case-result glass"><strong>{value}</strong><span>{label}</span></li>'
            for value, label in c["results"]
        )
        text = f'\n          <p class="case-block__text">{c["results_text"]}</p>' if c.get("results_text") else ""
        results_block = f'''
        <section class="case-block reveal">
          <h2 class="case-block__title">{c["results_title"]}</h2>
          <ul class="case-results" aria-label="{t["results_aria"]}">
{cards}
          </ul>{text}
        </section>'''

    nxt_name = display_name(nxt, lang)
    nxt_c = nxt[lang]

    return f'''<!DOCTYPE html>
<html lang="{t["html_lang"]}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{escape(name)} — {t["title_suffix"]}</title>
  <meta name="description" content="{escape(c["lead"])}" />
  <meta name="theme-color" content="#07080c" />

  <meta property="og:title" content="{escape(c["title"])}" />
  <meta property="og:description" content="{escape(c["lead"])}" />
  <meta property="og:type" content="article" />
  <meta property="og:locale" content="{t["og_locale"]}" />

  <link rel="icon" href="{FAVICON}" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet" />

  <link rel="stylesheet" href="{base}styles.css" />
  <script>document.documentElement.classList.add("js");</script>
</head>
<body class="case-page">
  <!-- Gerado por scripts/build_cases.py — edite o script, não este arquivo. -->
  <a class="skip-link" href="#content">{t["skip"]}</a>

  <div class="backdrop" aria-hidden="true">
    <div class="orb orb--1"></div>
    <div class="orb orb--2"></div>
    <div class="orb orb--3"></div>
    <div class="grid-lines"></div>
    <div class="grain"></div>
  </div>

  <header class="nav" data-nav>
    <div class="nav__inner container">
      <a href="{home}" class="nav__logo" aria-label="{t["home_label"]}">
        <span class="nav__logo-mark">GB</span>
        <span class="nav__logo-text">Guilherme Borborema</span>
      </a>

      <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="nav-menu" aria-label="{t["open_menu"]}" data-nav-toggle>
        <span></span><span></span>
      </button>

      <nav class="nav__menu" id="nav-menu" aria-label="{t["nav_label"]}">
        <ul class="nav__links">
{nav_links}
        </ul>
        <a href="#{contact_id}" class="btn btn--primary btn--sm nav__cta">{t["lets_talk"]}</a>
      </nav>

      <div class="nav__lang" role="group" aria-label="{t["lang_label"]}">
{lang_switch}
      </div>
    </div>
  </header>

  <main id="content">
    <article class="container case" style="--hue: {case["hue"]}">
      <header class="case-hero">
        <a class="case-back reveal" href="{home}#{projects_anchor}">{ICON_ARROW_LEFT}{t["all_cases"]}</a>
        <span class="tag reveal">{escape(c["tag"])}</span>
        <h1 class="case-hero__title reveal">{escape(c["title"])}</h1>
        <p class="case-hero__lead reveal">{escape(c["lead"])}</p>
        <div class="case-hero__actions reveal">
{chr(10).join(actions)}
        </div>
{meta}
      </header>

{visual}

      <div class="case-content">
{sections}
{list_block}{results_block}
      </div>

      <a class="case-next glass reveal spotlight" href="{nxt["slug"]}.html" style="--hue: {nxt["hue"]}">
        <span class="case-next__label">{t["next"]}</span>
        <span class="case-next__title">{escape(nxt_name)}</span>
        <span class="case-next__tag">{escape(nxt_c["tag"])}</span>
        <svg class="case-next__arrow" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </a>
    </article>

    <section class="section container" id="{contact_id}" aria-labelledby="{contact_id}-title" data-contact>
      <div class="cta glass reveal spotlight">
        <div class="cta__glow" aria-hidden="true"></div>
        <p class="section__kicker">{t["cta_kicker"]}</p>
        <h2 class="cta__title" id="{contact_id}-title">{t["cta_title"]}</h2>
        <p class="cta__text">{t["cta_text"]}</p>
        <div class="cta__actions">
          <a href="{WHATSAPP[lang]}" target="_blank" rel="noopener noreferrer" class="btn btn--primary btn--lg magnetic">
            {ICON_CHAT}
            {t["cta_whatsapp"]}
          </a>
          <a href="mailto:{EMAIL}" class="btn btn--glass btn--lg magnetic">
            {ICON_MAIL}
            {t["cta_email"]}
          </a>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer container">
    <p>© <span data-year>2026</span> Guilherme Borborema. {t["footer"]}</p>
    <ul class="footer__social">
      <li><a href="mailto:{EMAIL}">{t["footer_email"]}</a></li>
      <li><a href="{WHATSAPP[lang]}" target="_blank" rel="noopener noreferrer">WhatsApp</a></li>
      <li><a href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn</a></li>
      <li><a href="{INSTAGRAM}" target="_blank" rel="noopener noreferrer">Instagram</a></li>
      <li><a href="#content">{t["back_top"]}</a></li>
    </ul>
  </footer>

  <a class="wa-float" href="{WHATSAPP[lang]}" target="_blank" rel="noopener noreferrer" aria-label="{t["wa_label"]}">
    {ICON_WHATSAPP}
  </a>

  <script src="{base}script.js" defer></script>
</body>
</html>
'''


def main():
    for lang, out_dir in (("pt", ROOT / "cases"), ("en", ROOT / "en" / "cases")):
        out_dir.mkdir(parents=True, exist_ok=True)
        for i, case in enumerate(CASES):
            path = out_dir / f"{case['slug']}.html"
            path.write_text(render_page(case, lang, i), encoding="utf-8")
            print(f"✓ {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
