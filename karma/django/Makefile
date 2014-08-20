all:

run:
	cd mysite ; python manage.py runserver 

# INSTALL: apt-get install libxml2-dev libxslt1-dev python-dev

tags:
	ctags-exuberant -e -R \
	. \
	$(VIRTUAL_ENV)/lib/*/site-packages/
	wc -l TAGS
