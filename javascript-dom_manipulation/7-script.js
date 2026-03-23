// Séléctionne la liste <ul> avec l'id "list_movies"
const listMovies = document.querySelector('#list_movies');

// Fait une requete GET vers l'API Star Wars pour récupérer tous les films
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  // Convertit la réponse en objet JS
  .then(function (response) {
    return response.json();
  })
  // data.results contient le tableau de tous les films
  .then(function (data) {
  // Pour chaque film dans le tableau results
  data.results.forEach(function (film) {
  // Cree un nouvel element <li> en mémoire
  const newItem = document.createElement('li');

  // Ajoute le titre du film dans le <li>
  newItem.textContent = film.title;

  // Insère le <li> dans la liste <ul>
  listMovies.appendChild(newItem);
  });
})
// Gère les erreurs réseau
.catch(function (error) {
    console.log('Erreur: ', error);
});
