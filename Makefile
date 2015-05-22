###
# Copyright 2014 Tomasz Wyderka <wyderkat@cofoh.com>
#  www.cofoh.com
# Licensed under GPL-v3
##

DIST=CSSOnDiet/cod.py setup.py LICENSE README.md changelog

VERSION=$(shell cat CSSOnDiet/cod.py | grep -E '^VERSION *= *".*"' | grep -oE '[0-9\.]+')
VERNAME=CSSOnDiet-$(VERSION)
TARBALL=dist/$(VERNAME).tar.gz
SUBLIME_COD_COPY=sublimetext/cod.py

all: $(SUBLIME_COD_COPY) test

dist: $(TARBALL)

test: test2.7 test2.6 test3.2 test3.3 test3.4 
t: test2.7

test%: $(TARBALL)
	@echo "\nExecuting $@\n"
	@cd tests && bash regression $(TARBALL) $(VERNAME) python$(subst test,,$@)


github: 
	@git push github master --tags

cssondiet.com: $(TARBALL)
	cp $^ ~/cssondiet.com/download


$(TARBALL): $(DIST) MANIFEST.in
	python setup.py sdist
pypi: $(DIST)
	python setup.py sdist upload
pypiinfo: 
	python setup.py register
# makes links in the local machine. Root needed
develop: 
	python setup.py develop
install: 
	python setup.py install

sublime: $(SUBLIME_COD_COPY)
	@cd sublimetext; git commit -a && git push github master --tags

$(SUBLIME_COD_COPY): CSSOnDiet/cod.py
	@cp $< $@

guide.html: guide.md
	markdown $< > $@


.PHONY: all dist test t github cssondiet.com pypi pypiinfo develop install sublime 
