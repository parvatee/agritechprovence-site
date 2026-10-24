// Envoi du formulaire de contact via Web3Forms, sans quitter la page
(function () {
  var f = document.getElementById('contact-form');
  if (!f) return;
  var status = f.querySelector('.form-status');
  var btn = f.querySelector('button[type="submit"]');
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    if (f.botcheck && f.botcheck.checked) return;
    btn.disabled = true; btn.textContent = 'Envoi…';
    status.className = 'form-status'; status.textContent = '';
    var data = Object.fromEntries(new FormData(f));
    if (data.email) data.replyto = data.email;
    fetch(f.action, { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify(data) })
      .then(function (r) { return r.json(); })
      .then(function (j) {
        if (j.success) {
          f.reset();
          status.className = 'form-status ok';
          status.textContent = 'Merci, votre message est bien arrivé. Nous revenons vers vous sous 48 heures.';
        } else { throw new Error(j.message); }
      })
      .catch(function () {
        status.className = 'form-status err';
        status.innerHTML = 'L’envoi n’a pas abouti. Écrivez-nous à <a href="mailto:Julie.Demarigny@agritechprovence.com">Julie.Demarigny@agritechprovence.com</a>.';
      })
      .finally(function () { btn.disabled = false; btn.textContent = 'Envoyer'; });
  });
})();
