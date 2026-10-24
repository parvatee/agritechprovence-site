#!/usr/bin/env python3
"""Assemble les pages du site : en-tete et pied de page communs + corps de page.
Usage : python3 _src/build.py  (depuis la racine du site)
Modifier les textes dans _src/pages/*.html, puis relancer ce script."""
import pathlib, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "_src" / "pages"
SITE_URL = "https://www.agritechprovence.com"
LINKEDIN = "https://www.linkedin.com/in/jdemarigny/"
INSTAGRAM = "https://www.instagram.com/agritechprovence"

PAGES = [
    # fichier, titre, description, entree de menu
    ("index.html", "Agritech Provence | Drone et IA pour les vignes bio de Provence",
     "Agritech Provence survole les vignes bio de Provence avec un drone multispectral et une intelligence artificielle, et dit aux vignerons où aller voir.", "accueil"),
    ("solution.html", "Notre solution | Agritech Provence",
     "Mildiou, oïdium, flavescence dorée, manquants : notre méthode de détection par drone multispectral, de la carte au terrain.", "solution"),
    ("resultats.html", "Résultats 2026 | Agritech Provence",
     "Ce que le drone a vu dans les vignes : premiers résultats de la campagne 2026, présentés par cépage.", "resultats"),
    ("equipe.html", "Qui sommes-nous | Agritech Provence",
     "Une jeune entreprise d'Apt, deux télépilotes, des partenaires de recherche et des vignerons engagés.", "equipe"),
    ("prix.html", "Prix et soutiens | Agritech Provence",
     "101 Femmes Entrepreneures, Be a Boss Women Tour, Bpifrance, Initiative Terres de Vaucluse, Force Femmes.", "prix"),
    ("presse.html", "Presse | Agritech Provence",
     "Articles, communiqués et kit presse d'Agritech Provence.", "presse"),
    ("contact.html", "Contact | Agritech Provence",
     "Vigneron, journaliste, institution ou partenaire : parlons de vos vignes.", "contact"),
    ("actualites.html", "Actualités et veille | Agritech Provence",
     "Actualités d'Agritech Provence et veille sur le drone agricole, l'imagerie multispectrale et la santé de la vigne.", "actualites"),
    ("mentions-legales.html", "Mentions légales | Agritech Provence",
     "Mentions légales et données personnelles du site Agritech Provence.", None),
    ("404.html", "Page introuvable | Agritech Provence", "Cette page n'existe pas.", None),
]

MENU = [("solution", "solution.html", "Notre solution"), ("resultats", "resultats.html", "Résultats 2026"),
        ("equipe", "equipe.html", "Qui sommes-nous"), ("prix", "prix.html", "Prix et soutiens"),
        ("actualites", "actualites.html", "Actualités"), ("presse", "presse.html", "Presse")]

ICON_LI = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="#CFE07A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>'
ICON_IG = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="#CFE07A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.5"/></svg>'


def page(fname, title, desc, key, body):
    cur = ' aria-current="page"'
    items = "\n".join(
        f'<li><a href="{href}"{cur if k == key else ""}>{label}</a></li>'
        for k, href, label in MENU)
    contact_cur = ' aria-current="page"' if key == "contact" else ""
    extra_js = '\n<script src="assets/js/form.js"></script>' if key == "contact" else ""
    canonical = SITE_URL + "/" + ("" if fname == "index.html" else fname)
    body = body.replace("{{LINKEDIN}}", LINKEDIN).replace("{{INSTAGRAM}}", INSTAGRAM) \
               .replace("{{ICON_LI}}", ICON_LI).replace("{{ICON_IG}}", ICON_IG)
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{SITE_URL}/assets/img/mildiou-foyers.jpg">
<meta property="og:locale" content="fr_FR">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Source+Sans+3:wght@400;600&family=JetBrains+Mono:wght@400&display=swap">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="site-header">
<div class="wrap nav">
<a class="brand" href="index.html"><img src="assets/img/logo.png" alt="Logo Agritech Provence" width="68" height="68"><span><b>AGRITECH PROVENCE</b><small>Drone · multispectral · IA</small></span></a>
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
<ul class="menu" id="menu">
{items}
<li><a class="btn btn--nuit" href="contact.html"{contact_cur}>Contact</a></li>
</ul>
</div>
</header>
<main id="contenu">
{body.strip()}
</main>
<footer class="site-footer">
<div class="wrap">
<div class="brand-mini"><img src="assets/img/logo.png" alt="" width="40" height="40"><span>Agritech Provence · Drone et intelligence artificielle pour les vignes bio de Provence · Apt, Vaucluse</span></div>
<nav aria-label="Liens secondaires"><a href="{LINKEDIN}">LinkedIn</a><a href="{INSTAGRAM}">Instagram</a><a href="presse.html">Presse</a><a href="mentions-legales.html">Mentions légales</a></nav>
</div>
</footer>
<script src="assets/js/nav.js"></script>{extra_js}
</body>
</html>
'''


# Revue de presse, du plus recent au plus ancien. url = None tant que le lien n'est pas connu.
PRESS = [
    # (media, date, titre, url, libelle du lien, affiche en page d'accueil)
    ("La Provence", "6 oct. 2026", "Avec son drone, Agritech Provence décèle les maladies de la vigne vauclusienne",
     "https://www.laprovence.com/article/ecoplanete/51222930973722/avec-son-drone-agritech-provence-decele-les-maladies-de-la-vigne-vauclusienne", "Lire l'article", True),
    ("Les Rebondisseurs Français", "28 sept. 2026", "Be a Boss Women Tour 2026 : le rebond au cœur de l'entrepreneuriat féminin",
     "https://www.lesrebondisseursfrancais.fr/be-a-boss-women-tour-2026-le-rebond-au-coeur-de-lentrepreneuriat-feminin/", "Lire l'article", False),
    ("Be a Boss", "25 sept. 2026", "Be a boss Awards 2026 : les trois lauréates de la 12e édition",
     "https://www.beaboss.fr/actualites-1056/be-a-boss-awards-2026-les-trois-laureates-de-la-12e-edition-55929", "Lire l'article", True),
    ("Vaucluse Hebdo", "22 sept. 2026", "Apt : Julie Demarigny révolutionne l'agriculture avec Agritech Provence",
     "https://mesinfos.fr/84400-apt/apt-julie-demarigny-revolutionne-l-agriculture-avec-agritech-provence-339279.html", "Lire l'article", True),
    ("Presse Agence", "8 sept. 2026", "Le concours « 101 femmes » dévoile ses lauréates 2026",
     "https://presseagence.fr/paris-entrepreneuriat-feminin-le-concours-101-femmes-devoile-ses-laureates-2026/", "Lire l'article", False),
    ("Immo Project", "22 juil. 2026", "Rencontre les finalistes du Be a Boss Women Tour Sud",
     "https://www.immoproject.fr/rencontre-les-finalistes-du-be-a-boss-women-tour-sud-qui-dominera/", "Lire l'article", False),
    ("Be a Boss", "6 juil. 2026", "Be a Boss Women Tour Sud : les finalistes !",
     "https://www.beaboss.fr/creation-dentreprise-1024/be-a-boss-women-tour-sud-deux-entrepreneures-selectionnees-55443", "Lire l'article", False),
    ("ICI Vaucluse", "2026", "Des drones expérimentés pour surveiller les vignes de Vaucluse",
     "https://www.ici.fr/emissions/l-info-d-ici-ici-vaucluse/des-drones-experimentes-pour-surveiller-les-vignes-de-vaucluse-9517578", "Écouter", False),
    # A garder en dernier (demande de Julie)
    ("La Marseillaise", "23 oct. 2026", "Des drones et l'IA pour traquer les maladies de la vigne",
     "https://www.lamarseillaise.fr/economie/des-drones-et-l-ia-pour-traquer-les-maladies-de-la-vigne-CJ20834116", "Lire l'article", False),
]


def press_card(m, d, t, url, label, home=False):
    inner = f'<span class="eyebrow">{m} · {d}</span><span class="card-title">{html.escape(t)}</span>'
    if url:
        return f'<a class="card" href="{url}">{inner}<span class="lien">{label}</span></a>'
    return f'<div class="card">{inner}</div>'


POSTS_DIR = ROOT / "_src" / "posts"
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]


def load_posts():
    """Chaque article : _src/posts/<slug>.html, commencant par un commentaire JSON
    <!--{"title":..., "date":"AAAA-MM-JJ", "category":..., "summary":..., "image":...}-->"""
    import json, re
    posts = []
    for f in POSTS_DIR.glob("*.html"):
        txt = f.read_text(encoding="utf-8")
        m = re.match(r"\s*<!--(.*?)-->", txt, re.S)
        meta = json.loads(m.group(1))
        meta["slug"] = f.stem
        meta["body"] = txt[m.end():]
        y, mo, d = meta["date"].split("-")
        meta["date_fr"] = f"{int(d)} {MOIS[int(mo) - 1]} {y}"
        posts.append(meta)
    return sorted(posts, key=lambda p: p["date"], reverse=True)


def card(p):
    img = f'<img src="{p["image"]}" alt="" loading="lazy" style="aspect-ratio:16/9;object-fit:cover;border-radius:6px;background:#000">' if p.get("image") else ""
    return (f'<a class="card" href="article-{p["slug"]}.html">{img}<span class="eyebrow">{p["category"]} · {p["date_fr"]}</span>'
            f'<span class="card-title">{html.escape(p["title"])}</span><span class="muted" style="font-size:16px">{html.escape(p["summary"])}</span>'
            f'<span class="lien">Lire</span></a>')


def article_body(p):
    return f'''<article>
<section class="section--nuit"><div class="wrap page-hero stack narrow" style="margin-left:auto;margin-right:auto">
<p class="eyebrow"><a href="actualites.html" style="color:inherit">Actualités</a> · {p["category"]} · {p["date_fr"]}</p>
<h1 style="font-size:clamp(34px,4.6vw,52px)">{html.escape(p["title"])}</h1>
<p class="lead muted">{html.escape(p["summary"])}</p>
</div></section>
<section class="section"><div class="wrap narrow prose">
{p["body"].strip()}
<p style="margin-top:48px"><a class="btn btn--nuit" href="actualites.html">Toutes les actualités</a></p>
</div></section>
</article>'''


def main():
    urls = []
    posts = load_posts()
    for p in posts:
        fname = f"article-{p['slug']}.html"
        (ROOT / fname).write_text(page(fname, p["title"] + " | Agritech Provence", p["summary"], "actualites", article_body(p)), encoding="utf-8")
        urls.append(SITE_URL + "/" + fname)
    cards_all = "\n".join(card(p) for p in posts)
    cards_latest = "\n".join(card(p) for p in posts[:3])
    for fname, title, desc, key in PAGES:
        body = (SRC / fname).read_text(encoding="utf-8").replace("{{POSTS}}", cards_all).replace("{{LATEST}}", cards_latest).replace("{{PRESS}}", "\n".join(press_card(*x) for x in PRESS)).replace("{{PRESS3}}", "\n".join(press_card(*x) for x in PRESS if x[5]))
        (ROOT / fname).write_text(page(fname, title, desc, key, body), encoding="utf-8")
        if fname != "404.html":
            urls.append(SITE_URL + "/" + ("" if fname == "index.html" else fname))
    sm = "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}\n</urlset>\n', encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
    print("ok", len(PAGES), "pages")


if __name__ == "__main__":
    main()
