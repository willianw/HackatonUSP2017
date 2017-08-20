run:
	python manage.py makemigrations
	python manage.py migrate 
	python manage.py runserver

restart-database:
	mongo database-hackaton restart-database.js

install:
	sudo apt-get install -y mongodb python-pip
	pip install Django
	pip install pymongo
	mongo << EOT
	use database-hackaton
	db.createCollection("professores")
	EOT
