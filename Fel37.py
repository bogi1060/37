import numpy as np


db=int(input("Hany sziget legyen?: "))




sziget=np.chararray((3,3))
sziget[:]="O"

viz=np.chararray((100,100))
viz[:]="~"
mtx=np.random.randint(2, size=(100, 100))

print("Matrix: ",sziget,viz)

sum=10000//16
print ("Max sziget: ",sum)

