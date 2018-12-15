import zipfile 
import re 
class docx():
    def __init__(self,file):
        self.__file=file
    def read(self):                 ##self==file
        f=zipfile.ZipFile(self.__file)
        word=f.read("word/document.xml")
        word=re.findall(re.compile("<w:t>.*?</w:t>"),word.decode("utf-8"))
        for i in range(0,len(word)):
            word[i]=word[i].replace("<w:t>","")
            word[i]=word[i].replace("</w:t>","\n")
        return word
