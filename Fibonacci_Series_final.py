terms = int(input("Number of Terms Here: "))

a = 0
b = 1
count = 0
if terms <= 0:
    print( "the Number should be Above 0")
elif terms == 1:
    print(0)

else:
    while count < terms:
        print(a)
        c = a + b
        # Update the numbers
        a = b
        b = c
        count += 1