def Mainmenu():
    print("""
+-+-+-+-+-+ SORTING ALGORITHM APPLICATION +-+-+-+-+-+ 
-         Programmed by: Mahid L. Dandamun          - 
+                    BSCOE 2-5                      +
-                                                   -
+            < < < M A I N  M E N U > > >           +
-            [1] SELECTION SORTING                  -
+            [2] BUBBLE SORTING                     +
-            [3] INSERTION SORTING                  -
+            [4] MERGE SORTING                      +
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ """)

def addtolist(num, list):
    print("Enter your", {num}, "INTEGERS now (END EACH INTEGER BY AND ENTER KEY) =>")
    for i in range(0, num):
        data = int(input())
        if data != "":
            list.append(data)
def addtolistText(num, list):
    print("Enter your", {num}, "LETTERS now (END EACH LETTER BY AND ENTER KEY) =>")
    for i in range(0, num):
        data = input()
        if data.isupper() and data != "" and not data.isdigit():    
            list.append(data)
        else:
            return
list1 = []
# Algo1= Ascending
# Algo2= Descending

def selection_algo1():
    for j in range(len(list1) - 1):
        min_val = min(list1[j:])
        min_index = list1.index(min_val, j)
        if list1[j] != list1[min_index]:
            list1[j], list1[min_index] = list1[min_index], list1[j]
        print("PASS", j + 1, ":", list1)
    print("FINAL SORTED ELEMENTS => ", list1)

def selection_algo2():
    for j in range(len(list1) - 1):
        max_val = max(list1[j:])
        max_index = list1.index(max_val, j)
        if list1[j] != list1[max_index]:
            list1[j], list1[max_index] = list1[max_index], list1[j]
        print("PASS", j + 1, ":", list1)
    print("FINAL SORTED ELEMENTS => ", list1)

def bubble_algo1():
    for j in range(len(list1) - 1):
        for i in range(len(list1) - 1):
            if list1[i] > list1[i + 1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
        print("PASS", j + 1, ":", list1)
    print("FINAL SORTED ELEMENTS => ", list1)

def bubble_algo2():
    for j in range(len(list1) - 1):
        for i in range(len(list1) - 1):
            if list1[i] < list1[i + 1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
        print("PASS", j + 1, ":", list1)
    print("FINAL SORTED ELEMENTS => ", list1)

def insertion_algo1():
    for i in range(1, len(list1)):
        current_elem = list1[i]
        pos = i - 1
        while pos >= 0:
            if current_elem < list1[pos]:
                list1[pos + 1] = list1[pos]
                list1[pos] = current_elem
                pos = pos - 1
            else:
                break
        print("PASS", i, ":", list1)
    print("FINAL SORTED ELEMENTS => ", list1)

def insertion_algo2():
    for i in range(1, len(list1)):
        current_elem = list1[i]
        pos = i - 1
        while pos >= 0:
            if current_elem > list1[pos]:
                list1[pos + 1] = list1[pos]
                list1[pos] = current_elem
                pos = pos - 1
            else:
                break
        print("PASS", i, ":", list1)
    print("FINAL SORTED ELEMENTS => ", list1)

def merge_algo1(list1):
    if len(list1) > 1:
        mid = len(list1)//2
        leftside_list = list1[:mid]
        rightside_list = list1[mid:]
        merge_algo1(leftside_list)
        merge_algo1(rightside_list)
        i = 0
        j = 0
        k = 0
        while i < len(leftside_list) and j < len(rightside_list):
            if leftside_list[i] < rightside_list[j]:
                list1[k] = leftside_list[i]
                i += 1
                k += 1
            else:
                list1[k] = rightside_list[j]
                j += 1
                k += 1
        while len(leftside_list) > i:
            list1[k] = leftside_list[i]
            i += 1
            k += 1
        while len(rightside_list) > j:
            list1[k] = rightside_list[j]
            j += 1
            k += 1
        print("FINAL SORTED ELEMENTS => ", list1)
    else:
        return
def merge_algo2(list1):
    if len(list1) > 1:
        mid = len(list1)//2
        leftside_list = list1[:mid]
        rightside_list = list1[mid:]
        merge_algo1(leftside_list)
        merge_algo1(rightside_list)
        i = 0
        j = 0
        k = 0
        while i < len(leftside_list) and j < len(rightside_list):
            if leftside_list[i] < rightside_list[j]:
                list1[k] = leftside_list[i]
                i += 1
                k += 1
            else:
                list1[k] = rightside_list[j]
                j += 1
                k += 1
        while len(leftside_list) > i:
            list1[k] = leftside_list[i]
            i += 1
            k += 1
        while len(rightside_list) > j:
            list1[k] =rightside_list[j]
            j += 1
            k += 1
        list1.reverse()
        print("FINAL SORTED ELEMENTS => ", list1)
    else:
        return

def merge_sort(algor1, algor2):
    try:
        num = int(input("How many elements are there on our lists?"))
        if num > 0:
            elementtype = int(input("Enter type of element? [1] INTEGERS [2]LETTERS(Upper-case Only) => "))
            match elementtype:
                case 1:  # integers
                    sortmode = int(input("Enter the sorting mode:[1] ASCENDING [2] DESCENDING => "))
                    match sortmode:
                        case 1:  # ascending
                            addtolist(num, list1)
                            algor1(list1)
                        case 2:  # Descending
                            addtolist(num, list1)
                            algor2(list1)
                        case _:
                            print("Your input is not within the choices")
                            print()
                            return
                case 2:  # Letters
                    sortmode = int(input("Enter the sorting mode:[1] ALPHABETICALLY [2] REVERSE ALPHABETICAL ORDER=> "))
                    match sortmode:
                        case 1:  # Alphabetical
                            addtolistText(num, list1)
                            algor1(list1)

                        case 2:  # Reverse Alphabetical
                            addtolistText(num, list1)
                            algor2(list1)
                        case _:
                            print("Your input is not within the choices")
                            print()
                            return
                case _:
                    print("Your input is not within the choices")
                    print()
                    return
    except ValueError:
        print("Invalid input")
        print()




def sort(algo1, algo2):
    try:
        num = int(input("How many elements are there on our lists?"))
        if num > 0:
            elementtype = int(input("Enter type of element? [1] INTEGERS [2]LETTERS(Upper-case Only) => "))
            match elementtype:
                case 1:  # integers
                    sortmode = int(input("Enter the sorting mode:[1] ASCENDING [2] DESCENDING => "))
                    match sortmode:
                        case 1:  # ascending
                            addtolist(num, list1)
                            algo1()
                        case 2:  # Descending
                            addtolist(num, list1)
                            algo2()
                        case _:
                            print("Your input is not within the choices")
                            print()
                            return
                case 2:  # Letters
                    sortmode = int(input("Enter the sorting mode:[1] ALPHABETICALLY [2] REVERSE ALPHABETICAL ORDER=> "))
                    match sortmode:
                        case 1:  # Alphabetical
                            addtolistText(num, list1)
                            algo1()

                        case 2:  # Reverse Alphabetical
                            addtolistText(num, list1)
                            algo2()
                        case _:
                            print("Your input is not within the choices")
                            print()
                            return
                case _:
                    print("Your input is not within the choices")
                    print()
    except ValueError:
        print("Invalid input")
        print()
        return

def program():
    while True:
        Mainmenu()
        try:
            option = int(input("Select an option: "))
            print()

            if option == 1:  # Selection sort
                sort(selection_algo1, selection_algo2)
                ch = input("Do you wan to try again? [y/n]")
                if ch == 'y':
                    list1.clear()
                    continue
                else:
                    break

            elif option == 2:  # Bubble sort
                    sort(bubble_algo1, bubble_algo2)
                    ch = input("Do you wan to try again? [y/n]")
                    if ch == 'y':
                        list1.clear()
                        continue
                    else:
                        break

            elif option == 3:  # Insertion sort
                    sort(insertion_algo1, insertion_algo2)
                    ch = input("Do you wan to try again? [y/n]")
                    if ch == 'y':
                        list1.clear()
                        continue
                    else:
                        break

            elif option == 4:  # Merge sort

                merge_sort(merge_algo1, merge_algo2)
                ch = input("Do you wan to try again? [y/n]")
                if ch == 'y':
                    list1.clear()
                    continue
                else:
                    break

            else:
                print("Your input is not within the choices")
                print()
                continue

        except ValueError:
            print("Invalid input")
            print()
program()
