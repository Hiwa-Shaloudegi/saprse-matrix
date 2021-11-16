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

    rows_columns_indexes = []
    valuse = []
    matrix_result  = []

    sparse = densify(matrix)


    for row in sparse:
        rows_columns_indexes.append(row[:2])
        valuse.append(row[2])


    i = 0
    for arr in rows_columns_indexes:
        arr.reverse()
        arr.append(valuse[i])
        i += 1
        matrix_result.append(arr)


    matrix_result.sort()

    return matrix_result






def add(matrix1, matrix2):

    matrix_result  = []

    sparse1 = densify(matrix1)
    sparse2 = densify(matrix2)

    
    for sparse1_row in sparse1:
        for sparse2_row in sparse2:

            if sparse1_row[:2] == sparse2_row[:2]:

                suum = sparse1_row[2] + sparse2_row[2]

                result_row = sparse1_row[:2]
                result_row.append(suum)

                matrix_result.append(result_row)


                index1 = sparse1.index(sparse1_row)
                sparse1[index1].clear()

                index2 = sparse2.index(sparse2_row)
                sparse2[index2].clear()

                break

            
    for row1 in sparse1:
        if row1 != []:
            matrix_result.append(row1)

    for row2 in sparse2:
        if row2 != []:
            matrix_result.append(row2)

    
    matrix_result.sort()

    return matrix_result





    
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