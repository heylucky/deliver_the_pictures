#-*-coding:utf8-*-
import os
import sys
import time
import shutil


# path = r"E:\python_handle_pictures\test_pict"

# 获取当前路径

# picture = r"file.jpg"


def change_to_current_path():
    current_path = os.getcwd()
    os.chdir(current_path)

    
def get_all_pictures(path):
    files_list = os.listdir(path)
    for files in files_list:
        if os.path.isdir(files):    # 排除文件夹
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
    
    

