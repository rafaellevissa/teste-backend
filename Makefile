migrate:
	export $(xargs < .env)
	@python manage.py migrate

start:
	@python manage.py runserver 0.0.0.0:8000

seeder:
	@for fixture in $(shell ls ./seed); do \
		python manage.py loaddata seed/$$fixture; \
	done
