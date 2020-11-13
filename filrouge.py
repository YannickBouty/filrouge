"""
Script principal fournisseur des services.
"""

import hashlib
from flask import Flask, request, abort, send_from_directory
from werkzeug.exceptions import RequestEntityTooLarge
from flask_swagger_ui import get_swaggerui_blueprint
import controlleurs.controlleurfilrouge

app = Flask(__name__)
#limite la taille des fichiers à 5Mo
app.config["MAX_CONTENT_LENGTH"]=5*1024*1024
#Pour les caractères accentués dans le JSON
app.config['JSON_AS_ASCII'] = False

# nom de l'utilisateur hashé
NOM_UTILISATEUR = '5b250a2d1a504957cf1280f084757a4d4072f2a2cd1101c0fa8a8bb6002cf287'
# mot de passe de l'utilisateur hashé
MOT_DE_PASSE = '8f21ee6dc94c3a780ac0ff891c36b343ae0db7ee5cbf4fb4ac496ade5c4c94f4'

# swagger specification #
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Projet fil rouge, Yannick Bouty"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
# fin swagger specification ###

# pylint: disable=no-else-return

def authorisation_acces():
    """
    Autorise l'accès.
    Parameters
    ----------
    request : flask.request
    Returns
    -------
    boolean
    """
    #récupération de l'utilisateur passé en paramètre du curl
    user = request.authorization
    #hashage du nom et du mot de passe
    nom_utilisateur_hash = hashlib.sha256(user.username.encode()).hexdigest()
    mot_de_passe_hash = hashlib.sha256(user.password.encode()).hexdigest()
    #authorisation ok : retourne True
    return bool(nom_utilisateur_hash==NOM_UTILISATEUR and mot_de_passe_hash==MOT_DE_PASSE)

@app.route('/uploadfile', methods=['POST'])
def upload_file():
    """
    Ce service web permet le dépôt de fichiers
    ['csv','gif','jpeg','jpg','md','pdf','png','txt'].
    Ce service web retourne les métadonnées et
    le contenu du fichier passé dans la requête au format JSON.
    Returns
    -------
    json
    """
    if not authorisation_acces():
        abort(401)
    return controlleurs.controlleurfilrouge.aiguiller(request)

@app.route('/bienvenue')
def bienvenue():
    """
    Page de bienvenue.
    """
    return 'Bienvenue sur le service fil rouge de Yannick !'

@app.errorhandler(401)
@app.errorhandler(404)
@app.errorhandler(413)
@app.errorhandler(500)
@app.errorhandler(RequestEntityTooLarge)
def page_erreur(error):
    """
    Cette fonction retourne le message d'erreur approprié.
    Parameters
    ----------
    error : int
    Returns
    -------
    Une phrase expliquant l'erreur avec le numéro de celle-ci : string
    """
    return 'Vous avez rencontré une erreur {}.\n'.format(error.code), error.code
