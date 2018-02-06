#!/bin/bash
#start development server on :8000

export DEBUG=True
export TMDB_API_KEY=YOUR_TMDB_API_KEY

read -n1 -p "Run the app on Docker [D] or pipenv [P]: " choice
case $choice in
  d|D) printf "\nWet to be done...\n";;
  p|P) printf "\nRunning on pipenv...\n "
    pip install -r requirements.txt
    export DATABASE_URL=sqlite:////tmp/snugasabuginacouch-tmp-sqlite.db
    python manage.py collectstatic --noinput
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver ;;
  *) printf "\nChoose [D] for Docker or [P] for pipenv. \n" ;;
esac

