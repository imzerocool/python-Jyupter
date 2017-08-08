def temp_con():
    while True:
        try:
            temp=int(raw_input("Enter Temperature: "))
            break
        except:
            print "Enter Temperature in Float followed by c/f | Example 35.55c or 35.55C"
            return
    t=float(temp[0:-1])  # String slicing Example
    if temp[-1]=="f":
        print"Temperature is correct...."
        print t
        c=((t-32)/9)*5
        print "Temperatre in Centigrade: ",c
    elif temp[-1]=="c":
        print t
        f=((t/5)*9)+32
        print "Temperature in Fahrenheit: ",f