// Séléctionne l'élément <header> danss le DOM
const header = document.querySelector('header');

// Séléctionne l'élément qui a l'id "red_header"
// querySelector avec # cible un id
const redHeader = document.querySelector('#red_header');

// Ecoute le clic  sur l'element red_header
// Quand l'utilisateur clique, la fonction callback s'excute
redHeader.addEventListener('click', function () {
  // Change la couleur du texte du header en rouge
  header.style.color = '#FF0000';
});
