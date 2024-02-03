import os
import shutil

from_dir = "C:/Users/kumar/Downloads"
to_dir = "C:/Users/kumar/Pictures/Saved_Pictures"
to_dir2 = "C:/Users/kumar/Pictures/Docs"
list_of_files = os.listdir(from_dir)
#print(list_of_files)
for file_name in list_of_files:
    name, ext = os.path.splitext(file_name)
    #print(ext)
    if ext == "":
        continue
    if ext in [".xlsx", ".pptx", ".txt", ".docx", ".pdf"]:
        path1 = from_dir + "/" + file_name #this is the source
        path2 = to_dir + "/" + "doc_files"
        path3 = to_dir + "/" + "doc_files" + "/" + file_name
        print(path1)
        print(path3)
        if os.path.exists(path2):
            print("moving the file...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("moving the file...")
            shutil.move(path1, path3)
            

