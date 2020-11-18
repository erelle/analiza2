
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





def yahakobi(matrix,solution):
    dom = dominant(matrix)
    if dom > 0:
        print("non dominant matrix ")
        return
    else:
        print("dominant matrix ")
        e=0.001
        x=0
        y=0
        z=0
        dif=10
        while dif>e:
            x0=x
            y0=y
            z0=z
            i=0
            x=(solution[0]-matrix[i][1]*y0-matrix[i][2]*z0)/matrix[i][0]
            i+=1
            y=(solution[1]-matrix[i][0]*x0-matrix[i][2]*z0)/matrix[i][1]
            i+=1
            z=(solution[2]-matrix[i][0]*x0-matrix[i][1]*y0)/matrix[i][2]
            print("x: ", x, "y: ", y, "z: ",z)
            dif=abs(x-x0)













def zaidel(matrix, solution):
    dom = dominant(matrix)
    if dom > 0:
        print("non dominant matrix ")
        return
    else:
        print("dominant matrix ")



choice=int(input("which one do you want to use: 1 yahakobi, 2 zaidel "))
if choice==1:
    yahakobi(matrix,solution)
if choice==2:
    zaidel(matrix,solution)



