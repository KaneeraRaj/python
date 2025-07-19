def is_disarium(n):
    s=str(n)
    total=0
    for i in range(len(s)):
        total=int(s[i])**(i+1)
        return total==n
    
    n=int(input("Enter a number:"))

    if is_disarium(n):
        print("It is a disarium number")
    else:
        print("It is not a disarium number")