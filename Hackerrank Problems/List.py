'''
Question
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
'''
if __name__ == '__main__':
    N = int(input())
    List=[]
    for i in range(1,N+1):
        ope=input().split(" ")
        if (ope[0]=="append"):
            List.append(int(ope[1]))
        elif (ope[0]=="insert"):
            index = int(ope[1])
            if 0 <= index <= len(List):
                List.insert(index,int(ope[2]))
            else:
                print("Invalid index for insert operation.")
        elif (ope[0]=="sort"):
            List.sort()
        elif (ope[0]=="reverse"):
            List.reverse()
        elif (ope[0]=="pop"):
            List.pop()
        elif (ope[0]=="remove"): 
            List.remove(int(ope[1]))
        elif (ope[0]=="print"):
            print(List)
        else:
            print("invalid input")