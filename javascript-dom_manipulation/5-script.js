// Séléctionne l'élément  <header> dans le DOM
const header = document.querySelector('header');

// Séléctionne l'élément avec l'id "update_header"
const updateHeader = document.querySelector('#update_header');

// Ecoute le clic sur l'élément update_header
updateHeader.addEventListener('click', function () {
  // Remplace le texte du header par "New Header!!!"
  header.textContent = 'New Header!!!';
});
