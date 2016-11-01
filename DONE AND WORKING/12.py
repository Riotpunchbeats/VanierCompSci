#histogram function
inp = int(input("Please enter some numbers: ").split())
def histogram(inputList):
 
    for i in range(len(inputList)): #for the amount of each number in list, iterate over list
        print (inputList[i]*'*')#prints histogram based on list
 
 
List = inp
 
histogram(List)
