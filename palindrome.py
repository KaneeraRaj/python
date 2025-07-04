def isPalindrome (string):
    leftpos=0
    rightpos=len(string)-1

    while rightpos>=leftpos:
        if not string[leftpos]==string[rightpos]:
            return False
        leftpos+=1
        rightpos-=1 
    return True
    
print("Is this a palindrome?")
print(isPalindrome('malayalam'))