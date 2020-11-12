#!/bin/bash
export FLASK_APP=filrouge.py
export FLASK_ENV=development
flask run --host=0.0.0.0 -p 8000 --cert=mescertificats/certificat-hello.pem --key=mescertificats/key.pem
