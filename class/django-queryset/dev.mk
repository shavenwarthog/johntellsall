all:

tags:
	ctags-exuberant -e -R --languages=python \
	*.py $(VIRTUAL_ENV)/lib/python*/*/django
	wc -l TAGS
