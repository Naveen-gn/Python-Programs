# First question
def f(x):
  d=0
  while x > 1:
    (x,d) = (x/2,d+1)
  return(d)
result=f(27182818)
print(result)