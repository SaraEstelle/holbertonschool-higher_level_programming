// On attend que le DOm soit entiérement chargé avant d'exécuter le code
// Car le script est dans le <head>, le <div id="hello"> n'existe pas encore
document.addEventListener('DOMContentLoaded', function () {
  // Séléctionne l'élement avec l'id "hello"
  const hello = document.querySelector('#hello');

  // Fait une requete GET vers l4API hellosalut en frnaçais
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
    // Affiche la traduction de "hello" dans le div #hello
      hello.textContent = data.hello;
    })
    .catch(function (error) {
      console.log('Erreur: ', error);
    });
});
