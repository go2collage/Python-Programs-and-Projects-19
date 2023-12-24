# Python Program / Project

def accept_roll():
    rollno = []
    students = int(input("Enter number of students: "))
    for i in range(students):
        roll = int(input("Enter Roll number: "))
        rollno.append(roll)
    return rollno

def print_roll(rollno):
    for i in range(len(rollno)):
        print(rollno)
        break

def ins_sort(rollno):
    for i in range(len(rollno)):
        key = rollno[i]
        j = i - 1
        while j>=0 and key < rollno[j]:
            rollno[j+1] = rollno[j]
            j -= 1 
            rollno[j+1] = key
    return rollno

def nr_ternarysearch(sort_roll, find_roll):
    left = 0
    right = len(sort_roll) - 1
    while left <= right:
        mid1 = left + (right-left) //3
        mid2 = left + 2 * (right - left) // 3
        if find_roll == sort_roll[left]:
            return left
        elif find_roll == sort_roll[right]:
            return right
        elif find_roll < sort_roll[left] or find_roll > sort_roll[right]:
            return -1
        elif find_roll <= sort_roll[mid1]:
            right = mid1
        elif find_roll > sort_roll[mid1] and find_roll <= sort_roll[mid2]:
            left = mid1+1
            right = mid2
        else:
            left = mid2 + 1
    return -1

def r_ternarysearch(sort_roll,left, right, find_roll):
    if (right >= left):
        mid1 = left + (right-left) //3
        mid2 = right - (right - left) // 3
        if(sort_roll[mid1] == find_roll):
            return mid1
        if (sort_roll[mid2] == find_roll):
            return mid2

        if(find_roll < sort_roll[mid1]):
            return r_ternarysearch(sort_roll,left, mid1-1, find_roll)
        elif find_roll > sort_roll[mid2]:
            return r_ternarysearch(sort_roll,mid2+1, right, find_roll)
        else:
            return r_ternarysearch(sort_roll,mid1+1, mid2+1, find_roll)
    return -1


# Driver Code

unsort_roll = []
sort_roll = []

while (True):
    print("************ Menu ************")
    print("1. Accept Students roll numbers. ")
    print("2. Display the Students roll numbers. ")
    print("3. Sort roll numbers from the list.")
    print("4. Perform Non-Recursive Ternary Search.")
    print("5. Perform Recursive Ternary Search.")
    print("6. Exit.")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        unsort_roll = accept_roll()
    elif choice == 2:
        print_roll(unsort_roll)
    elif choice == 3:
        print("Elements after performing sort operation: ")
        sort_roll =  ins_sort(unsort_roll)
        print(sort_roll)
    elif choice == 4:
        find_roll = int(input("Enter the Roll number to search: "))
        index = nr_ternarysearch(sort_roll, find_roll)
        if index != -1:
            print("Roll number found.")
        else:
            print("Roll number not found.")
    elif choice == 5:
        find_roll = int(input("Enter the Roll number to search: "))
        left = 0
        right = len(sort_roll) - 1
        index = r_ternarysearch(sort_roll,left, right, find_roll)
        if index != -1:
            print("Roll number found.")
        else:
            print("Roll number not found.")

    else:
        print("You have exit.")
        exit()