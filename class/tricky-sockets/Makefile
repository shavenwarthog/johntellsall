SHELL := /bin/bash

all: jslides single

%.src: %.py
	python $< > $@

%.out: %.py
	python $< > $@

%.html: %.py
	pygmentize -f html $< > $@

# :::::::::::::::::::::::::::::::::::::::: PUSH

WEB := $(HOME)/src/johntellsall/website/class/tricky-sockets

# copy all but backup files and output files, like '_build'
push:
	-ln -s $(PWD)/_build/slides .
	rsync -sva --copy-links \
	`/bin/ls -1 | egrep -v '[_~]'` $(WEB)/
	@echo
	find $(WEB) -type f

# :::::::::::::::::::::::::::::::::::::::: BUILD

# images -- list images in Markdown format
# Ex: .. image:: _static/large_BaxterCutawayFF3.jpg
.PHONY: images
images:
        /bin/ls -1 _static/*g \
        | awk '{print ".. image::",$$1}'


.PHONY: single
single:
	sphinx-build -b singlehtml -d _build/doctrees \
	. _build/singlehtml

.PHONY: jslides
jslides: index.rst
		sphinx-build -qN -b slides -d _build/doctrees \
		. _build/slides
		@echo
		wc -l *.rst

# ::::::::::::::::::::::::: DEV

# INSTALL: pip install watchdog
automake:
	watchmedo shell-command \
	--pattern='*.rst' --command 'make all'

tags:
	ctags-exuberant -e -R \
	. \
	$(VIRTUAL_ENV)/lib/*/site-packages/
	wc -l TAGS

clean:
	-$(RM) *.gz *.dsc
