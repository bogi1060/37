db=int(input("Hany sziget legyen?: "))

# mtx=np.random.randint(2, size=(100, 100))

sziget=np.chararray((3,3))
sziget[:]="O"
szigetek=sziget*db



viz=np.chararray((100,100))
viz[:]="~"
mtx=np.random.randint(2, size=(100, 100))

print("Matrix: ",szigetek,viz)

sum=10000//16
print ("Max sziget: ",sum)