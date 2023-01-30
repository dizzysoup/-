step = 0 # 用來記錄執行次數
#2-1
def fibonacci(n):
    global step 
    step = step + 1 
    if n <= 0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
def f(x):
    global step 
    step = 0 
    i = 0
    while i < x:
        print(fibonacci(i),end=',')
        i = i+1    
    print(step)
   
#2-2
def fibonaccii(n):
    data = [0 for i in range(0,n+1)]
    data[1] = 1
    for i in range(2,n+1):
        data[i] = data[i-1] + data[i-2]
    return data
def h(x):
    data = fibonaccii(x)
    for i in range(x):
        print(data[i],end=',') 

#2-3
def fibonacci3(n,data):
    if n>5:print(n,' * ',end='')
    if n <=0:return 0
    elif n==1 or n ==2:data[n]=1
    elif data[n]==0:
        data[n] = fibonacci3(n-1,data)+fibonacci3(n-2,data)
    return data[n]
def p(x):
    data = [0 for i in range(x+1)]
    for i in range(x):
        fibonacci3(i,data)

def main():
    # f(8) # 2-1
    # h(8) # 2-2
    p(8) #2-3

if __name__ == '__main__' :
    main()