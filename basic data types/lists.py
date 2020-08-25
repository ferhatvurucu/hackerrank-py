'''
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.
'''
n = int(input())
arr = []
for i in range(n):
    command, *values = input().split()
    if command == "print":
        print(arr)
    else:
        exec_command = 'arr.' + command + "(" + ','.join(values) + ')'
        eval(exec_command)