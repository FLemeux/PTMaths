// Récupérer l'élément img contenant le GIF
const animationImg = document.getElementById('animation-img');

// Fonction pour redémarrer l'animation
function restartAnimation() {
    animationImg.style.display = 'none'; // Masquer l'image
    animationImg.style.display = 'block'; // Afficher à nouveau l'image pour la relancer
}

// Écouter l'événement "load" de l'image pour relancer l'animation une fois que toutes les frames ont été affichées
animationImg.addEventListener('load', function() {
    restartAnimation();
});
