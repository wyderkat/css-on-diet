###
# Copyright 2014 Tomasz Wyderka <wyderkat@cofoh.com>
#  www.cofoh.com
# Licensed under GPL-v3
##

DIST=cod version LICENSE README.md
VERSION=$(shell cat cod | grep -E '^VERSION *= *".*"' | grep -oE '[0-9\.]+')
VERDIR=cod-$(VERSION)
TARBALL=$(VERDIR).tgz

all: test

$(TARBALL): $(DIST)
	@mkdir $(VERDIR)
	@cp $^ $(VERDIR)
	@tar cfz $@ $(VERDIR)
	@rm -r $(VERDIR)

test: $(TARBALL)
	@cd tests && bash regression $(TARBALL) $(VERDIR)

# make_version has to be first
dist: make_version $(TARBALL)

d: $(TARBALL)

cofoh: $(TARBALL)
	scp $^ Cofoh:cofoh/f/

pub: cofoh


make_version:
	@./wyderkat/versioning.py

.PHONY: clean test dist all make_version cofoh pub
