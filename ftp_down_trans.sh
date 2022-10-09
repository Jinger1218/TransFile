#从FTP上下载单文件到本地
#!/bin/sh

sshpass -p 'pwd' scp -r user@ip:/data/prod_server/$1  /home/kaka/Desktop/trans_server

echo "download from ftp successfully"