# Linear Search - check the searching item or value start to end in the array or list

# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	ele = int(input())
	# adding the element
	lst.append(ele) 

print(lst)

target = int(input("Enter the target value: "))

# check target value with lst
for i in range(0, n):
    if target == lst[i]:
        print(i)
        break
    # else block runs if target not matched
else:
    print("Target not present in the list")