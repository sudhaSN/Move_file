import os
import shutil

from_dir = "Downloads"
to_dir = "C:/Users/sudha/OneDrive/Documents/Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for x in list_of_files:
    os.path.splitext(x)
