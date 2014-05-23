SHELL := /bin/bash
include ../dev.mk

all:

tags:
	ctags-exuberant -e -R \
	. /usr/lib/python2.7/dist-packages/pip
	wc -l TAGS
