# Error Handling first Programe
while True:
    try:
        x=int(raw_input("Enter a Number: "))
        break
    except ValueError:
        print "Not an Number, Try Again..."
print "Thank You..!!"