// Revue de veille : filtres par catégorie, mot clé, période et recherche libre.
// Sans JavaScript, toutes les actualités restent visibles.
(function () {
  var form = document.querySelector('.veille-filtres');
  if (!form) return;
  var items = Array.prototype.slice.call(document.querySelectorAll('.veille-item'));
  var weeks = Array.prototype.slice.call(document.querySelectorAll('.veille-semaine'));
  var chips = Array.prototype.slice.call(form.querySelectorAll('.veille-chip'));
  var kw = form.querySelector('[data-filtre="kw"]');
  var mois = form.querySelector('[data-filtre="mois"]');
  var q = form.querySelector('[data-filtre="q"]');
  var compte = form.querySelector('.veille-compte');
  var vide = document.querySelector('.veille-vide');
  var cat = '';

  function norm(s) {
    return (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  }

  function apply() {
    var k = kw.value, m = mois.value, t = norm(q.value.trim());
    var n = 0;
    items.forEach(function (it) {
      var ok = (!cat || it.dataset.cat === cat) &&
        (!k || it.dataset.kw.split('|').indexOf(k) !== -1) &&
        (!m || it.dataset.mois === m) &&
        (!t || norm(it.textContent).indexOf(t) !== -1);
      it.hidden = !ok;
      if (ok) n++;
    });
    weeks.forEach(function (w) {
      w.hidden = !w.querySelector('.veille-item:not([hidden])');
    });
    compte.textContent = n + (n > 1 ? ' actualités' : ' actualité');
    vide.hidden = n !== 0;
  }

  chips.forEach(function (c) {
    c.addEventListener('click', function () {
      cat = c.dataset.val;
      chips.forEach(function (o) { o.setAttribute('aria-pressed', o === c ? 'true' : 'false'); });
      apply();
    });
  });
  [kw, mois].forEach(function (s) { s.addEventListener('change', apply); });
  q.addEventListener('input', apply);
  apply();
})();
