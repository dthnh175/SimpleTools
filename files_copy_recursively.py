# mass copy all files with given extension from all subdir recursively to current root dir
# tested on Windows 10 OS

import glob
import shutil
import os
import argparse
import tqdm

parser = argparse.ArgumentParser(description='mass copy all files in source folder to chosen folder')
parser.add_argument('--ext', dest='extension', default='bin', help='extension of files to be copied')
parser.add_argument('--src', dest='src', default='.', help='path to source folder')
parser.add_argument('--dest', dest='dest', default='.', help='path to dest folder')
parser.add_argument('--clean', dest='doClean', action='store_true', help='delete old sub dirs in src folder')

args = parser.parse_args()
extension = args.extension
src = args.src
dest = args.dest
doClean = args.doClean

# enumerate files and folders
files = glob.glob(src + "/**/*." + extension, recursive=True) # all files paths in the src folder
print("Files counted: " + str(len(files)))
subdirs = [name for name in os.listdir(src) if os.path.isdir(os.path.join(src, name))]
print("Sub dirs counted: " + str(len(subdirs)))

# copy all chosen files to dest folder
print("Copying all files from subdirs recursively to dest folder...")
for file in tqdm.tqdm(files):
    file_name = file.split("\\")[-1]
    shutil.copyfile(file, dest + "\\" + file_name)

# delete old files, folders (optional)
if doClean == True:
    print("Deleting all subdirs in src folder...")
    for subdir in tqdm.tqdm(subdirs):
        shutil.rmtree(src + "\\" + subdir)
