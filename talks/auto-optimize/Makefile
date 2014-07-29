SHELL := /bin/bash

# XXXXX HACK: scipy
SETUP_ENV := env PYTHONPATH=/usr/lib/python2.7/dist-packages/


all: last

.PHONY: all.out
all.rst: $(addsuffix .out,$(basename $(wildcard *.py)))
	echo $<

.PHONY: %.rst
%.rst: %.py
	make $(addsuffix .out,$(basename $<))
	../../mkexamples.py $< $(addsuffix .out,$(basename $<)) | tee $@

%.out: %.py
	$(SETUP_ENV) python $< > $@

# %.rst: %.py
# 		../../mkexamples.py $<

.PHONY: simple.rst simple.out
simple.rst: simple.py simple.out
	../../mkexamples.py simple.py simple.out | tee $@

.PHONY: jslides
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

