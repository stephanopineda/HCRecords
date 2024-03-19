1. open this folder on vscode
2. select a .py file
3. change selected interpreter on the bottom bar
4. create a virtual enviroment using the latest python version
5. a .venv folder should be added to the folder
6. run the following commands:
pip install django
pip install djangorestframework
pip install django-cors-headers
pip install pillow      

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

