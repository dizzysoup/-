def B(cf,p):
    print('A:',end='')
    cf(p)
def CF(p):
    print(p,end='')
def A(X):
    print('B:',end='')
    B(CF,X)
    print()
def M(x):
    f=lambda s:s[0]*s[1] if s[1]>s[2] else s[0] + s[1]
    print(f(x))
def K(perm):
    if len(perm)<=1:return [perm]
    r = []
    for i in range(len(perm)):
        others = K(perm[:i]+perm[i+1:])
        for s in others:
            r =r +[perm[i]+s]
    return r

print(K('XYZ')) # ['XYZ','XZY','YXZ','YZX','ZXY','ZYX']
A('C') # B:A:C
M([4,5,6,7]) # 9

# 1-2 質數判斷
def g(N):
    for i in range(2,N):
        if N%i == 0 : return False
    return True
def f(N):
    data=[i for i in range(2,N) if g(i) == True]
    return data
print(f(20)) # [2,3,5,7,11,13,17,19]

#1-3
def h(data):
    result=[]
    length=len(data)
    for s in range(length):
        x = data[s]
        y = data[0:s]+data[s+1:length]
        result = result + [x+y]
    return result 
print(h('ABCD')) # ['ABCD','BACD','CABD','DABC']