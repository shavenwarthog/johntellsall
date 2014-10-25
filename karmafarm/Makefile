all: test

test:
	./dsearch.py

tags:
	ctags-exuberant --languages=python -e -R \
	. $(VIRTUAL_ENV)/lib/*/site*/*stackexchange*
