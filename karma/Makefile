SHELL := /bin/bash

all: last.out

last:
	python `ls -1t *.py | head -1`

last.out:
	make `ls -1t *.py | head -1 | sed 's/.py$$/.out/'`

tags:
	ctags-exuberant -e -R \
	. \
	/usr/lib/python2.7/{collections,multiprocessing,BaseHTTPServer,resource,subprocess,threading,unittest}* \
	/usr/share/pyshared/scapy/ \
	$(VIRTUAL_ENV)/lib/python2.7/site-packages/requests*
	wc -l TAGS

%.src: %.py
	@echo '## source'
	@echo
	@cat $< | sed -e 's/^/    /'

%.out: %.py
	@echo '## source'
	@echo
	@cat $< | sed -e 's/^/    /'
	@echo
	@echo '## output'
	@echo
	@python $< 2>&1 | sed -e 's/^/    /'
