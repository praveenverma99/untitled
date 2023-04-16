num = int(input("Enter No. to be checked for even ,odd, prime  : "))

#11prime = true

for i in range(2, num):
    if(num%i == 0):
     #   prime = false
        break

    if prime:
        print("This number is Prime")

    else:
        print("This number is not Prime")
