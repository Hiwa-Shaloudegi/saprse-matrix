import sys
import sparse as spr


while (True):

    ################ Menu
    address1 = input("Enter the first file address: ")
    address2 = input("Enter the second file address: ")

    matrix1, matrix2 = spr.make_to_matrix(address1, address2)

    print()
    print("Choose an item:")
    print()
    print("1- add")
    print("2- minus")
    print("3- multiply")
    print("4- divide")
    print("5- tranpose")
    print("6- Exit")
    print()

    selected_number = int(input("Enter The Number: "))


    if selected_number == 1:
        result = spr.add(matrix1, matrix2)
        spr.pretty(result)



    elif selected_number == 2:
        result = spr.minus(matrix1, matrix2)
        spr.pretty(result)



    elif selected_number == 3:
        result = spr.multiply(matrix1, matrix2)
        spr.pretty(result)




    elif selected_number == 4:
        result = spr.divide(matrix1, matrix2)
        spr.pretty(result)




    elif selected_number == 5:

        n = int(input("Wich matrix? [1/2]: "))

        if n == 1:
            result = spr.tranpose(matrix1)

        elif n == 2:
            result = spr.tranpose(matrix2)

        else:
            sys.exit('Invalid Number!')

        spr.pretty(result)



    elif selected_number == 6:
        sys.exit("END OF THE PROGRAM")



    else:
        sys.exit('Invalid Number!') 


