###
# Copyright 2014 Tomasz Wyderka <wyderkat@cofoh.com>
#  www.cofoh.com
# Licensed under GPL-v3
##

SRC=cod Makefile tests version wyderkat LICENSE

all: test

cod.xz: $(SRC)
	tar cfJ $@ $^

test: cod.xz
	@cd tests && bash regression


# make_version has to be first
dist: make_version cod.xz

make_version:
	@./wyderkat/versioning.py

.PHONY: clean test dist all make_version 
