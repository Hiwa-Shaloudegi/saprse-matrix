def make_to_matrix(address_file1, address_file2):

    # Open and Read files

    f1 = open(address_file1, 'r')
    f2 = open(address_file2, 'r')

    f1 = open(address_file1, 'r')
    content1 = f1.read()
    f1.close()

    f2 = open(address_file2, 'r')
    content2 = f2.read()
    f2.close()


    # Converting file's content to array_2D (matrix)

    arr1 = content1.split(" / ")
    arr1_2d = [i.split(" ") for i in arr1]

    arr2 = content2.split(" / ")
    arr2_2d = [i.split(" ") for i in arr2]


    return arr1_2d, arr2_2d







def densify(matrix):

    rows = []
    columns = []
    values = []

    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if int(matrix[i][j]) != 0:
                rows.append(i)
                columns.append(j)
                values.append(int(matrix[i][j]))


    # WRONG
    # result = [[]*3] * len(rows)

    result  = [[]*3 for i in range(len(rows))]

    i = 0
    for x in result:
        
        x.append(rows[i])
            
        x.append(columns[i])
    
        x.append(values[i])
        i += 1

    return result





def tranpose(matrix):
    sparse = densify(matrix)
    pass




def add(matrix1, matrix2):

     sparse1 = densify(matrix1)
     sparse2 = densify(matrix2)

     pass
    
    
        




    
def minus(matrix1, matrix2):
    sparse1 = densify(matrix1)
    sparse2 = densify(matrix2)
    pass



    
def multiply(matrix1, matrix2):
    sparse1 = densify(matrix1)
    sparse2 = densify(matrix2)
    pass




    
def divide(matrix1, matrix2):
    sparse1 = densify(matrix1)
    sparse2 = densify(matrix2)
    pass








################## Pretty print of Matrix
    # for row in result:
    #     for cell in row:
    #         print(cell, end='\t')
    #     print(end='\n')

    ###OR

    #'\n'.join(['\t'.join([str(cell) for cell in row]) for row in result])