from PIL import Image, ImageDraw
import os

# Paramètres de l'animation
largeur_canvas = 400
hauteur_canvas = 200
rayon_cercle = 20
nombre_images = 30

# Créer un dossier pour stocker les images générées
dossier_images = "animation_images"
os.makedirs(dossier_images, exist_ok=True)

# Fonction pour dessiner le cercle à une position donnée
def dessiner_cercle(position_x, position_y):
    image = Image.new("RGB", (largeur_canvas, hauteur_canvas), "white")
    draw = ImageDraw.Draw(image)
    draw.ellipse(
        [
            (position_x - rayon_cercle, position_y - rayon_cercle),
            (position_x + rayon_cercle, position_y + rayon_cercle),
        ],
        fill="red",
    )
    return image

# Générer les images de l'animation
for i in range(nombre_images):
    x = (i * largeur_canvas) // nombre_images
    y = hauteur_canvas // 2
    image = dessiner_cercle(x, y)
    nom_image = "image_{:02d}.png".format(i)
    chemin_image = os.path.join(dossier_images, nom_image)
    image.save(chemin_image)

# Imprimer le nombre d'images générées
print("{} images générées dans le dossier '{}'.format(nombre_images, dossier_images)")
