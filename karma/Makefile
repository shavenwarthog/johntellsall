SHELL := /bin/bash

all:

tags:
	ctags-exuberant -e -R \
	. /usr/lib/python2.7/{multiprocessing,subprocess,threading}*
	wc -l TAGS

%.out: %.py
	@echo '## source'
	@cat $< | sed -e 's/^/    /'
	@echo
	@echo '## output'
	@echo
	@python $< | sed -e 's/^/    /'
