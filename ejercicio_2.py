num = int(input("Ingresa el numero: "))
cuenta=0
for i in range (2, num):
    if(num % i==0):
        cuenta=cuenta+1 
if(num==1):
        cuenta=3
if(cuenta>1):
        print("No es primo")
else:
        print("Es primo")
