def singBottles():
    for i in range(99,0,-1): #Sets range and increment to decrese by
        print(str(i)+"bottles of beer on the wall, "+str(i) +" bottles of beer.") #prints verse with current number of bottles
        print("Take one down pass it around," +str(i-1) +" bottles of beer on the wall.") #prints verse with one less bottle
        print(" ")
singBottles()
