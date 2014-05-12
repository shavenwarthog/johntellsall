# XX: for root:
PWD := $(shell pwd)
NGINX := /usr/local/nginx/sbin/nginx

all:

ARGS = -c $(PWD)/nginx_dlna.conf -p $(PWD) 

test:
	$(NGINX) -t $(ARGS)

run:
	$(NGINX) $(ARGS)

tags:
	ctags-exuberant -e -R \
	.
	wc -l TAGS
