// On attend que le DOM soit entièrement chargé
document.addEventListener('DOMContenLoaded', function() {
  // Séléctionner le combo box, le bouton et le div d'affichage
  const languageCode = document.querySelector('#language_code');
  const btnTranslate = document.querySelector('#btn_translate');
  const hello = document.querySelector('#hello');

  // Ecouter le clic sur le bouton "Translate"
  btnTranslate.addEventListener('click', function () {
    // Récuperer la valeur séléctionné dans le combo box ( ex: "fr , en , es")
    const lang = languageCode.value;

    // Construit l'URL avec le code langue séléctionné
    fetch('https://hellosalut.stefanbohacek.com/?lang=' + lang)
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        // affiche la traduction da,s le div #hello
        hello.textContent = data.hello;
    })
    .catch(function (error) {
        console.log('Erreur: ', error);
    });
  });
});
