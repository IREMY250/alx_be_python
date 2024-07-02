n =int (input("Enter the size of the pattern:"))
x = 1
while x <= n :
    for i in range (1,n+1):
        print ("*", end="")
    print ()
    x=x+1
