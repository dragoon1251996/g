import json

def read(dir):
    with open(dir,encoding="utf-8") as file:
        return json.load(file)
def save(data,dir):
    with open(dir,"w",encoding="utf-8") as file:
        json.dump(data,file,ensure_ascii=False,indent=4)

data=read("allGrammar_v1.json")

temp=[]
for i in range(len(data)):
    print(data[i]["title"])
    temp.append({str(i):data[i]})
save(temp,"form3.json")