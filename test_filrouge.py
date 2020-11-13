import unittest
import io
from requests.auth import _basic_auth_str
from filrouge import app


class TestFilRouge(unittest.TestCase):
    
    def test_mauvaiseUrl(self):
        with app.test_client() as client:
            username = 'francoislaissus'
            password = 'mssio'
            maReponse = client.get('/', \
                    headers={'Authorization': _basic_auth_str(username, password)})
            self.assertEqual(maReponse.status_code, 404)
    def test_bienvenue(self):
        with app.test_client() as client:
            maReponse = client.get('/bienvenue')
            self.assertEqual(maReponse.status_code, 200)

    def test_uploadfile_userOk_fileOk(self):
        with app.test_client() as client:
            username = 'francoislaissus'
            password = 'mssio'
            with open('./fichierstest/data.csv','rb') as fichier:
                fichierIO = io.BytesIO(fichier.read())
            maData = {'monFichier': (fichierIO, 'data.csv')}
            maReponse = client.post('/uploadfile', headers={'Authorization': _basic_auth_str(username, password)}, \
                    data=maData, content_type='multipart/form-data')
            maReponseJson = maReponse.get_json()
            monExtension = maReponseJson['Extension']
            self.assertEqual(monExtension, 'csv')

    def test_uploadfile_userKo_fileOk(self):
        with app.test_client() as client:
            username = 'utilisateur'
            password = 'mdp'
            with open('./fichierstest/data.csv','rb') as fichier:
                fichierIO = io.BytesIO(fichier.read())
            maData = {'monFichier': (fichierIO, 'data.csv')}
            maReponse = client.post('/uploadfile', headers={'Authorization': _basic_auth_str(username, password)}, \
                    data=maData, content_type='multipart/form-data')
            self.assertEqual(maReponse.status_code, 401)
    
    def test_uploadfile_userOk_fileBig(self):
        with app.test_client() as client:
            username = 'francoislaissus'
            password = 'mssio'
            with open('./fichierstest/bigdata.pdf','rb') as fichier:
                fichierIO = io.BytesIO(fichier.read())
            maData = {'monFichier': (fichierIO, 'bigdata.pdf')}
            maReponse = client.post('/uploadfile', headers={'Authorization': _basic_auth_str(username, password)}, \
                    data=maData, content_type='multipart/form-data')
            self.assertEqual(maReponse.status_code, 413)

    def test_uploadfile_userOk_fileEntensionKo(self):
        with app.test_client() as client:
            username = 'francoislaissus'
            password = 'mssio'
            with open('./fichierstest/data.sql','rb') as fichier:
                fichierIO = io.BytesIO(fichier.read())
            maData = {'monFichier': (fichierIO, 'data.sql')}
            maReponse = client.post('/uploadfile', headers={'Authorization': _basic_auth_str(username, password)}, \
                    data=maData, content_type='multipart/form-data')
            self.assertIn(b'Acc\xc3\xa8s autoris\xc3\xa9 mais le fichier ne porte pas une extension autoris\xc3\xa9e !\n', \
                    maReponse.data)
