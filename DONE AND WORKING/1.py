"""find the largest of two numbers given by user"""
print ('Please enter two numbers')
"""prompt user to enter numbers"""

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
"""define maxiumum of two function"""
def maximum(num1, num2):
    if num1 > num2:
        print (num1)
    else:
        print (num2)
"""print result"""        
print ("this is the largest number: ")
maximum(num1, num2)
