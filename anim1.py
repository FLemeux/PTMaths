from PIL import Image, ImageDraw
import math
import os

def dessiner_segment_pointille(draw, x1, y1, x2, y2, couleur="black", pas=5, width=1):
    longueur = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    nb_points = int(longueur / pas)

    for i in range(nb_points):
        if i % 2 == 0:
            draw.line(
                (
                    x1 + (i * (x2 - x1) // nb_points),
                    y1 + (i * (y2 - y1) // nb_points),
                    x1 + ((i + 1) * (x2 - x1) // nb_points),
                    y1 + ((i + 1) * (y2 - y1) // nb_points),
                ),
                fill=couleur,
                width=width
            )

def dessiner_cercle(t, image_precedente=None):
    # Définition des dimensions de l'image
    largeur_canvas = 300
    hauteur_canvas = 300

    # Création de l'image blanche
    if image_precedente is None:
        image = Image.new("RGB", (largeur_canvas, hauteur_canvas), "white")
    else:
        image = image_precedente.copy()

    draw = ImageDraw.Draw(image)

    # Centre du cercle
    centre_x, centre_y = largeur_canvas // 2, hauteur_canvas // 2

    # Rayon du cercle
    rayon_cercle = 100

    # Points A et B sur le cercle
    angle_t = math.radians(t)
    point_a_x = centre_x + (rayon_cercle * math.cos(angle_t))
    point_a_y = centre_y + (rayon_cercle * math.sin(angle_t))

    point_b_x = centre_x + (rayon_cercle * math.cos(2 * angle_t))
    point_b_y = centre_y + (rayon_cercle * math.sin(2 * angle_t))

    point_c_x=centre_x + rayon_cercle/3 *(2*math.cos(angle_t)+math.cos(2*angle_t))
    point_c_y=centre_x + rayon_cercle/3 *(2*math.sin(angle_t)+math.sin(2*angle_t))

    # Dessin du cercle
    draw.ellipse(
        [
            (centre_x - rayon_cercle, centre_y - rayon_cercle),
            (centre_x + rayon_cercle, centre_y + rayon_cercle),
        ],
        outline="red",
    )

    # Dessin des points A et B
    draw.ellipse([(point_a_x - 2, point_a_y - 2), (point_a_x + 2, point_a_y + 2)], fill="blue")
    draw.ellipse([(point_b_x - 2, point_b_y - 2), (point_b_x + 2, point_b_y + 2)], fill="blue")
    draw.ellipse([(point_c_x - 2, point_c_y - 2), (point_c_x + 2, point_c_y + 2)], fill="red")

    # Dessin du segment en pointillé reliant les points A et B
    dessiner_segment_pointille(draw, point_a_x, point_a_y, point_b_x, point_b_y, couleur="blue")

    return image

# Chemin du sous-dossier pour sauvegarder les images
sous_dossier = "images_cercles"
chemin_sous_dossier = os.path.join(os.getcwd(), sous_dossier)

# Créer le sous-dossier s'il n'existe pas déjà
os.makedirs(chemin_sous_dossier, exist_ok=True)

# Variable pour stocker l'image précédente
image_precedente = None

# Faire varier t entre 0 et 360 degrés (ou 0 et 2*pi radians)
for i, t in enumerate(range(0, 370, 10)):
    image_resultante = dessiner_cercle(t, image_precedente)

    # Formater l'indice i en deux chiffres (00, 01, 02, ..., 36)
    indice_formatte = f"{i:02}"

    # Construire le nom du fichier
    nom_fichier = os.path.join(chemin_sous_dossier, f"image_{indice_formatte}.png")
    image_resultante.save(nom_fichier)

    # Mettre à jour l'image précédente avec l'image actuelle pour la prochaine itération
    image_precedente = image_resultante

print("Sauvegarde terminée !")
