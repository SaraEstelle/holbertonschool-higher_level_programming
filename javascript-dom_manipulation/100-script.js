// On attend que le DOM soit entièrement chargé
document.addEventListener('DOMContentLoaded', function () {
  // Séléctionne les trois boutons et la liste
  const addItem = document.querySelector('#add_item');
  const removeItem = document.querySelector('#remove_item');
  const clearList = document.querySelector('#clear_list');
  const myList = document.querySelector('.my_list');

  // Ajouter un <li>Item</li> à la fin de la liste
  addItem.addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });

  // Supprime le dernier <li> de la liste
  removeItem.addEventListener('click', function () {
    const lastItem = myList.lastElementChild;
    if (lastItem) {
        myList.removeChild(lastItem);
    }
  });

  // Supprime tous les <li> de la liste
  clearList.addEventListener('click', function () {
    myList.innerHTML = '';
  });
});
