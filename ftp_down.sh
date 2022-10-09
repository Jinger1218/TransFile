#从FTP上下载单文件到本地
#!/bin/sh
ftp -v -n ip<<EOF
user user pwd
binary
cd $2
lcd $3
prompt
get $1
bye
EOF
echo "download from ftp successfully"