# Site Agritech Provence

Site statique publié avec GitHub Pages.

- Textes des pages : `_src/pages/*.html`
- En-tête, pied de page, liens LinkedIn et Instagram : `_src/build.py`
- Après modification : `python3 _src/build.py` depuis la racine, puis commit.
- Revue de veille (section `#veille` de `actualites.html` ; `veille.html` redirige vers elle) : entrées dans `_src/veille.json` (date, semaine, categorie parmi Réglementaire, Agricole, Technique, Agronomique, titre, source, url, pays, mots_cles, resume, lecture). Ajoutées chaque lundi par la tâche de veille dans une pull request, à valider avant fusion.
