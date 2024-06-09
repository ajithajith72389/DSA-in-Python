# Binary Search - Two pointers algorithm

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

# target value for searching
target = int(input("Enter the target value: "))

#initialize variable for two pointer search
left = 0
right = len(lst) - 1
mid = 0

#check two pointer algorithm to target value
while left <= right:
    # Get the middle index
    mid = (left + right) // 2
    # if value of middle index equal to target
    if target == lst[mid]:
        print(mid)
        break
    # if target greater than middle index value, move left index one step forward
    elif target >= lst[mid]:
        left = mid + 1
    # if target lesser than middle index value, move right index one step backward
    elif target <= lst[mid]:
        right = mid - 1

# target not present in the list return -1
else:
    print(-1)