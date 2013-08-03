APPNAME = {{ project_name }}
DEST = `pwd`
STATIC_ROOT = $(APPNAME)/static
PUBLIC_ROOT = public
MEDIA_ROOT = public_media
STYLUS = node node_modules/.bin/stylus
UGLIFYJS = node node_modules/.bin/uglifyjs
YUICOMPRESSOR = yuicompressor
VE = python bin/virtualenv.py
VE_LOC = venv
ACTIVATE = source $(VE_LOC)/bin/activate
REQS = requirements.txt
MANAGE = $(ACTIVATE); python manage.py
NGINX = /usr/local/nginx/sbin/nginx
UWSGI = $(VE_LOC)/bin/uwsgi
ENV = prod
R_JS = node node_modules/.bin/r.js
FIND = find . -name "$(VE_LOC)" -prune -or
RELOAD_NGINX = $(shell $(FIND) -name "*.py" -or -name "config/nginx/*")
RELOAD_UWSGI = $(shell $(FIND) -name "*.html")

all: clean build
build: build_ve build_reqs build_settings build_static build_db
build_css: main.min.css
build_css_gz: main.min.css.gz
build_js: main.min.js
build_js_gz: main.min.js.gz
build_ve: $(VE_LOC)
clean: clean_pyc clean_osx clean_ve clean_static clean_settings
restart_web: restart_uwsgi restart_nginx
restart_cron: restart_celery
restart_db: restart_postgresql
start_web: start_uwsgi start_nginx
start_cron: start_celery
start_db: start_postgresql
stop_web: stop_uwsgi stop_nginx
stop_cron: stop_celery
stop_db: stop_postgresql

build_ve:
	$(VE) $(VE_LOC) --no-site-packages

clean_ve:
	rm -Rf $(VE_LOC)

build_settings:
	ln -s $(ENV).py $(DEST)/$(APPNAME)/settings/active.py

clean_settings:
	rm $(APPNAME)/settings/active.py

build_reqs:
	$(ACTIVATE); pip install -r $(REQS)

clean_reqs:
	$(ACTIVATE); pip uninstall -r $(REQS)

reset_reqs: clean_reqs build_reqs

build_db:
	$(ACTIVATE); \
		$(MANAGE) syncdb --noinput; \
		$(MANAGE) migrate

clean_db:
	echo 'todo'

reset_db:
	$(MANAGE) reset_db --router=default
	$(MANAGE) syncdb --noinput
	$(MANAGE) migrate

build_static: build_css build_js
	$(ACTIVATE); $(MANAGE) collectstatic

clean_static:
	rm -Rf $(PUBLIC_ROOT) $(MEDIA_ROOT)

reset_static: clean_static build_static

clean_os:
	find . -name ".DS_Store" -delete

clean_pyc:
	find . -name "*.pyc" -delete

clean_thumbnails:
	rm -Rf $(MEDIA_ROOT)/cache/*
	$(ACTIVATE); $(MANAGE) thumbnail clear

run:
	$(ACTIVATE); $(MANAGE) runserver_plus

shell:
	$(ACTIVATE); $(MANAGE) shell_plus

watch:
	$(ACTIVATE); watchmedo tricks tricks.yml

start_postgres:
	pg_ctl -D /usr/local/var/postgres -l logs/postgresql.log start -m fast

stop_postgres:
	pg_ctl -D /usr/local/var/postgres -l logs/postgresql.log stop -m fast

restart_postgres:
	pg_ctl -D /usr/local/var/postgres -l logs/postgresql.log restart -m fast

start_celery:
	sudo /etc/init.d/celeryd start
	sudo /etc/init.d/celerybeat start

stop_celery:
	sudo /etc/init.d/celeryd start
	sudo /etc/init.d/celerybeat start

restart_celery:
	sudo /etc/init.d/celeryd restart
	sudo /etc/init.d/celerybeat restart

start_nginx:
	$(NGINX) -c $(DEST)/config/nginx/nginx.conf

stop_nginx:
	$(NGINX) -c $(DEST)/config/nginx/nginx.conf -s stop

restart_nginx:
	$(NGINX) -c $(DEST)/config/nginx/nginx.conf -s reload

start_uwsgi:
	$(UWSGI) --ini config/uwsgi.ini

stop_uwsgi:
	$(UWSGI) --ini config/uwsgi.ini --stop pids/uwsgi.pid

restart_uwsgi:
	$(UWSGI) --ini config/uwsgi.ini --reload pids/uwsgi.pid

%.min.css: $(STATIC_ROOT)/styl/%.styl
	$(STYLUS) -u nib -I $(STATIC_ROOT)/css -c --include-css \
								-I $(STATIC_ROOT)/styl < $< | \
	$(YUICOMPRESSOR) --type css > $(STATIC_ROOT)/build/$@

%.min.css.gz: $(STATIC_ROOT)/styl/%.styl
	$(STYLUS) -u nib -I $(STATIC_ROOT)/css -c --include-css \
								-I $(STATIC_ROOT)/styl < $< | \
	$(YUICOMPRESSOR) --type css | \
	gzip -9c > $(STATIC_ROOT)/build/$@

%.min.js: $(STATIC_ROOT)/js/%.js
	$(R_JS) -o $(STATIC_ROOT)/js/build.js out=$(STATIC_ROOT)/build/$@

%.min.js.gz: $(STATIC_ROOT)/js/%.js
	$(R_JS) -o $(STATIC_ROOT)/js/build.js out=$(STATIC_ROOT)/build/$@
	gzip -9c < $(STATIC_ROOT)/build/$@ > $(STATIC_ROOT)/build/$@


.PHONY: run shell reset_db servers_start servers_reload servers_stop debug
