**FOR WINDOWS**
cd to SHOE ECOM SITE/BASE
python -m venv myvenv
myvenv\scripts\activate
pip install -r requirements.txt
create a .env file within SHOE ECOM SITE/BASE
Run the file BASE\secretKey.py
Copy the output and paste into .env
save all
python manage.py runserver
go to http://127.0.0.1:8000/home/
Navigate around the different pages