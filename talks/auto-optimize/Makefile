SHELL := /bin/bash

all: last

#         -D slide_theme=single-level
jslides: index.rst
		sphinx-build -qN -b slides -d _build/doctrees \
		. _build/slides
		@echo
		wc -l *.rst

tags:
	ctags-exuberant -e -R \
	. \
	$(VIRTUAL_ENV)/lib/*/site-packages/
	wc -l TAGS

# :::::::::::::::::::::::::::::::::::::::::::::::::: HISTORICAL


# XXXXX HACK: scipy
%.run: %.py
	env PYTHONPATH=/usr/lib/python2.7/dist-packages/ \
	python $<

zoot:
	./optimize.py -o 

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

