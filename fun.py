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




