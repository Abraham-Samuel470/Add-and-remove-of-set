print("***************** Add and Remove from set as per user choice ******************")
my_set={1,2,3,4,5}
while(True):
    
    print("Before adding:",my_set)
    ask=input("Do you want to add or remove(y/n)?")
    if ask=='y':
        op=input("Click 'A' to Add or Click 'R' to Remove")
        if op=='A':
            n=int(input("How many numbers to add : "))
            for i in range(0,n):
                  print("Add into set: ")
                  my_set.add(int(input()))
            print("My new set after adding is", my_set)
            continue
            print("*******************************************************************")
        elif op=='R':
            print(my_set)
            l=len(my_set)
            print("From above select what number to remove")
            m=int(input("How many numbers to remove : "))
            for i in range(0,m):
                my_set.remove(int(input()))
            print("My New set after removing is",my_set)
            print("*******************************************************************")
        else:
            print("Select a valid command")
    elif ask=='n':
        print("Program has terminated...")
        break
    else:
        print("Please select y or n!")
    my_set = my_set
    
