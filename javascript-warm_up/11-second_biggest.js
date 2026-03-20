#!/usr/bin/node
const liste = (process.argv.slice(2));
const tab = liste.map((element) => parseInt(element));

if (tab.length === 0 || tab.length === 1) {
  console.log(0);
} else {
  // Crée un nouveau tableau 'unique' avec uniquement des valeurs uniques (supprime les doublons avec Set (...new Set(nom_tab)))
  const unique = [...new Set(tab)];
  // Trie le tableau 'unique' en ordre décroissant (du plus grand au plus petit avec sort((a, b) => b - a))
  const n = unique.sort((a, b) => b - a);
  // Affiche le deuxième plus grand nombre (index 1 après le tri)
  console.log(n[1]);
}
