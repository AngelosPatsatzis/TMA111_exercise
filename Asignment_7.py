import json

file = open("dictionaries.txt", "r")
dictionaryString = ''
#diabasma prwths grammhs tou arxeiou
for line in file:
    for character in line:
        dictionaryString += character
    break

#epexergasia prokeimenou na meinoun mono ta kleidia tou dictionary
dictionaryString = dictionaryString[1:-2]
dictionaryString = dictionaryString.replace('"','')

clearList = []
for i in range(len(dictionaryString)):
    clearString = ''
    if dictionaryString[i] == ':':
        for j in range(i,len(dictionaryString)):
           clearString += dictionaryString[j]
           if dictionaryString[j] == ',':
               break
        clearList.append(clearString)
    else:
        continue  

for i in range (len(clearList)):
    dictionaryString = dictionaryString.replace(clearList[i],'')
#dimiourgia listas me ta diathesima kleidia
keys = dictionaryString.split(' ')
flag = False
#check mexri o xrhsths na balei ena apo ta diathesima kleidia
while flag == False:
    print(f"Ta diathesima kleidia einai:\n {keys}")
    searchKey = input('Parakaloume pliktrologiste ena kleidi: ' )
    #anazithsh kleidiou
    for i in keys:
        if i == searchKey:
            print('To kleidi brethike')
            flag = True
            break
    if flag == False:
        print('To kleidi den brethike. Parakaloume xana prospathiste')

dictionaryList = []
#diabasma arxeiou character by character
for line in file:

    stringPerLine = ''
    for character in line:
        if character == '\n':
            break
        else:
            stringPerLine += character
    #metatroph ths kathe gramhs se dictionary
    dictionaryPerLine = json.loads(stringPerLine)
    #add in a list all the dictionaries from each line
    dictionaryList.append(dictionaryPerLine)
    
#print(dictionaryList)
#dhmiourgia dictionary me kleidia ta periexwmena tou kleidiou pou exei plhktrologhsei parapanw o xrhsths
#kai auto to dictionary tha exei san periexomena to plithos twn forwn pou emfanizontai
frequenceDictionary = {}
for i in range(len(dictionaryList)):
    if i == 0:
        frequenceDictionary[dictionaryList[i][searchKey]] = 1
    elif dictionaryList[i][searchKey] in frequenceDictionary:
        frequenceDictionary[dictionaryList[i][searchKey]] += 1
    else:
        frequenceDictionary[dictionaryList[i][searchKey]] = 1

#add in a list all the values of frequenceDictionary 
frequenceList = []
for i in frequenceDictionary:
    frequenceList.append(frequenceDictionary[i])
#print(frequenceList)

#euresh tou max auths ths list, dhladh thn dhmofilesterh timh
maxF = frequenceList[0]
for i in range(len(frequenceList)):
    if maxF < frequenceList[i]:
        maxF = frequenceList[i]

#add in another list the keys of the frequenceDictionary  
maxMinList = []
for i in frequenceDictionary:
    if frequenceDictionary[i] == maxF:
        popularValue = i
    maxMinList.append(i)

#euresh max and min ths listas auths
if type(maxMinList[0]) == int: 
    max = maxMinList[0]
    min = maxMinList[0]
else:
    max = len(maxMinList[0])
    min = len(maxMinList[0])
for i in range(len(maxMinList)):
    if type(maxMinList[i]) == int:
        if int(max) < maxMinList[i]:
            max = maxMinList[i]
        if int(min) > maxMinList[i]:
            min = maxMinList[i]
    #Theorw oti se peroptwsh pou to periexomeno tou kleidiou einai string, 
    #tha prepei na briskei to max kai to min analoga me to mhkos tou string
    elif type(maxMinList[i]) == str:
        if int(max) < len(maxMinList[i]):
            max = len(maxMinList[i])
        if int(min) > int(len(maxMinList[i])):
            min = len(maxMinList[i])

#Ektyposh apotelesmatwn
print(f"H dhmofilesterh timh tou kleidiou autou einai {popularValue}")
print(f"H megalyterh timh apo ta periexomena twn kleidiwn autwn einai {max}")
print(f"H mikroterh timh apo ta periexomena twn kleidiwn autwn einai {min}")

#kleisimo file
file.close()