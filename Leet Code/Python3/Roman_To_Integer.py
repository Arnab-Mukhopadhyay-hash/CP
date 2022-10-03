# taking the roman number as input string
inputString = input()
# dictionary containing the values of the roman numerals
valueDict = {'I': 1, 
'V': 5, 
'X': 10,
'L': 50,
'C': 100,
'D': 500,
'M': 1000}
# converting the string to a char array or character list
stringList = []
stringList[:0] = inputString

# converting the input string to integer
num = 0
for i in range(len(stringList)):
    if i != len(stringList) - 1:
        if stringList[i] == 'I' and (stringList[i+1] == 'V' or stringList[i+1] == 'X'):
            num = num - valueDict['I']
        elif stringList[i] == 'X' and (stringList[i+1] == 'L' or stringList[i+1] == 'C'):
            num = num - valueDict['X']
        elif stringList[i] == 'C' and (stringList[i+1] == 'D' or stringList[i+1] == 'M'):
            num = num - valueDict['C']
        else:
            num = num + valueDict[stringList[i]]
    else:
        num = num + valueDict[stringList[i]]
        
print(num)

