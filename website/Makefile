all:

# NOTE: 'jta_sync' user homedir is /
# TODO: use -c vs -e so will return?
sync:
	lftp \
	-e 'cd / ; mirror -v --reverse --only-newer -X project --ignore-time --use-cache -X *.pickle -X *.doctree ' \
	jta
