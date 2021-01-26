#!/bin/bash
export AWS_DEFAULT_PROFILE=csloginstudent
export FLASK_APP=filrouge.py
export FLASK_ENV=development
python3 -m flask run --host=0.0.0.0 -p 55080 --cert=mescertificats/certificat-hello.pem --key=mescertificats/key.pem
