setup:
	@pip install -r requirements.txt
	@python manage.py migrate
	@python manage.py loaddata fixture.yaml
