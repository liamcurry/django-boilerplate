virtualenv = virtualenv
activate = source $(virtualenv)/bin/activate

all: build

build:
	virtualenv --no-site-packages $(virtualenv)
	$(activate); \
		pip install -r requirements.txt; \
		python manage.py collectstatic
	npm install

install: build
	$(activate); python manage.py syncdb

install_dev: install
	$(activate); pip install -r requirements_dev.txt
	mv project_name/settings.{py.example,py}

clean:
	rm -Rf $(virtualenv) node_modules public_cache/* public/*
	find . -name "*.pyc" -or -name "*.db" -delete

run:
	$(activate); python manage.py runserver_plus

shell:
	$(activate); python manage.py shell_plus

.PHONY: run shell
