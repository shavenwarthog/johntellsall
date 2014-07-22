SHELL := /bin/bash

all: last

.PHONY: x.dat
x.dat:
	python ./optimize.py

.PHONY: static.html
static.html: static_example.py
	python $< > $@

best: optimize.dat
	sort -r -k 2n $< | head

last:
	python `ls -1t *.py | head -1`

optimize.dat: optimize.py
	./$<

.PHONY: optimize.png
optimize.png: optimize.gp optimize.dat
	gnuplot optimize.gp
	eog $@

tags:
	ctags-exuberant -e -R \
	. \
	$(VIRTUAL_ENV)/lib/*/site-packages/
	wc -l TAGS
