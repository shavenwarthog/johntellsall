all: jslides

# push:
# 	rsync -av ../class/django-queryset2 class/ && make sync

count:
	./mkindex.py index.rst

%.rst: %.py
	./mkexamples.py $<

last.out:
	make `ls -1t *.py | head -1 | sed -e s/.py/.out/`

.PHONY: fp-examples.rst
fp-examples.rst:
	./mkexamples.py parse?.py > $@

oindex:
	./mkindex.py ../django-queryset/index.rst

jslides: fp-examples.rst
	sphinx-build -qN -b slides -d _build/doctrees \
	-D slide_theme=single-level \
	. _build/slides
	@echo
	wc -l *.rst


tags:
	ctags-exuberant -e -R --languages=python \
	. $(VIRTUAL_ENV)/lib/python*/*/django
	wc -l TAGS
