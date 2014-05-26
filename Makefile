###
# Copyright 2014 Tomasz Wyderka <wyderkat@cofoh.com>
#  www.cofoh.com
# Licensed under GPL-v3
##

DIST=CSSOnDiet/cod.py setup.py LICENSE README.md Changes

VERSION=$(shell cat cod | grep -E '^VERSION *= *".*"' | grep -oE '[0-9\.]+')
VERNAME=CSSOnDiet-$(VERSION)
TARBALL=dist/$(VERNAME).tar.gz
SUBLIME_COD_COPY=sublimetext/cod.py

all: $(SUBLIME_COD_COPY) test

$(TARBALL): $(DIST)
	@python setup.py sdist >/dev/null
dist: $(TARBALL)

d: $(TARBALL)


test: test2.7 test3.3

test%: $(TARBALL)
	@echo "\nExecuting $@\n"
	@cd tests && bash regression $(TARBALL) $(VERNAME) python$(subst test,,$@)


pub: 
	@git push github master --tags
cofoh: $(TARBALL)
	scp $^ Cofoh:cofoh/f/
pypi: $(DIST)
	python setup.py sdist upload
pypiinfo: 
	python setup.py register
sublime: $(SUBLIME_COD_COPY)
	@cd sublimetext; git commit && git push github master --tags

$(SUBLIME_COD_COPY): CSSOnDiet/cod.py
	@cp $< $@



.PHONY: clean test dist d all cofoh pypi pypiinfo sublime pub
