inp = int(input("Please enter some numbers: ").split())
def histogram(inputList):
 
    for i in range(len(inputList)):
        print (inputList[i]*'*')
 
 
List = [inp]
 
histogram(List)
