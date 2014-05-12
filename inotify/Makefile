SHELL := /bin/bash

all:

test:
	python ./vwatch.py /tmp


tags:
	ctags-exuberant -e -R \
	. $(VIRTUAL_ENV)
	wc -l TAGS
