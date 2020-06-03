import sys,os,chardet
a=os.listdir("C:\\Users\82021\PycharmProjects\pyqt\python笔记")
# print(a)
for i in a:
    if i!="笔记整合.py":
        with open(i,"rb") as file:
            file2=file.read()
            file2=bytes(i+"-"*100+"\n",encoding=chardet.detect(file2).get("encoding"))+file2
            if "GB2312"==chardet.detect(file2).get("encoding"):
                with open("C:\\Users\82021\PycharmProjects\pyqt\笔记GB2312.txt","ab") as file3:
                    file3.write(file2)
            else:
                with open("C:\\Users\82021\PycharmProjects\pyqt\笔记utf-8.txt","ab") as file3:
                    file3.write(file2)
            # # print(i+":"+chardet.detect(file2).get("encoding"))