m = int(input("Enter Marks to be graded : "))

if(m>=90):
    print("Excellent "+str(int(m/100*100))+'%')

elif(m>=80):
    print("Very Good "+str(int(m/100*100))+'%')

elif(m>=70):
    print("Good")
    print("Good "+str(int(m/100*100))+'%')


elif(m>=60):
    print("Can do better "+str(int(m/100*100))+'%')

elif(m>=50):
    print("Just Passed "+str(int(m/100*100))+'%')

else:
    print("You have to repeat "+str(int(m/100*100))+'%')

