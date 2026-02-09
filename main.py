while True:
    try: #Checks if the input is the correct type which is an integer
        exammark=int(input("What is your exam grade? - "))
        while exammark < 0: #Another while loop, checking if the exam grade is under 0
            exammark=int(input("Please input your exam grade again! - "))
        break
    except ValueError: #If the data doesn't match the input we are getting, this code prevents an error and loops the code back
        print("Please enter a valid number")
print("Checking your grade...")
print("Your grade is:")
if exammark > 80:
    print("A")
elif 60<=exammark<=79:
    print("B")
elif 40<=exammark<=59:
    print("C")
elif exammark <= 20:
    print("Fail")