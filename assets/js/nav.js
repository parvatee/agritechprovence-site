// Menu mobile
(function () {
  var b = document.querySelector('.menu-toggle');
  var m = document.getElementById('menu');
  if (!b || !m) return;
  b.addEventListener('click', function () {
    var open = m.classList.toggle('is-open');
    b.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
})();
