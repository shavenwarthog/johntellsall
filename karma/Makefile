SHELL := /bin/bash

all: last

last:
	python `ls -1t *.py | head -1`

last.out:
	make `ls -1t *.py | head -1 | sed 's/.py$$/.out/'`

tags:
	ctags-exuberant -e -R \
	. /usr/lib/python2.7/{multiprocessing,subprocess,threading,unittest}*
	wc -l TAGS

%.out: %.py
	@echo '## source'
	@echo
	@cat $< | sed -e 's/^/    /'
	@echo
	@echo '## output'
	@echo
	@python $< | sed -e 's/^/    /'
