#/usr/bin/python
#
#This python program converts nested array to flat array eg: [[1,2,[3]],4] as [1,2,3,4]
#

inputArray=[[1,2,[3]],4]
flatArray=[]

## This function inserts item to flatArray

def insertToArray(value):
    flatArray.append(value)

## This function iterates through elements of the array recursively 
## and inserts to the flat array

def iterateArray(inputArray):
    if  type(inputArray) == type([]):
        for item in inputArray:
            if type(item) == type([]):
                iterateArray(item)
            else:
                insertToArray(item)
        
    
iterateArray(inputArray)

print "Result: " +  str(flatArray)






    
    

