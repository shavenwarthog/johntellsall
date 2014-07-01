SHELL := /bin/bash

all: last

last:
	python `ls -1t *.py | head -1`

tags:
	ctags-exuberant -e -R \
	. \
	$(VIRTUAL_ENV)/lib/*/site-packages/
	wc -l TAGS
