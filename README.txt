Centrale Supelec-MS SIO 2020-YANNICK BOUTY

------------------------------------------
	RECUPERATION PROJET
------------------------------------------
1/Installer git
Exemple sous FreeBSD : sudo pkg install git
2/Dans une console, placer vous dans votre répertoire de travail et récupérer le projet avec la commande :
git clone https://github.com/YannickBouty/filrouge.git

------------------------------------------
	INSTALLATION
------------------------------------------
1/Installer python
Exemple sous FreeBSD : sudo pkg install python
2/Installer pip
Exemple sous FreeBSD : sudo pkg install py37-pip
3/Installer les packages requis
Exemple : pip install -r requirements.txt

------------------------------------------
	LANCEMENT DU SERVEUR
------------------------------------------
Dans une console, lancer le serveur avec la commande :
./lancement-serveur-filrouge.sh

Si le fichier ne s'exécute pas, il faut lui donner les droits d'exécution :
chmod 744 lancement-serveur-filrouge.sh

------------------------------------------
	SWAGGER
------------------------------------------
Dans votre navigateur tapez l'URL : https://0.0.0.0:55080/swagger 

------------------------------------------
	TESTER LES SERVICES
------------------------------------------
Dans une console :
1/Service opérationnel :
Dans votre navigateur tapez l'URL : https://0.0.0.0:55080/bienvenue

2/Test du service d'upload de fichiers :
Les fichiers autorisés sont les ['csv','gif','jpeg','jpg','md','pdf','png','txt'] de taille max d'5Mo.
Une authentification est nécessaire avec : username = francoislaissus et password = mssio

Exemple : curl -ki -X POST -u "francoislaissus:mssio" https://0.0.0.0:55080/uploadfile -F 'monFichier=@./fichierstest/data.csv'

3/Dans le fichier "automatisation-tests-fonctionnels-filrouge.sh", vous trouverez des exemples de tests fonctionnels.
Vous pouvez l'exécuter avec la commande :
./automatisation-tests-fonctionnels-filrouge.sh

Si le fichier ne s'exécute pas, il faut lui donner les droits d'exécution :
chmod 744 automatisation-tests-fonctionnels-filrouge.sh

------------------------------------------
	TESTS UNITAIRES
------------------------------------------
Dans une console à la racine du projet, exécuter la commande :
pytest -sv

------------------------------------------
	CONNAISSANCES MISE EN OEUVRE
------------------------------------------
Langage script et cURL
Langage Python
Installation de packages
Architecture MVC (sans les templates ...)
Tests unitaires
Qualité de code avec pylint (respect de la PEP)
Versionning des sources avec GIT et GITHUB
AWS IAM et CREDENTIALS
AWS EC2
AWS S3
AWS ROUTE 53
AWS ELASTIC IP

------------------------------------------
	AMELIORATIONS
------------------------------------------
Mettre en oeuvre un API MANAGER

