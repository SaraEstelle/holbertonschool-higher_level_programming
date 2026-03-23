// Séléctionne l'element <header> dans le DOM
const header = document.querySelector('header');

// Séléctionne l'élément qui a l'id "red_header"
const redHeader = document.querySelector('#red_header');

// Ecoute le clic sur l'élément red_header
redHeader.addEventListener('click', function () {
  // Ajoute la classe CSS "red" à l'élément header
  // la classe .red est définie dans le CSS : color: #FF0000
  header.classList.add('red');
});
