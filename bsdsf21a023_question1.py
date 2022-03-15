from ast import If


data =int(input("ENTER DATA: "))
a =[0,11,22,33,44,55,66,88,99,100]
l =0
r =9
m =(l+r)//2
if data==a[m]:
    print(m)
elif data>a[m]:
    l =m+1
    m =(l+r)//2 
    if data==a[m]:
        print(m)
    elif data>a[m]:
        l =m+1
        m =(l+r)//2 
        if data>a[m]:
            print("9")
        else:
            print("8")  
    elif data<a[m]:
        r =m-1
        m =(l+r)//2
        if data==a[m]:
            print(m)
        elif data>a[m]:
            print(l)            

elif data<a[m]:
    r =m-1
    m =(l+r)//2
    if data==a[m]:
        print(m)
    elif data<a[m]:
        print("0")
    elif data>a[m]:
        l =m+1
        m =(l+r)//2
        if data==a[m]:
            print("2")
        else:
            print("3")        
