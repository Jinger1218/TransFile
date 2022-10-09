from itertools import product
import os
import time
import sys
import datetime
 
def main():
    env = sys.argv[1]
    print("环境："+env)
    job_trans()
    while True:
        flag = 0
        now_hour = time.strftime("%H", time.localtime())
        print(now_hour)
        if now_hour >= "12":
            if(env == "pro"):
                if(flag == 0):
                    job_pro()
                    flag = 1
                return
            # else:
            #     if(flag == 0):
            #         job_trans()
            #         flag = 1
            #     return
        if now_hour > "01":
            flag = 0
        print("休眠开始")
        time.sleep(60*60)
        


def job_pro():
    #下载实盘数据到生产环境 20220721A_tar.gz
    print("------------启动pro_job--------------------")
    today=datetime.date.today() 
    da = str(today)[:4]+str(today)[5:7]+str(today)[8:]
    da = da+'A_tar.gz'
    print(da)
    filename = da
    filepath = '/home/kaka/Desktop/shipan_server'
    localpath = '/data/prod_server'
    status = os.system('sh ftp_down.sh '+filename+' '+filepath+' '+localpath)
    print(status)
    # 运行成功返回0
    if(status == 0):
        print("下载数据成功")



def job_trans():
    #在生产环境下载文件到 中转环境 20220721A_tar.gz
    print("------------job_trans--------------------")
    today=datetime.date.today() 
    da = str(today)[:4]+str(today)[5:7]+str(today)[8:]
    da = da+'A_tar.gz'
    print(da)
    filename = da
    status = os.system('sh ftp_down_trans.sh '+filename)
    print(status)
    if(status == 0):
        print("下载数据成功")
    #在中转环境推送数据文件到测试服务器
    up_filename = da
    up_filepath = '/data/test_server'
    up_localpath = '/home/kaka/Desktop/trans_server'
    up_status = os.system('sh ftp_up_trans.sh '+up_filename+' '+up_filepath+' '+up_localpath)
    print(up_status)
    if(status == 0):
        print("上传数据成功")

if __name__ == '__main__':
    main() 