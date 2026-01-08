n=int(input("Enter a number:"))
even=0
odd=0
for i in range(1,n+1):
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("Even Numbers of range 1 to ",(n), "are: ",(even))
print("Odd Numbers of range 1 to ",(n), "are: ",(odd))
