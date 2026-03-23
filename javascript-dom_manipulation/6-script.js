// Séléctionne l4élément avec l'id "character"
const character = document.querySelector('#character');

// Fait une requete GET vers l'API Star Wars avec Fetch
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  // .then() s'excute quand la réponse arrive
  // on convertit la réponse en objet JavaScript (JSON)
  .then(function (reponse) {
    return reponse.json();
  })
  // .then() s'excuste quand le JSON est pret
  // data contient toutes les infos du personnage
  .then(function (data) {
  // Affiche le nom du personnage dans le div #character
    character.textContent = data.name;
  })
  // .catch() s'excute si une erreur se produit
  .catch(function (error) {
    console.log('Erreur: ', error);
  });
