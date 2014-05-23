all:

include dev.mk
include hieroglyph.mak

start:
	./project/project/manage.py runserver

%.html: %.py
	pygmentize -f html $< > $@

jslides:
	sphinx-build -qN -b slides -d _build/doctrees \
	-D slide_theme=single-level \
	. _build/slides
	@echo
	@wc -l *.rst

# 	$(SPHINXBUILD) -b slides $(ALLSPHINXOPTS) $(BUILDDIR)/slides

# TODO: ?? --only-newer 
# NOTE: using 'jta_sync' user, whose homedir is /class/
sync:
	exit 1
	lftp \
	-e 'cd /django-queryset ; mirror -v --reverse -X project --ignore-time --use-cache -X *.pickle -X *.doctree --dry-run' \
	jta

