run:
	python manage.py migrate
	python manage.py runserver

restart-database:
	mongo database-hackaton restart-database.js

install:
	sudo apt-get install mongodb python-pip
	pip install Django
	mongo << EOT
	use database-hackaton
	db.createCollection("professores")
	EOT
