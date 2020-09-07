import os

def split(number):
    newFileName=[]
    startTime=[]
    stopTime=[]
    print('Enter filename with extention (example.mkv or E:\\example.mkv): ',end=' ')
    mainfile=input()
    for i in range(number):
        print('Enter new filename with extention (example.mp4 or E:\\example.mp4): ',end=' ')
        temp1=input()
        newFileName.append(temp1)
        print('Enter start time of new clip (HH:MM:SS): ',end=' ')
        temp2=input()
        startTime.append(temp2)
        print('Enter end time of new clip (HH:MM:SS): ',end=' ')
        temp3=input()
        stopTime.append(temp3)
    
    for i in range(number):
        os.system('ffmpeg -i '+mainfile+' -ss '+startTime[i]+' -to '+stopTime[i]+' -codec copy '+newFileName[i])

def convert(number):
    oldfilename=[]
    newfilename=[]
    for i in range(number):
        print('Enter filename with extention (example.mkv or E:\\example.mkv): ',end=' ')
        temp1=input()
        oldfilename.append(temp1)
        print('Enter new filename with extention (example.mp4 or E:\\example.mp4): ',end=' ')
        temp2=input()
        newfilename.append(temp2)
    for i in range(number):
        os.system('ffmpeg -i '+oldfilename[i]+' -codec copy '+newfilename[i])

def extract(number):
    fileName=[]
    frameName=[]
    print('Enter extention of frames (.jpg / .png): ',end=' ')
    format=input()
    for i in range(number):
        print('Enter filename with extention (example.gif or E:\\example.gif): ',end=' ')
        temp1=input()
        fileName.append(temp1)
        print('Enter frames name (img or image): ',end=' ')
        temp2=input()
        frameName.append(temp2)
    for i in range(number):
        os.system('ffmpeg -i '+fileName[i]+' '+frameName[i]+'%d'+format)

def main():
    print('A simple command line tool for ffmpeg')
    print('-------------------------------------')
    print('Options:')
    print('1. Convert files')
    print('2. Split files')
    print('3. Exctact frames of a gif')
    
    print('Enter option number : ',end=' ')
    val=input()
    if val is '1':
        print('Numbers of file for conversion: ',end=' ')
        num=int(input())
        convert(num)
    elif val is '2':
        print('Numbers of new clip: ',end=' ')
        num=int(input())
        split(num)
    elif val is '3':
        print('Numbers of gif file for extraction: ',end=' ')
        num=int(input())
        extract(num)

main()