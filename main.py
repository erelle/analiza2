#ניסיתי לעשות ליותר מ3 על 3 אבל לא הצלחתי כשזה הגיעה לפונקציות
#ניסיתי לפי LUD גם הסתבכתי

#name:erelle boubli
#id:324460443

matrix=[]
row=[]
rows= 3
print("enter numbes to fill a 3x3 matrix ")
for i in range (rows):
    for i in range (rows):
        num=float(input("enter a number "))
        row.append(num)
    matrix.append(row)
    row = []
print("your matrix is " ,matrix)
solution=[]
print("enter 3 solution numbers ")
for i in range (rows):
    num = float(input("enter a number for solution "))
    solution.append(num)

def dominant(matrix):
    sumNum=0
    flag=0
    for i in range(len(matrix)):
        sumNum=abs(sum(matrix[i]))-abs(matrix[i][i])
        if abs(matrix[i][i])<sumNum:
            flag+=1
    return flag


def yahakobi(matrix,solution):
    print("TAHAKOBI: ")
    dom = dominant(matrix)
    if dom > 0:
        print("your matrix is a non dominant matrix ")
        return
    else:
        print("your matrix is a dominant matrix ")
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
            print("x: ", x, ",y: ", y, ",z: ",z)
            dif=abs(x-x0)
        print("x-x0= ",dif)




def zaidel(matrix, solution):
    print("ZAIDEL: ")
    dom = dominant(matrix)
    if dom > 0:
        print("your matrix is a non dominant matrix ")
        return
    else:
        print("your matrix is a dominant matrix ")
        e = 0.001
        x = 0
        y = 0
        z = 0
        dif = 10
        while dif > e:
            x0 = x
            y0 = y
            z0 = z
            i = 0
            x = (solution[0] - matrix[i][1] * y0 - matrix[i][2] * z0) / matrix[i][0]
            i += 1
            y = (solution[1] - matrix[i][0] * x - matrix[i][2] * z0) / matrix[i][1]
            i += 1
            z = (solution[2] - matrix[i][0] * x - matrix[i][1] * y) / matrix[i][2]
            print("x: ", x, ",y: ", y, ",z: ", z)
            dif = abs(x - x0)
        print("x-x0= ",dif)

choice=int(input("which one do you want to use first: 1 yahakobi, 2 zaidel "))
if choice==1:
    yahakobi(matrix,solution)
    zaidel(matrix,solution)
if choice==2:
    zaidel(matrix,solution)
    yahakobi(matrix,solution)



