#!/bin/bash
#Début tests
echo '------------------------------------------------------------------------'
echo 'DEBUT TESTS'
echo '------------------------------------------------------------------------'
echo 'TESTS UPLOAD'
echo '------------------------------------------------------------------------'
#Test : user ok, fichier existant et extension ok
curl -ki -X POST -u "francoislaissus:mssio" https://0.0.0.0:55080/uploadfile -F 'monFichier=@./fichierstest/data.csv'
curl -ki -X POST -u "francoislaissus:mssio" https://0.0.0.0:55080/uploadfile -F 'monFichier=@./fichierstest/data.gif'
curl -ki -X POST -u "francoislaissus:mssio" https://0.0.0.0:55080/uploadfile -F 'monFichier=@./fichierstest/data.jpeg'
curl -ki -X POST -u "francoislaissus:mssio" https://0.0.0.0:55080/uploadfile -F 'monFichier=@./fichierstest/data.jpg'
curl -ki -X POST -u "francoislaissus:mssio" https://0.0.0.0:55080/uploadfile -F 'monFichier=@./fichierstest/data.md'
curl -ki -X POST -u "francoislaissus:mssio" https://0.0.0.0:55080/uploadfile -F 'monFichier=@./fichierstest/data.pdf'
curl -ki -X POST -u "francoislaissus:mssio" https://0.0.0.0:55080/uploadfile -F 'monFichier=@./fichierstest/data.png'
curl -ki -X POST -u "francoislaissus:mssio" https://0.0.0.0:55080/uploadfile -F 'monFichier=@./fichierstest/data.txt'
echo '------------------------------------------------------------------------'
#Test : user ok, fichier existant et extension ok en majuscule
curl -ki -X POST -u "francoislaissus:mssio" https://0.0.0.0:55080/uploadfile -F 'monFichier=@./fichierstest/data.CSV'
curl -ki -X POST -u "francoislaissus:mssio" https://0.0.0.0:55080/uploadfile -F 'monFichier=@./fichierstest/data.GIF'
echo '------------------------------------------------------------------------'
#Test : user ok, fichier > 5Mo et extension ok
curl -ki -X POST -u "francoislaissus:mssio" https://0.0.0.0:55080/uploadfile -F 'monFichier=@./fichierstest/bigdata.pdf'
echo '------------------------------------------------------------------------'
#Test : user ko, fichier existant et extension ok
curl -ki -X POST -u "user:pwd" https://0.0.0.0:55080/uploadfile -F 'monFichier=@./fichierstest/data.txt'
echo '------------------------------------------------------------------------'
#Test : user ok, fichier existant et extension ko
curl -ki -X POST -u "francoislaissus:mssio" https://0.0.0.0:55080/uploadfile -F 'monFichier=@./fichierstest/data.sql'
echo '------------------------------------------------------------------------'
#Test : user ok, fichier non existant et extension quelconque
curl -ki -X POST -u "francoislaissus:mssio" https://0.0.0.0:55080/uploadfile -F 'monFichier=@./fichierstest/data.doc'
echo '------------------------------------------------------------------------'
#Test : user ok, fichier non écrit dans la requête et extension quelconque
curl -ki -X POST -u "francoislaissus:mssio" https://0.0.0.0:55080/uploadfile -F 'monFichier=@'
echo '------------------------------------------------------------------------'
echo 'FIN TESTS'
echo '------------------------------------------------------------------------'

