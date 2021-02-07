"""
Script de contrôle du projet.
"""

from werkzeug.utils import secure_filename
from flask import abort
import metiers.metierfilrouge

# fichiers dont le contenu est affiché en clair
EXTENSIONS_DATA_BRUTES = ['csv','md','txt']
# fichiers dont le contenu est encodé en base64
EXTENSIONS_DATA_BASE_SOIXANTE_QUATRE = ['gif','jpeg','jpg','pdf','png']
# fichiers authorisés
ALLOWED_EXTENSIONS = ['csv','gif','jpeg','jpg','md','pdf','png','txt']
# fichiers images authorisés
ALLOWED_IMAGES = ['jpg','jpeg','png']
# répertoire de stockage des fichiers
UPLOAD_DIRECTORY = './uploadfiles/'

# pylint: disable=no-else-return

def controle_extension(nom_fichier):
    """
    Renvoie vrai si le fichier possède une extension autorisée
    qu'elle soit en minuscule ou en majuscule.
    Parameters
    ----------
    nom_fichier : string
    Returns
    -------
    boolean
    """
    return '.' in nom_fichier and nom_fichier.rsplit('.', 1)[1].lower() \
            in ALLOWED_EXTENSIONS

def aiguiller(request):
    """
    Contrôle si l'extension du fichier est autorisée
    et en fonction oriente le traitement.
    Parameters
    ----------
    request : flask.request
    Returns
    -------
    Cette fonction retourne les métadonnées et
    le contenu du fichier passé en paramètre au format JSON.
    {
        'Précision': '',
        'Type mime': '',
        'Taille en octets': '',
        'Nom de fichier': '',
        'Extension': '',
        'Contenu': ''
    }

    """
    fichier_envoye = request.files['monFichier']
    nom_fichier = secure_filename(fichier_envoye.filename)
    if fichier_envoye:
        # je vérifie qu'un fichier a bien été envoyé
        if controle_extension(nom_fichier):
            # je vérifie que son extension est valide
            # fichier_envoye.save(UPLOAD_DIRECTORY + nom_fichier)
            #Aiguillage vers le bon traitement métier
            if '.' in nom_fichier and nom_fichier.rsplit('.', 1)[1].lower() \
                    in EXTENSIONS_DATA_BRUTES:
                return metiers.metierfilrouge.generer_json_data_brutes(request)
            elif '.' in nom_fichier and nom_fichier.rsplit('.', 1)[1].lower() \
                    in EXTENSIONS_DATA_BASE_SOIXANTE_QUATRE:
                return metiers.metierfilrouge.generer_json_data_basesoixantequatre(request)
            else:
                return metiers.metierfilrouge.generer_json_vierge(request)
        else:
            return 'Accès autorisé mais le fichier ne porte pas une extension autorisée !\n'
    else:
        return 'Accès autorisé mais vous avez oublié le fichier en paramètre !\n'

def controler_images(request):
    fichier_envoye = request.files['monFichier']
    nom_fichier = secure_filename(fichier_envoye.filename)
    if not ('.' in nom_fichier and nom_fichier.rsplit('.', 1)[1].lower() \
                    in ALLOWED_IMAGES):
        abort(415)
    return metiers.metierfilrouge.detection_labels(request)
