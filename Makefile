# Options (TODO)
SHOULD_GZ =
SHOULD_MIN =

# Executables
YUI_FLAGS = --type css
CLOSURE_FLAGS =
VIRTUALENV_FLAGS =
VIRTUALENV_LOC = .ve
DJANGO = python manage.py
FIND = find . -name "$(VIRTUALENV_LOC)" -prune

# CSS
CSS_SRC_EXTS = styl sass scss less
CSS_SRC_FILES = $(shell $(FIND) $(foreach EXT, $(CSS_SRC_EXTS), -or -name "*.$(EXT)"))
CSS_GEN = $(foreach EXT, $(CSS_SRC_EXTS), $(filter %.css, $(CSS_SRC_FILES:.$(EXT)=.css)))
CSS_REG = $(shell $(FIND) -or -name "*.css" -not -name "*.min.css")
CSS_MIN = $(CSS_REG:.css=.min.css) $(CSS_GEN:.css=.min.css)
CSS_TARGETS = $(CSS_GEN) $(CSS_MIN) $(CSS_MIN:.css=.css.gz)

# Javascript
JS_SRC_EXTS = coffee
JS_SRC_FILES = $(shell $(FIND) $(foreach EXT, $(JS_SRC_EXTS), -or -name "*.$(EXT)"))
JS_GEN = $(foreach EXT, $(JS_SRC_EXTS), $(filter %.js, $(JS_SRC_FILES:.$(EXT)=.js)))
JS_REG = $(shell $(FIND) -or -name "*.js" -not -name "*.min.js")
JS_MIN = $(JS_REG:.js=.min.js) $(JS_GEN:.js=.min.js)
JS_TARGETS = $(JS_GEN) $(JS_MIN) $(JS_MIN:.js=.js.gz)

all: clean build

build: assets $(VIRTUALENV_LOC)

assets: css js

css: $(CSS_TARGETS)

js: $(JS_TARGETS)

%.css: %.styl
	stylus --use nib < $< > $@

%.css: %.sass
	sass --compass $< > $@

%.css: %.scss
	sass --compass $< > $@

%.css: %.less
	lessc $< > $@

%.min.css: %.css
	java -jar ./bin/yuicompressor-2.4.7.jar $(YUI_FLAGS) <$< | sed 's/ and(/ and (/g' >$@

%.js: %.coffee
	coffee -cp $< > $@

%.min.js: %.js
	java -jar ./bin/compiler.jar $(CLOSURE_FLAGS) --js=$< >$@

%.gz: %
	gzip -9 <$< >$@

$(VIRTUALENV_LOC):
	./bin/virtualenv.py $(VIRTUALENV_LOC) $(VIRTUALENV_FLAGS)
	$(VIRTUALENV_LOC)/bin/pip install -r requirements/prod.txt

clean:
	rm -Rf $(CSS_TARGETS) $(JS_TARGETS) $(VIRTUALENV_LOC)

run:
	@$(DJANGO) runserver_plus

shell:
	@$(DJANGO) shell_plus

test:
	@echo "Implement this yourself"

docs:
	@echo "Implement this yourself"

fixture:
	@$(DJANGO) dumpdata $(APP_NAME) --indent=2 --natural > fixtures/$(APP_NAME).json

.PHONY: fixture clean
