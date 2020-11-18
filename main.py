
matrix=[]
row=[]
rows= int(input("enter number of rows: "))
for i in range (rows):
    for i in range (rows):
        num=float(input("enter a number "))
        row.append(num)
    matrix.append(row)
    row = []
print("your matrix is " ,matrix)
solution=[]
for i in range (rows):
    num = float(input("enter a number for solution"))
    solution.append(num)

def dominant(matrix):
    sumNum=0
    flag=0
    for i in range(len(matrix)):
        sumNum=abs(sum(matrix[i]))-abs(matrix[i][i])
        if abs(matrix[i][i])<sumNum:
            flag+=1
    return flag

def EmptyMatrix(matrix):
    m=[]
    row=[]
    num = 0
    for i in range(len(matrix)):
        for i in range(len(matrix)):
            row.append(num)
        m.append(row)
        row = []
    return m


def findLUD(matrix):
    x0 = 0
    L = EmptyMatrix(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            int(i)
            int(j)
            if j >= i:
                L[i][j] = 0
            else:
                L[i][j] = int(matrix[i][j])
    print("L :", L)
    U = EmptyMatrix(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            int(i)
            int(j)
            if j <= i:
                U[i][j] = 0
            else:
                U[i][j] = int(matrix[i][j])
    print("U :", U)
    D = EmptyMatrix(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            int(i)
            int(j)
            if j == i:
                D[i][j] = int(matrix[i][j])
            else:
                D[i][j] = 0

    print("D :", D)
    return L,U,D


def yahakobi(matrix,solution):
    dom = dominant(matrix)
    if dom > 0:
        print("non dominant matrix ")
        return
    else:
        print("dominant matrix ")




    L,U,D=findLUD(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
          if D[i][j]!=0:
              D[i][j]*=1/10








def zaidel(matrix, solution):
    dom = dominant(matrix)
    if dom > 0:
        print("non dominant matrix ")
        return
    else:
        print("dominant matrix ")
    findLUD(matrix)



choice=int(input("which one do you want to use: 1 yahakobi, 2 zaidel "))
if choice==1:
    yahakobi(matrix,solution)
if choice==2:
    zaidel(matrix,solution)



