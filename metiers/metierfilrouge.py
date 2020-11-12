"""
Script métier du projet.
"""

import base64
from flask import jsonify
from werkzeug.utils import secure_filename

# pylint: disable=too-many-arguments

def contruire_retour(precision, nom_fichier, extension, mime_type, taille, contenu):
    """
    Construit un retour Json avec les métadata du fichier uploadé.
    Parameters
    ----------
    precision : string
    nom_fichier : string
    extension : string
    mime_type : string
    taille : int
    contenu : string
    Returns
    -------
    json
    """
    return {'Précision':precision, 'Nom du fichier':nom_fichier, \
            'extension':extension, 'Mime type':mime_type, \
            'Taille en octets':taille, 'Contenu':contenu}

def generer_json_data_brutes(request):
    """
    Cette fonction génère un JSON avec les métadonnées et le contenu brute
    d'un fichier CSV ou TXT ou MD passé dans la requête.
    Returns
    -------
    {
        'Précision': '',
        'Type mime': '',
        'Taille en octets': '',
        'Nom de fichier': '',
        'Extension': '',
        'Contenu': ''
    }
    """
    precision = 'Format de fichier où les données sont affichées en brute !'
    contenu = request.files['monFichier'].read()
    mime_type = request.files['monFichier'].mimetype
    taille = request.headers.get('Content-Length')
    nom_fichier = secure_filename(request.files['monFichier'].filename)
    extension = nom_fichier.split(".")[-1].lower()
    return jsonify(contruire_retour(precision, nom_fichier, extension, mime_type, taille, contenu))

def generer_json_data_basesoixantequatre(request):
    """
    Cette fonction génère un JSON avec les métadonnées et le contenu encodé en base 64
    d'un fichier GIF ou JPEG ou JPG ou PNG ou PDF passé dans la requête.
    Returns
    -------
    {
        'Précision': '',
        'Type mime': '',
        'Taille en octets': '',
        'Nom de fichier': '',
        'Extension': '',
        'Contenu': ''
    }
    """
    precision = 'Format de fichier où les données sont affichées en base64 !'
    contenu = request.files['monFichier'].read()
    contenu_base_soixantequatre = base64.b64encode(contenu)
    mime_type = request.files['monFichier'].mimetype
    taille = request.headers.get('Content-Length')
    nom_fichier = secure_filename(request.files['monFichier'].filename)
    extension = nom_fichier.split(".")[-1].lower()
    return jsonify(contruire_retour(precision, nom_fichier, extension, \
            mime_type, taille, contenu_base_soixantequatre))

def generer_json_vierge(request):
    """
    Cette fonction génère un JSON avec les métadonnées
    sans le contenu d'un fichier passé dans la requête.
    Returns
    -------
    {
        'Précision': '',
        'Type mime': '',
        'Taille en octets': '',
        'Nom de fichier': '',
        'Extension': '',
        'Contenu': ''
    }
    """
    precision = 'Format de fichier non pris en compte !'
    mime_type = request.files['monFichier'].mimetype
    taille = request.headers.get('Content-Length')
    nom_fichier = secure_filename(request.files['monFichier'].filename)
    extension = nom_fichier.split(".")[-1].lower()
    contenu = ''
    return jsonify(contruire_retour(precision, nom_fichier, extension, mime_type, taille, contenu))
