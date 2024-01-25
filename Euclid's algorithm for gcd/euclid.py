#Euclid's algorithm for gcd of two numbers
def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if m%n==0:
        return n
    else:
        diff=m-n
        return gcd(max(n,diff),min(n,diff))
m=int(input("Enter the first number: "))   
n=int(input("Enter the second number: "))
result =gcd(m,n)
print("GCD of ",m,",",n," : ",result)

#Another Euclid's algorithm for gcd of two numbers using while loop
def gcd(m,n):
    if m<n:
       (m,n)=(n,m)
    while (m%n!=0):
        diff=m-n
        (m,n)=(max(n,diff),min(n,diff))
    return n
m=int(input("Enter the first number: "))   
n=int(input("Enter the second number: "))
result =gcd(m,n)
print("GCD of ",m,",",n," : ",result)    