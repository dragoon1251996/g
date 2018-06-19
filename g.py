import requests

# def request(str):
#     req=requests.request("POST",)


import urllib
# print(urllib.parse.quote_plus('一年の中でいつが一番涼しいですか'))




import requests

url = "http://www.atilika.org/kuromoji/rest/tokenizer/tokenize"

headers = {
    'accept': "*/*",
    'accept-encoding': "gzip, deflate",
    'accept-language': "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    'connection': "keep-alive",
    'content-type': "application/x-www-form-urlencoded",
    'cookie': "__utmc=97291215; __utma=97291215.710864539.1529285802.1529285802.1529289216.2; __utmz=97291215.1529289216.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)",
    'host': "www.atilika.org",
    'origin': "http://www.atilika.org",
    'referer': "http://www.atilika.org/",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/70.4.222 Chrome/64.4.3282.222 Safari/537.36",
    'x-requested-with': "XMLHttpRequest",
    'cache-control': "no-cache",
    'postman-token': "c98c3f63-8b51-4e71-6804-6814c3ca8d02"
    }
import json
def read(dir):
    with open(dir,encoding="utf-8") as file:
        return json.load(file)

def token(str):
    payload = "text="+urllib.parse.quote_plus(str)+"&mode=0"
    response = requests.request("POST", url, data=payload, headers=headers)

    return [X["surface"] for X in json.loads(response.text)["tokens"]]
def tokenB(str):
    payload = "text="+urllib.parse.quote_plus(str)+"&mode=0"
    response = requests.request("POST", url, data=payload, headers=headers)
    k=json.loads(response.text)
    return [X["base"] for X in k["tokens"] if "base" in X.keys()]


def listkey(dic):
    temp={}
    ind=0
    for i in dic:
        for k in i:
            temp[str(k)]=[]
            t=[]
            for  j in i[k]:
                # for h in token(j):
                #     t.append(h)
                try:
                    for h in token(j.strip()):
                        t.append(h)
                        print(h,"=====",j)
                        if h=="" or h==" ":
                            print(j+"*******************************")
                except:
                    print(j)
            temp[str(k)]=t
        print(ind)
        ind+=1

    return temp
    # print(temp)

def save(data,dir):
    with open(dir,"w",encoding="utf-8") as file:
        json.dump(data,file,ensure_ascii=False,indent=4)

# form=read("form.json")





# save(listkey(form),"f.json")
keylist=[]
form=read("f.json")
F=read("form.json")
for i in  form.keys():
    for j in form[i]:
        keylist.append(j)

keylist=list(set(keylist))



def sublist(l1,l2):
    leng=len(l1)
    leng1=len(l2)
    t=0
    t1=0
    while t<leng and t1<leng1:
        if l1[t]==l2[t1]:
            t1=t1+1
        t=t+1
    if t1==leng1:
        return True
    return False
def subString(arr,S):
    for i in arr:
        if i not in S:
            return False
    return True

def G(SS):
    SS=SS.replace(" ","")
    S=token(SS)
    S1=tokenB(SS)
    S=[X for X in S if X in keylist ]
    S1=[X for X in S1 if X in keylist ]
    j=0
    tem=[]

    for i in form.keys():
        if sublist(S,form[i])or sublist(S1,form[i]):
            # print([X for X in F[j].values()])
            # print(SS)
            try:
                if subString([X[0] for X in F[j].values()],SS):
                    tem.append([len(form[i]),str(F[j])])
            except:
                print(F[j])
        j=j+1

    tem.sort(reverse=True)
    return tem

import time
t=time.time()
KK="バーカッ そんな大金 見せびらかすな!"
print(G(KK))
print(time.time()-t)