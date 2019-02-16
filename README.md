# django-admin-example
Examples of what can be done with django admin

If you want to set the project up:

    $ mkdir working_dir
    $ cd working_dir
    $ virtualenv -p python3 env
    $ source env/bin/activate
    $ git clone https://github.com/pythoniste/django-admin-example
    $ cd django-admin-example/
    $ pip install --upgrade -r requirements.txt
    $ cd example
    $ ./manage.py migrate
    $ ./manage.py loaddata initial_data
    $ ./manage.py runserver

Ces commandes permettant de :

    - créer un répertoire de travail qui contiendra:
        - un environnement Python virtuel
        - le projet
    - installer toutes les dépendances nécessaires
    - créer la base de données
    - peupler la base de données avec des informations basiques

On a ainsi un utilisateur admin (mot de passe: adminadmin) et ce qu'il faut pour saisir des objets de type "Test"

Vous pouvez ainsi ouvrir un serveur sur localhost:8000/admin, vous connecter et commencer à regarder l'interface admin et comparer ce que vous voyez avec le code du projet.
