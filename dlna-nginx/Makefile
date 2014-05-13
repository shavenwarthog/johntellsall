# XX: for root:
PWD := $(shell pwd)
NGINX := /usr/local/nginx/sbin/nginx

all:

ARGS = -c $(PWD)/nginx_dlna.conf -p $(PWD) 

test:
	$(NGINX) -t $(ARGS)

run:
	-fuser -k 9000/tcp
	$(NGINX) $(ARGS)
	tail -f logs/error.log

reload:
	$(NGINX) $(ARGS) -s reload


# :::::::::::::::::::::::::::::::::::::::::::::::::: DEV


tags:
	ctags-exuberant -e -R \
	.
	wc -l TAGS
