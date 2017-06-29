# coding = utf-8
from hashlib import md5
import os
import time
import datetime
import shutil

# filename  = r".\2016-08\IMG_20160828_185248.jpg"

allmd5Dict = {}
total_file = 0		# 总共对比的文件总数
total_repeat = 0	# 重复的文件总数
pic_format = ['.jpg','.png','.gif','.jpeg']

def getmd5(filename):
	'''
	获取文件的md5值
	'''
	with open(filename, 'rb') as fd:
		file_txt = fd.read()
		m = md5(file_txt)
		print("%s : %s"%(m, filename))
		return m.hexdigest()

def creatDir(newdir):
	"""
	在当前目录下新建文件夹
	"""
	os.mkdir(newdir)

def handle_repeat_files(file):
	"""
	开始查找重复的文件
	"""
	global total_file
	global total_repeat

	if os.path.isdir(file):
		return
	file_md5 = getmd5(file)			# 获得md5值
	total_file += 1					# 总的文件夹数

	if file_md5  not in allmd5Dict:			
		allmd5Dict[file_md5] = file
	else:
		total_repeat += 1			# 重复的图片数
		if not os.path.exists('../repeat_picture'):
			creatDir('../repeat_picture')
			shutil.move(file, '../repeat_picture')
		else:
			if os.path.exists(file):
				namelist = os.path.splitext(file)		# 把file文件名，如abc.txt分割成['abc','.txt']的形式
				# newname = str(datetime.datetime.now().second).join(namelist)
				newname = 'a'.join(namelist)
				os.rename(file, newname)
				shutil.move(newname, "../repeat_picture")
				return
				
			shutil.move(file, "../repeat_picture")


def main():

	rootpath = input("path: ")
	if rootpath == "":
		"直接回车表示在当前文件夹"
		rootpath = os.getcwd()

	if not os.path.exists(rootpath):	# 判断是否有效的路径
		print('错误的目录路径,请确认路径是否正确！')
		return
	start_time = datetime.datetime.now()
	for item in os.listdir(rootpath):
		if item == 'repeat_picture':						# 防止第二次运行进入repeat_picture文件夹
			continue
		if os.path.splitext(item)[-1] not in pic_format:	# 防止文件夹中有其他类型的文件
			continue
			
		if os.path.isdir(item):								# 如果为文件夹，则进入文件夹
			os.chdir(item)
			for file in os.listdir(os.getcwd()):
				handle_repeat_files(file)
			os.chdir(r"../")
		else:
			handle_repeat_files(item)

	end_time = datetime.datetime.now()
	delta = (end_time - start_time).total_seconds()
	return {"total_file":total_file, "total_repeat":total_repeat, "use_time":delta}


if __name__ == '__main__':

	res = main()
	print("图片处理结束")
	print("总共处理图片：%d"%res['total_file'])
	print("查到重复图片：%d"%res['total_repeat'])
	print("用时： %s s"%res['use_time'])
