# CSS
STYL = $(shell find . -name "*.styl")
SASS = $(shell find . -name "*.sass")
SCSS = $(shell find . -name "*.scss")
LESS = $(shell find . -name "*.less")
GENERATED_CSS = $(STYL:.styl=.css) $(SASS:.sass=.css) $(LESS:.less=.css) $(SCSS:.scss=.css)
PLAIN_CSS = $(shell find . -name "*.css" -not -name "*.min.css")
CSS = $(PLAIN_CSS) $(GENERATED_CSS)
CSS_MIN = $(CSS:.css=.min.css)
CSS_MIN_GZ = $(CSS_MIN:.css=.css.gz)

# Javascript
COFFEE = $(shell find . -name "*.coffee")
GENERATED_JS = $(COFFEE:.coffee=.js)
PLAIN_JS = $(shell find . -name "*.js" -not -name "*.min.js")
JS = $(PLAIN_JS) $(GENERATED_JS)
JS_MIN = $(JS:.js=.min.js)
JS_MIN_GZ = $(JS_MIN:.js=.js.gz)

# Executables
YUI = java -jar ./bin/yuicompressor-2.4.7.jar
YUI_FLAGS = --type css
CLOSURE = java -jar ./bin/compiler.jar
CLOSURE_FLAGS =
VIRTUALENV = ./bin/virtualenv.py
VIRTUALENV_FLAGS = --no-site-packages
VIRTUALENV_LOC = .ve
DJANGO = python manage.py

CLEANUP = $(shell find . -name '*.pyc' -or -name '.sass-cache' -or -name '.DS_Store')

all: $(CSS) $(CSS_MIN) $(CSS_MIN_GZ) $(JS) $(JS_MIN) $(JS_MIN_GZ)

%.css: %.styl
	stylus < $< > $@

%.css: %.sass
	sass --compass $< > $@

%.css: %.scss
	sass --compass $< > $@

%.css: %.less
	lessc $< > $@

%.min.css: %.css
	$(YUI) $(YUI_FLAGS) <$< | sed 's/ and(/ and (/g' >$@

%.js: %.coffee
	coffee -cp $< > $@

%.min.js: %.js
	$(CLOSURE) $(CLOSURE_FLAGS) --js=$< >$@

%.gz: %
	gzip -9 <$< >$@

clean:
	rm -Rf $(GENERATED_CSS) $(CSS_MIN) $(CSS_MIN_GZ) $(GENERATED_JS) $(JS_MIN) $(JS_MIN_GZ) $(CLEANUP)

# Helpers
# -------

.PHONY: run reset create_ve create_fixture shell

run:
	@$(DJANGO) runserver_plus

reset:
	@rm -f .dev.db
	@$(DJANGO) syncdb --noinput
	@$(DJANGO) loaddata fixtures/*.json

shell:
	@$(DJANGO) shell_plus

create_ve:
	@$(VIRTUALENV) $(VIRTUALENV_LOC) $(VIRTUALENV_FLAGS)

create_fixture:
	@$(DJANGO) dumpdata $(APP_NAME) --indent=2 --natural > fixtures/$(APP_NAME).json
