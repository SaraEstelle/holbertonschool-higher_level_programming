// Séléctionne l'élément avec l'id "add_item"
const addItem = document.querySelector('#add_item');

// Séléctionne la liste <ul> avec la classe "my_list"
const myList = document.querySelector('.my_list');

// 2coute le clic sur l'élément add_item
addItem.addEventListener('click', function () {
  // Crée un nouvel élément <li> en mémoire
  const newItem = document.createElement('li');

  // Ajoute le texte "Item" dans le nouvel élément
  newItem.textContent = 'Item';

  // Insère le nouvel élément à la fin de la liste <ul>
  myList.appendChild(newItem);
});
