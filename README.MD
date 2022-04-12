Application which takes in image of any size and shrinks it to 140x140 px

Initial cmds
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate

everytime when u want to runserver
python manage.py runserver

endpoint for create record -> http://127.0.0.1:8000/createRecord
endpoint for getting formated image and all records -> http://127.0.0.1:8000/getAllRecords

for testing and upload images to db use postman api service or testcases
