x = int(input())

def palindrome(n):
    new_x=0
    while(n>0):
        d=n%10
        new_x=(new_x*10) + d
        n=int(n/10)
        
    if new_x == x:
        return True
    return False

print(palindrome(x))