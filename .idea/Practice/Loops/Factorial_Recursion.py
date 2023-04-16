#a = int(input("Enter No. for which factorial to be known : "))
#fact = 1
#for i in range(a):
 #   fact = fact * (i+1)

#print(fact)

def fact_iter(n):
    rec = 1
    for i in range(n):
        rec = rec * (i+1)
    return rec

s = fact_iter(5)
print(s)

def fact_one(i):
    if i == 0 or i == 1:
      return 1
    return i * fact_one(i-1)

z = fact_one(10)

print(int(z))

