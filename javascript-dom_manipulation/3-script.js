// Sélétionne l'élément  <header> dans le DOM
const header = document.querySelector('header');

// Séléctionne l'élément qui a l'id "toggle_header"
const toggleHeader = document.querySelector('#toggle_header');

// Ecoute le clic sur l'élément toggle_header
toggleHeader.addEventListener('click', function () {
  // Si le header a la classe "red", on le remplace par "green"
  // Si le header a la classe "green", on le remplace par "red"
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
