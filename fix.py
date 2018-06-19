import json

def read(dir):
    with open(dir,encoding="utf-8") as file:
        return json.load(file)
def save(data,dir):
    with open(dir,"w",encoding="utf-8") as file:
        json.dump(data,file,ensure_ascii=False,indent=4)

data=read("form.json")
print(data)
save(data,"Form4.json")