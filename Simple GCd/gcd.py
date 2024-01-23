# Program for find the GCD of two integers
def gcd(m,n):
    fm=[]
    for i in range(1,m+1):
        if (m%i==0):
            fm.append(i)
    fn=[]        
    for j in range(1,n+1):
        if (n%j==0):
            fn.append(j)
    cn=[]
    for f in fm:
        if f in fn:
            cn.append(f)
    
    return cn[-1]
m=int(input("Enter the first number: "))   
n=int(input("Enter the second number: "))
result =gcd(m,n)
print("GCD of ",m,",",n," : ",result)