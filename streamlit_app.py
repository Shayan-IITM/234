a = float(input("Enter any number: "))
b = float(input("Enter any number: "))
c = float(input("Enter any number: "))
def maximum(a, b, c):
 
    if (a >= b) and (a >= c):
        largest = a
 
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
         
    return largest
print(maximum(a, b, c))
