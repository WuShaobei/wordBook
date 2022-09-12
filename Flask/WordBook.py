from Data import *
import heapq

class WorkBook():

    def __init__( self ) :
        self.__use__ = set()
        self.__dic__ = {}
        self.__use__ = set()
        self.__countsHeap__ = []
        self.__dateDic__ = {}
        self.__selectALL__()

    def __getDB__(self):
        return pymysql.connect(
            host = self.__host__, #host属性
            user = self.__user__, #用户名 
            password = self.__password__,  #此处填登录数据库的密码
            db = self.__dbn__ #数据库名
        )

    def additionVocabulary(self, v : Vocabulary) -> bool:
        word = v.getWord()
        db = getDB()
        cursor = db.cursor()

        try:
            cursor.execute(
                'INSERT INTO vocabulary VALUES'\
                + v.toStr()\
            )
            db.commit()
        except:
            db.rollback()
            db.close()
            return False

        date, counts = v.getDates(), v.getCounts()
        self.__use__.add( word )
        self.__dic__[ word ] = v
        heapq.heappush(self.__countsHeap__, (-counts, word))
        
        if date in self.__dateDic__:
            self.__dateDic__[date].add(word)
        else :
            self.__dateDic__[date] = { word } 

        db.close()
        return True

    def deleteVocabulary(self, word:str) -> bool :
        
        db = getDB()
        cursor = db.cursor()

        try:
            cursor.execute ( 
                'DELETE FROM vocabulary WHERE word = "%s"'\
                % ( word )
            )
            db.commit()
        except:
            db.rollback()
            db.close()
            return False

        self.__dic__[word] = None
        db.close()
        return True
    
    def updateVocabulary(self, v:Vocabulary) ->bool :

        db = getDB()
        cursor = db.cursor()
        
        try:
            cursor.execute(
                'UPDATE vocabulary ' + 
                'SET ' + v.getStr() + ' '
                'WHERE word="%s"'%(v.getWord())
            )
            db.commit()
        except:
            db.rollback()
            return False
        
        word, date = v.getWord(), getNowTime()
        self.__use__.add( word )
        if date in self.__dateDic__:
            self.__dateDic__[date].add(word)
        else :
            self.__dateDic__[date] = { word } 
        
        counts = v.getCounts() 
        if counts>=0:
            heapq.heappush(self.__countsHeap__, (-counts, word))
        
        db.close()
        return True

    def selectVocabulary(self, word:str)->Vocabulary:
        db = getDB()
        cursor = db.cursor()

        try:
            cursor.execute(
                'SELECT * FROM vocabulary ' + 
                'WHERE word="%s"'%word
            )
            if result := cursor.fetchone() :
                res = Vocabulary(
                    word = result[0],
                    paraphrase= result[1],
                    roots = result[2],
                    dates = result[3],
                    counts = result[4],   
                )
                db.close()
                res.update()
                self.updateVocabulary(res)
                return res
            else:
                db.close()
                return None
        except:
            db.close()  
            return None
        
    def __selectALL__(self):
        db = getDB()
        cursor = db.cursor()

        cursor.execute(
            'SELECT * FROM vocabulary'
        )
        
        miDate = getNowTime() - 30
        for result in cursor.fetchall() :
            (word, date, counts) = result[0], result[3], result[4]
            
            v = Vocabulary(
                word = result[0],
                paraphrase= result[1],
                roots = result[2],
                dates = result[3],
                counts = result[4],   
            )
            
            self.__dic__[word] = v
            

            if date >= miDate :
                if date in self.__dateDic__:
                    self.__dateDic__[date].add(word)
                else :
                    self.__dateDic__[date] = { word } 

            if counts >= 0 :
                heapq.heappush(self.__countsHeap__, (-counts, word))
        
        db.close()
        
    def reviewByUse(self) -> Vocabulary:
        for word in self.__use__:
            v = self.__dic__[word]
            self.__use__.remove(word)
            return v

    def reviewByDate(self) -> (int, Vocabulary):
        date = getNowTime()

        d = date - 1
        if d in self.__dateDic__:
            for word in self.__dateDic__[d] :
                v = self.__dic__[word]
                self.__dateDic__[d].remove(word)
                return v
                # return (1, v)
            
        d = date - 2
        if d in self.__dateDic__:
            for word in self.__dateDic__[d] :
                v = self.__dic__[word]
                self.__dateDic__[d].remove(word)
                return v
                # return (2, v)

        d = date - 3
        if d in self.__dateDic__:
            for word in self.__dateDic__[d] :
                v = self.__dic__[word]
                self.__dateDic__[d].remove(word)
                return v
                # return (3, v)

        d = date - 5
        if d in self.__dateDic__:
            for word in self.__dateDic__[d] :
                v = self.__dic__[word]
                self.__dateDic__[d].remove(word)
                return v
                # return (5, v)

        d = date - 7
        if d in self.__dateDic__:
            for word in self.__dateDic__[d] :
                v = self.__dic__[word]
                self.__dateDic__[d].remove(word)
                return v
                # return (7, v)

        d = date - 15
        if d in self.__dateDic__:
            for word in self.__dateDic__[d] :
                v = self.__dic__[word]
                self.__dateDic__[d].remove(word)
                return v
                # return (15, v)

        d = date - 30
        if d in self.__dateDic__:
            for word in self.__dateDic__[d] :
                v = self.__dic__[word]
                self.__dateDic__[d].remove(word)
                # return (30, v)
                return v

    def reviewByCounts(self) -> Vocabulary:
        if self.__countsHeap__ :
            word = self.__countsHeap__[0][1]
            heapq.heappop(self.__countsHeap__)
            return self.__dic__[word]