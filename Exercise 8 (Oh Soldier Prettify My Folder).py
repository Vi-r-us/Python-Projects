'''
Problem Statement:
The task you have to perform is” Oh Soldier Prettify my Folder.”

Suppose you have a folder, and its path is also given. You have to create a function which takes
three input arguments, which are:

def soldier("C://", "harry.txt", "jpg")

-Full Path of the folder as input strings.
-Dictionary file
-File Format

The function will perform three tasks:

-First, it will check all the files present in the folder whose paths are given as an input
 argument.
-Then it will capitalize the first letter of each file. If the name of the file is present in
 a dictionary file then it will not capitalize the first letter. It will only capitalize the
 first letter of the files, which are not present in the dictionary file.
-The function renames the file names to number in range of 1 to100 whose format is the same as
 mentioned in the input parameter like 1.jpg.

After performing these tasks, your folder will prettify as all the first letters of the files
in the folder will be capitalize except for those files whose names are present in the dictionary
file. And the files having the same format as given in the input argument will rename to number
in the range of 1-100.
'''

import os

def soldier(directory , file_name , file_format):
    if os.path.isdir(directory)==True:
        os.chdir(directory)
        i=1
        for file in os.listdir():
            if file_name == file:
                continue
            elif file.endswith(file_format):
                os.rename(file , f"{i}{file_format}")
                i+=1
            else:
                os.rename(file , file.capitalize())
    else:
        print("The Directory you are looking for dosen't exist")

if __name__ == '__main__':
    d = input("Enter the name of the directory:\t")
    fn = input("Enter File Name:\t")
    ff = input("Enter the format of the File:\t")
    print(os.listdir(d))
    soldier(d,fn,ff)
