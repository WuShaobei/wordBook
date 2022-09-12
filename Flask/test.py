
from WordBook import *


# v1 = Vocabulary("1", "b", "c", getNowTime() - 30, 4)
# v2 = Vocabulary("2", "c", "d", getNowTime() - 15, 4)
# v3 = Vocabulary("3", "d", "j", getNowTime() - 7, 3)
# v4 = Vocabulary("4", "e", "k", getNowTime() - 5, 3)
# v5 = Vocabulary("5", "f", "l", getNowTime() - 3, 2)
# v6 = Vocabulary("6", "g", "m", getNowTime() - 2, 2)
# v7 = Vocabulary("7", "h", "i", getNowTime() - 1, 1)
# v8 = Vocabulary("8", "k", "l", getNowTime() , 5)

wb = WorkBook()
print(wb.reviewByDate())


# wb.deleteVocabulary(v1.getWord())
# wb.deleteVocabulary(v2.getWord())
# wb.deleteVocabulary(v3.getWord())
# wb.deleteVocabulary(v4.getWord())
# wb.deleteVocabulary(v5.getWord())
# wb.deleteVocabulary(v6.getWord())
# wb.deleteVocabulary(v7.getWord())
# wb.deleteVocabulary(v8.getWord())

# print(wb.additionVocabulary(v1))
# print(wb.additionVocabulary(v2))
# print(wb.additionVocabulary(v3))
# print(wb.additionVocabulary(v4))
# print(wb.additionVocabulary(v5))
# print(wb.additionVocabulary(v6))
# print(wb.additionVocabulary(v7))
# print(wb.additionVocabulary(v8))

# for _ in range(16):
#     v = wb.reviewByCounts()
#     print(v.toStr())
#     v.setCounts(-1)
#     print(wb.updateVocabulary(v))

# for _ in range(8) :
#     print(wb.reviewByUse().toStr())