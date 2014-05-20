include dev.mk
include hieroglyph.mak

jslides:
	sphinx-build -qN -b slides -d _build/doctrees \
	-D slide_theme=single-level \
	. _build/slides
	@echo
	@wc -l *.rst

# 	$(SPHINXBUILD) -b slides $(ALLSPHINXOPTS) $(BUILDDIR)/slides

