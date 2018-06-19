# import json
#
# def read(dir):
#     with open(dir,encoding="utf-8") as file:
#         return json.load(file)
# def save(data,dir):
#     with open(dir,"w",encoding="utf-8") as file:
#         json.dump(data,file,ensure_ascii=False,indent=4)
#
# data=read("allGrammar_v1.json")
# save(data,"k.json")


import tinysegmenter
import time
s=tinysegmenter.TinySegmenter()
t=time.time()
print(s.tokenize("バーカッ そんな大金 見せびらかすな!"))
print(s.tokenize("バーカッ そんな大金 見せびらかすな!"))
print(s.tokenize("バーカッ そんな大金 見せびらかすな!"))
print(s.tokenize("バーカッ そんな大金 見せびらかすな!"))
print(s.tokenize("バーカッ そんな大金 見せびらかすな!"))

print(time.time()-t)
t=time.time()

print(s.tokenize(" そんな大金 見せびらかすな!"))
print(s.tokenize(" そんな大金 見せびらかすな!"))
print(s.tokenize(" そんな大金 見せびらかすな!"))
print(s.tokenize(" そんな大金 見せびらかすな!"))
print(s.tokenize(" そんな大金 見せびらかすな!"))

print(time.time()-t)