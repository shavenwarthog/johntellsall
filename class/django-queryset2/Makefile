all: jslides

last.out:
	make `ls -1t *.py | head -1 | sed -e s/.py/.out/`

.PHONY: fp-examples.rst
fp-examples.rst:
	echo < /dev/null > $@
	make --no-print-directory parse1.rst >> $@
	@cat $@

%.rst: %.py
	@echo $<
	@echo ----------------
	@echo
	@echo '.. code-block: python'
	@echo
	@awk '{print "    "$$0}' $<
	@echo
	@echo ::
	@echo
	@python $< recipe.ini | awk '{print "    "$$0}'

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
