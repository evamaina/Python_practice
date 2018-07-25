import os
def rename_files():
	# get filenames from a folder
	file_list = os.listdir(r"/home/eva/Desktop/prank")
	# print(file_list)
	saved_path = os.getcwd()
	# for each file,rename file name
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)


rename_files()