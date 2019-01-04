largest = None
smallest = 50000
while True:

    num = raw_input("Enter a number: ")
    if num == "done":
        break
    try:
        num = float(num)
    except:
        print ("Invalid input")
        continue
    if largest <= num:
        largest = int(num)
        print("doing largest")
    if smallest > num:
        smallest = int(num)
        print("doing smallest")

print ("Maximum is", largest)
print ("Minimum is", smallest)