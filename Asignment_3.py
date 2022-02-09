file = open("Tale_of_two_cities.txt", "r")
charactersList = []
wordsList = []
#diabasma tou arxeiou character by character
for line in file:
    cleanString = ''
    isEmpty = False
    for character in line:
        # check and save the character space
        if ord(character) == 32:
            cleanString += character
        #check and save all the characters a-z & A-Z
        if (ord(character) >= 65 and ord(character) <= 90) or (ord(character) >= 97 and ord(character) <= 122):
           cleanString += character
           isEmpty = True
    if isEmpty == False:
        continue
    #split the string by the space
    words = cleanString.split(' ')
    #add into a list all the words of the file
    for word in words:
        if word != '':
            wordsList.append(word) 


#find the max length of the word in the list
maxl = len(wordsList[0])
for i in range(1,len(wordsList)):
    if maxl < len(wordsList[i]):
        maxl = len(wordsList[i])

#δημιουργία 2d list για τις λέξεις ομαδοποιημένες κατά το μέγεθος τους
CountLenWordsList = []
for i in range(maxl):
    column = []
    for j in wordsList:
        if len(j) == i+1:
            column.append(j)
    CountLenWordsList.append(column)
totalWords = len(wordsList)    
wordsList.clear()

#add all the words in a list where these words will delete from the general list with the words
#prokeitai gia tis lexeis pou to athroisma twn grammatwn tous einai 20
for i in range(10):
    rem = []  
    k = 0
    index = 20 - (i + 2)
    for j in CountLenWordsList[i]:
        if i != 9:
            if len(CountLenWordsList[index]) - 1 >= k:
                if (len(j) + len(CountLenWordsList[index][k])) == 20: 
                    rem.append(j)
                    rem.append(CountLenWordsList[index][k])
            else:
                break   
        else:
            if len(CountLenWordsList[i])%2 == 0:
               rem.append(CountLenWordsList[i])
               break
            else:
                rem.append(CountLenWordsList[i])
                for y in range(len(CountLenWordsList[i])%2):
                    rem.remove(CountLenWordsList[i][y])       
        k += 1
    c = 0
    #removing all that words where there are in the rem list from the general list 
    for l in rem:
        if i != 9:
            if c % 2 == 0:
                CountLenWordsList[i].remove(l)
            else:
                CountLenWordsList[18 - i].remove(l)
        else:
            if len(CountLenWordsList[i])%2 == 0:
                CountLenWordsList[i].clear()
            else:
                CountLenWordsList[i].remove(l)
        c += 1


#ypologismos twn zeugariwn lexewn pou diagrafthkan synolika
remainingWords = 0
for i in range(maxl):
  remainingWords += len(CountLenWordsList[i])

pairs = (totalWords - remainingWords) // 2
print(f"Diagrafthkan {pairs} zeugaria lexewn\n")

#anakoinwsh twn statistikwn twn lexewn pou paremeinan
for i in range(maxl):
    if i + 1 == 1:
       print(f"{len(CountLenWordsList[i])} lexeis me 1 gramma")
    elif len(CountLenWordsList[i]) != 0:
        print(f"{len(CountLenWordsList[i])} lexeis me {i + 1} grammata")

#kleisimo file  
file.close()