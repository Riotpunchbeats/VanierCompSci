def histogram(inputList):
 
    for i in range(len(inputList)):
        print (inputList[i]*'*')
 
 
List = raw_input("Please enter some numbers with spaces: ").split(",")
List = [int(i) for i in List]
histogram(List)
