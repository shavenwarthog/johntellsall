#!/bin/bash

# https://github.com/feralhosting/feralfilehosting/tree/master/Feral%20Wiki/SFTP%20and%20FTP/LFTP%20-%20Automated%20sync%20from%20seedbox%20to%20home
	lftp jta <<EOF
set cmd:parallel 1
cd /
mirror -v --reverse --only-newer -X project --ignore-time --use-cache -X *.pickle -X *.doctree
EOF

