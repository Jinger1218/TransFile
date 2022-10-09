#从本地向FTP上传单个文档
#!/bin/sh
sshpass -p 'pwd' scp $3/$1  user@ip:$2/$1
echo "commit to ftp successfully"