import zipfile 
import re 
from __important__ import *
class docx():
    def __init__(self,file,mode):
        self.__file=file
    def read(self):                 ##self==file
        f=zipfile.ZipFile(self.__file)
        word=f.read("word/document.xml")
        word=re.findall(re.compile("<w:t>.*?</w:t>"),word.decode("utf-8"))
        if self.__mode=='w':			##only read words
                word=re.findall(re.compile("<w:t>.*?</w:t>"),word.decode("utf-8"))
                for i in range(0,len(word)):
                    word[i]=word[i].replace("<w:t>","")
                    word[i]=word[i].replace("</w:t>","\n")
                return word
        if self.__mode=='p':				##only read pictures
                f=zipfile.ZipFile(self.__file)
                filelist=str(f.filelist)
                filename=re.findall("word/media/image1.*?'",filelist)
                pictures=f.read(filename[0].replace("'",""))
                return pictures
        
