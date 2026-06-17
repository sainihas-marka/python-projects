import os

folder_path=input("Enter the folder path:")
print("DEBUG:", repr(folder_path))
data=os.listdir(folder_path)


file_types = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",

    ".pdf": "PDFs",

    ".py": "Scripts",

    ".txt": "Text"
}

for file in data:
	result=os.path.splitext(file)

	path=os.path.join(folder_path,file)
	if os.path.isdir(path):
		continue
	elif result[1] in file_types :
		folder=file_types[result[1]]
		path=os.path.join(folder_path,folder)
		os.makedirs(path,exist_ok=True)
		old_path=os.path.join(folder_path,file)
		new_path=os.path.join(path,file)
		os.rename(old_path,new_path)

	else:
		#move the file into file(others)
		path=os.path.join(folder_path,"others")
		os.makedirs(path,exist_ok=True)
		old_path=os.path.join(folder_path,file)
		new_path=os.path.join(path,file)
		os.rename(old_path,new_path)