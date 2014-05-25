###
# Copyright 2014 Tomasz Wyderka <wyderkat@cofoh.com>
#  www.cofoh.com
# Licensed under GPL-v3
##

DIST=cod version LICENSE README.md Changes
VERSION=$(shell cat cod | grep -E '^VERSION *= *".*"' | grep -oE '[0-9\.]+')
VERDIR=cod-$(VERSION)
TARBALL=$(VERDIR).tgz
SUBLIME_COD_COPY=sublimetext/cod.py

all: $(SUBLIME_COD_COPY) test

$(SUBLIME_COD_COPY): cod
	cp $< $@

$(TARBALL): $(DIST)
	@mkdir $(VERDIR)
	@cp $^ $(VERDIR)
	@tar cfz $@ $(VERDIR)
	@rm -r $(VERDIR)

test: test2.7 test3.3

test%: $(TARBALL)
	@echo "\nExecuting $@\n"
	@cd tests && bash regression $(TARBALL) $(VERDIR) python$(subst test,,$@)


# make_version has to be first
dist: make_version $(TARBALL)

d: $(TARBALL)

cofoh: $(TARBALL)
	scp $^ Cofoh:cofoh/f/

pub: cofoh


make_version:
	@./wyderkat/versioning.py

.PHONY: clean test dist all make_version cofoh pub
