# First question
def f(x):
  d=0
  while x > 1:
    (x,d) = (x/2,d+1)
  return(d)
result=f(27182818)
print(result)

#Second question
def h(n):
    s = 0
    for i in range(2,n):
        if n%i == 0:
           s = s+i
    return(s)
ans1= h(60)
ans2= h(45)
result=ans1-ans2
print(result)

#Third question
def g(m,n):
    res = 0
    while m >= n:
        (res,m) = (res+1,m/n)
    return(res)
result= g(375,4)
print(result)