"""
Program Goals:
1. Get the input from the user!
2. Convert that input to an INT
3. Add that input ot a list
4. Pull values from specific index positions
"""

#create functions that will perform those actions above
import random
myList = []
unique_List = []
def programStart():
    while True:
        try:
            print("how about we start with making a list")
           numToAdd = input("How many integers do you want to add?  ")
           numRange = input("And how high would you like these numbers to go?  ")
           for x in range(0, int(numToAdd)):
               myList.append(random.randint(0, int(numRange)))
               print("Your list is now complete!")
            print("Choose one of the following options. Type a number ONLY!")
            choice = input("""1. Add to list,
2. Return the value at an index position
3. Print List
4. Random Search
5. Linear Search
6. Print Lists
7. Recursive Binary Search
8. Iterive Binary Search
9. End Program  """)
            
            if choice == "1":
                addToList()
            elif choice == "2":
                indexValues()
            elif choice == "3":
                sortList(myList)
            elif choice == "4":
                randomSearch()
            elif choice == "5":
                linearSearch()
            elif choice == "6":
                printLists()
            elif choice == "8":
                binSearch = input("What number are you looking for?   ")
                result = iteriveBinarySearch(unique_List, 0, len(unique_List, int(binSearch))
                if result != -1:
                    print("Your number is at index position {}".format(result))
                else:
                    print("Your number isnt here")
            elif choice == "7":
                binSearch = input("What number are you looking for?   ")
                recursiveBinarySearch(unique_List, 0, len(unique_List)-1, int(binSearch))
                
                
            else:
                print("The program will now end.  ")
                break
        except:
            print("An error occurred")

def addToList():
    newItem = input("Please type an integer!  ")
    myList.append(newItem)
    print(int(newItem))
    print(myList)

def addABunch():
    print("We're gonna add a bunch of numbers!")
    numToAdd = input("How many integers do you want to add?  ")
    numRange = input("And how high would you like these numbers to go?  ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete!")


def sortList(myList):
    for x in myList:
        if x not in unique_List:
            unique_List.append(x)
    unique_List.sort()
    showMe = input("Wanna see your new list? Y/N    ")
    if showMe.lower() == "y":
        print(unique_List)

def printLists():
    if len(unique_List) == 0:
        print(myList)
    else:
        whichOne = input("Which list? Sorted or un-sorted?      ")
        if whichOne.lower() == "Sorted":
            print(unique_List)

def indexValues():
    indexPos = input("At what index position would you like to look?  ")
    print(myList[int(indexPos)])

def randomSearch():
    print("Here's a random value from your list!")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're going to search through the list IN THE WORST WAY POSSIBLE!")
    searchItem = input("What are you looking for number-wise  ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index {}".format(x))

def recursiveBinarySearch(unique_List, low, high, x):
    if high >= low:
        mid = (high + low) //2

        if unique_List[mid] == x:
            print("oh, what luck. your number is at position {}".format(mid))
        elif unique_List[mid] > x:
            return recursiveBinarySearch(unique_List, low, mid -1, x)
        else:
            return recursiveBinarySearch(unique_List, mid + 1, high, x)
    else:
        print("Your number isn't here")

def iteriveBinarySearch(unique_List, x):
    low = 0
    high = len(unique_List) - 1
    mid = 0

    while low >= high:
        mid = (high+low) // 2

        if unique_List[mid] < x:
            low = mid + 1

        elif unique_List[mid] > x:
            high = mid -1

        else:
            return mid
    return -1
    

if __name__ == "__main__":
    mainProgram()
