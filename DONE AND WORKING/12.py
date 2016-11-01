def histogram(inputList):
 
    for i in range(len(inputList)):
        print (inputList[i]*'*')
 
 
List = input("Please enter some numbers with spaces: ").split(",")
print (List)
histogram(List)
