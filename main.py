import os

def split(num):
    for i in range(num):
        print("Enter original filename")
        name=input()
        print("Enter start time")
        start=input()
        print("Enter stop time")
        stop=input()
        print("Enter new name")
        new=input()
        # os.popen('ffmpeg -i '+name+' -ss '+start+' -to '+stop+' -codec copy '+new)
        os.system('ffmpeg -i '+name+' -ss '+start+' -to '+stop+' -codec copy '+new)

def convert(number):
    oldfilename=[]
    newfilename=[]
    for i in range(number):
        print('Enter filename with extention (example.mkv): ',end=' ')
        temp1=input()
        oldfilename.append(temp1)
        print('Enter new filename with extention (example.mp4): ',end=' ')
        temp2=input()
        newfilename.append(temp2)
    print(oldfilename)
    print(newfilename)

def main():
    print('A simple command line tool for ffmpeg')
    print('-------------------------------------')
    print('Options:')
    print('1. Convert files')
    print('2. Split files')
    print('3. Exctact frame of a gif')
    val=input()
    if val is '1':
        convert(2)

main()