
import pymysql
import time


def getNowTime():
    return time.time() // 86400

def getDB():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='12345678',
        database='wordbook'
    )


class Vocabulary():
    def __init__(self, word, paraphrase, roots, dates:int, counts:int) :
        self.__word__ = word
        self.__paraphrase__ = paraphrase
        self.__roots__ = roots
        self.__dates__ = dates
        self.__counts__ = counts
    
    def toStr(self):
        return '("%s","%s","%s", %d, %d)'\
        %(
            self.__word__,
            self.__paraphrase__,
            self.__roots__,
            self.__dates__,
            self.__counts__
        )
    
    def getStr(self):
        return 'paraphrase="%s",roots="%s",dates=%d,counts=%d'\
        %(
            self.__paraphrase__,
            self.__roots__,
            self.__dates__,
            self.__counts__
        )
    def getWord(self):
        return self.__word__

    
    def update(self, paraphrase="", roots=""):
        if paraphrase : self.__paraphrase__ = paraphrase
        if roots : self.__roots__ = roots
        self.__dates__ = getNowTime()
        self.setCounts(1)
    
    def setCounts(self, d:int):
        self.__counts__ += d

    def getCounts(self):
        return self.__counts__
    def getDates(self):
        return self.__dates__
    def getRoots(self):
        return self.__roots__
    def getParaphrase(self):
        return self.__paraphrase__    