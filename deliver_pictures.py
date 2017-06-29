#-*-coding:utf8-*-
# author：LinYuelin

import os
import sys
import time
import shutil
import logging

logger = logging.Logger()

# path = r"E:\python_handle_pictures\test_pict"

# 获取当前路径

# picture = r"file.jpg"

imagetype = [".jpg",".png",".jpeg",".bmp"]

def change_to_current_path():
    """
    将工作目录切换到.py文件所在的目录
    :return:
    """
    current_path = os.getcwd()
    os.chdir(current_path)

    
def get_all_pictures(path):
    """
    获取目录下所有的图片
    :param path:
    :return: 返回所有图片文件
    """
    files_list = os.listdir(path)
    for files in files_list:
        if os.path.isdir(files) or os.path.splitext(files)[1] not in imagetype:    # 排除文件夹以及文件类型不属于图片的文件
            files_list.remove(files)
    return files_list
            
def existing_dirs():
    current_path = os.getcwd()
    dirslist = os.listdir(current_path)
    for i in dirslist:
        if not os.path.isdir(i):
            dirslist.remove(i)
    return dirslist
    
    
    

def mkdir_by_modify_date(files_list, dirslist):
    for picture in files_list:
        fileinfos = os.stat(picture)
        mtime = fileinfos.st_mtime
        mdate = time.strftime("%Y-%m",time.localtime(mtime))
        if mdate not in dirslist:
            dirslist.append(mdate)
            os.mkdir(mdate)              # 根据日期创建文件夹
        shutil.move(picture,mdate)       # 移动图片到对应日期的文件夹下
        
    
def main():
    change_to_current_path()
    dirslist = existing_dirs()
    current_path = os.getcwd()
    files_list = get_all_pictures(current_path)
    mkdir_by_modify_date(files_list,dirslist)


        
        
if __name__ == '__main__':
    main()
    
    

