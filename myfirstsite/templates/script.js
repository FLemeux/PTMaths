// Détecte le défilement de la colonne de droite
document.querySelector(".right-column").addEventListener("scroll", function() {
  // Obtient la valeur de défilement vertical de la colonne de droite
  var scrollTop = this.scrollTop;
  
  // Applique la valeur de défilement à la colonne de gauche
  document.querySelector(".left-column").style.top = 110 + scrollTop + "px";
});
