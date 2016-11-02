def histogram(inputList):
 
    for i in range(len(inputList)):
        print (inputList[i]*'*')#prints correct number of stars for each number
 
 
ips = [int(x) for x in input("Please enter a list of numbers you'd like evaluated, with spaces: ").split()] #Split function that works
histogram(ips)
