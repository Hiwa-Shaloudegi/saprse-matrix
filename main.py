import sparse 
spr = sparse.Function()


while (True):
    print("\t\t\t\t\tWelcome, I do some operations on sparse matrices :)")
    print()

    
    ################

    # Read file
    address1 = input("Enter the first file address (the first matrix): ")
    address2 = input("Enter the second file address (the second matrix): ")
    #f1 = open(address1, 'r')
    #f2 = open(address1, 'r')

    f = open('example.txt', 'r')
    content = f.read()
    f.close()


    # Convert to 2D matrix

    arr = content.split(" / ")
    
    arr_2d = [i.split(" ") for i in arr]

    ################

    print("1- add")
    print("2- minus")
    print("3- multiply")
    print("4- divide")
    print("5- tranpose")
    print("6- Exit")
    print()

    selected_number = int(input("Enter The Number: "))


    if selected_number == 1:
        pass




    elif selected_number == 2:
        pass



    elif selected_number == 3:
        pass




    elif selected_number == 4:
        pass




    elif selected_number == 6:
        pass



    elif selected_number == 6:
        quit()



    else:pass #try catch





# Call sparses methods



# Show output results


