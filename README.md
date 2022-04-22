# chess

# Install wsl
(https://docs.microsoft.com/en-us/windows/wsl/install)

# Install vs code
Install the plugin remote - wsl
(this allows you to use (code .) in terminal to open up vs code through wsl)

# Install django/postgres/dependencies

Step 1: install python (sudo apt-get install python3.8)\
Step 2: install Postgres (sudo apt-get install postgresql-12)\
(https://help.ubuntu.com/community/PostgreSQL\
https://stackoverflow.com/questions/5394331/how-to-set-up-a-postgresql-database-in-django) \
Step 2.5: create database chessdb (createdb chessdb)\
(sudo service postgresql start)\
Step 3: install python3-pip (sudo apt install python3-pip)\
Step 4: install python venv (sudo apt install python3.8-venv)\
Step 4.5: create virtual environment (python3 -m venv env1)\
(from this point on use the venv $ source ~/.venv/env1/bin/activate use deactivate to leave)\
Step 5 install requirements.txt using pip (python -m pip install -r requirements.txt)\
    (dependency list, dont worry about these)\
    Django (pip install Django)\
    psycopg2 package (pip install psycopg2-binary)\
    Daphne (pip install daphne)

# Write tutorial app 1-6
https://docs.djangoproject.com/en/4.0/intro/tutorial01/

# redis?
Do we need redis for django channels?
https://github.com/danidee10/channels_postgres
(docker run -p 6379:6379 -d redis:5)

Changes to setting.py:
1- Change CHANNEL_LAYERS config
2- Add account to apps
3- Change username and password