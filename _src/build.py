#!/usr/bin/env python3
"""Assemble les pages du site : en-tete et pied de page communs + corps de page.
Usage : python3 _src/build.py  (depuis la racine du site)
Modifier les textes dans _src/pages/*.html, puis relancer ce script."""
import pathlib, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "_src" / "pages"
SITE_URL = "https://www.agritechprovence.com"
LINKEDIN = "https://www.linkedin.com/in/jdemarigny/"
INSTAGRAM = "#"  # TODO : lien du compte Instagram

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
    ("mentions-legales.html", "Mentions légales | Agritech Provence",
     "Mentions légales et données personnelles du site Agritech Provence.", None),
    ("404.html", "Page introuvable | Agritech Provence", "Cette page n'existe pas.", None),
]

MENU = [("solution", "solution.html", "Notre solution"), ("resultats", "resultats.html", "Résultats 2026"),
        ("equipe", "equipe.html", "Qui sommes-nous"), ("prix", "prix.html", "Prix et soutiens"),
        ("presse", "presse.html", "Presse")]

ICON_LI = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="#CFE07A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>'
ICON_IG = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="#CFE07A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.5"/></svg>'


def page(fname, title, desc, key, body):
    cur = ' aria-current="page"'
    items = "\n".join(
        f'<li><a href="{href}"{cur if k == key else ""}>{label}</a></li>'
        for k, href, label in MENU)
    contact_cur = ' aria-current="page"' if key == "contact" else ""
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
<a class="brand" href="index.html"><img src="assets/img/logo.png" alt="" width="48" height="48"><span>AGRITECH PROVENCE</span></a>
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
<ul class="menu" id="menu">
{items}
<li><a class="btn btn--signal" href="contact.html"{contact_cur}>Contact</a></li>
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
<script src="assets/js/nav.js"></script>
</body>
</html>
'''


def main():
    urls = []
    for fname, title, desc, key in PAGES:
        body = (SRC / fname).read_text(encoding="utf-8")
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
