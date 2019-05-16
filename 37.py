import random
import numpy as np

# def szigetek(viz,sziget,N):
#     N=int(input("Hány sziget legyen?: "))
#     viz=="~"
#     sziget=np.empty((3,3),np.int)
#     sziget=="O"
#     mat=np.empty((100,100),np.int)
# print(szigetek)
#
#
#
# import random
#
#     mat0=random.randint(("~","O").int)
#     mat1=random.randint("~","O")
#     mat2=random.randint("~","O")
#     mat3=random.randint("~","O")
#     lst=[mat0,mat1,mat2,mat3]
#
#     print(lst[0],lst[1])
#     print(lst[2],lst[3])



# db=int(input("Hany sziget legyen?: "))
#
#
# sziget=np.chararray((3,3))
# sziget[:]="O"
#
# viz=np.chararray((100,100))
# viz[:]="~"
# mtx=np.random.randint(2, size=(100, 100))
#
# print("Matrix: ",sziget,viz)
#
# sum=10000//16
# print ("Max sziget: ",sum)

# try:
#     sziget(db)




def sziget(x):
    b = np.full((100, 100), "~")
    k = []
    t = []
    a = random.randrange(2, 97, 4)
    c = random.randrange(2, 97, 4)

    for i in range(x):

        while a in k:
            a = random.randrange(2, 97, 4)

        k.append(a)
        while c in t:
            c = random.randrange(2, 97, 4)
        t.append(c)

        print(k)
        print(t)
        b[a][c] = "O"
        b[a - 1][c - 1] = "O"
        b[a][c - 1] = "O"
        b[a - 1][c] = "O"
        b[a + 1][c] = "O"
        b[a + 1][c - 1] = "O"
        b[a + 1][c + 1] = "O"
        b[a][c + 1] = "O"
        b[a - 1][c + 1] = "O"

    print(b)


try:

    sziget(8)

except TypeError:
    print("Nem megfelelő input.")

np.set_printoptions(threshold=np.inf)