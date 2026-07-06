'''
File helps store data perma

File Handling:
is a process of 
1.Creating files
2.reading the files
3.writing files
4.updating files
Using python

Why file handling?
data disappears after the program ends
with files:
1.store data perm
2.data sharing possible
3.reports/logs can be genareted

Types of files ???
Text Files:
1. .txt
2. .csv
3. .py
4. .json
    Binary Files:
    Images
    videos
    pdf's


#opening the files
SYntax:

file = open("Filename","mode")

File mode

mode    Meaning 
r        read
w        Write
a        append
x        create
r+       read+write
W+       write+read
a+       append+read
rb       read binary
wb       write binary

'''
try:  
    file = open
    data = file.read()
    print(data)
    file.close()
except FileNotFoundError as e:
    print("No file found",e)
    
#write mode - W
file = open
file.write("Hello Students")
file.close()



        