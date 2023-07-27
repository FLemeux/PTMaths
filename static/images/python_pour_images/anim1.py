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
def dessiner_cercle(t):
    # Définition des dimensions de l'image
    largeur_canvas = 300
    hauteur_canvas = 300

    # Création de l'image blanche
    image = Image.new("RGB", (largeur_canvas, hauteur_canvas), "white")
    draw = ImageDraw.Draw(image)

    # Centre du cercle
    centre_x, centre_y = largeur_canvas // 2, hauteur_canvas // 2

    # Rayon du cercle
    rayon_cercle = 100

    # Points A et B sur le cercle
    angle_t = math.radians(t)
    point_a_x = centre_x + int(rayon_cercle * math.cos(angle_t))
    point_a_y = centre_y + int(rayon_cercle * math.sin(angle_t))

    point_b_x = centre_x + int(rayon_cercle * math.cos(2 * angle_t))
    point_b_y = centre_y + int(rayon_cercle * math.sin(2 * angle_t))

    # Dessin du cercle
    draw.ellipse(
        [
            (centre_x - rayon_cercle, centre_y - rayon_cercle),
            (centre_x + rayon_cercle, centre_y + rayon_cercle),
        ],
        outline="red",
    )

    # Dessin des points A et B
    draw.ellipse([(point_a_x - 5, point_a_y - 5), (point_a_x + 5, point_a_y + 5)], fill="blue")
    draw.ellipse([(point_b_x - 5, point_b_y - 5), (point_b_x + 5, point_b_y + 5)], fill="blue")

    # Dessin du segment en pointillé reliant les points A et B
    draw.line((point_a_x, point_a_y, point_b_x, point_b_y), fill="blue", dash=(4, 4))

    return image

image_resultante = dessiner_cercle(30)

# Sauvegarde de l'image
image_resultante.save("cercle.png")

"""

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
"""
