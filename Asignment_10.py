file = open("Tale_of_two_cities.txt", "r")
charactersList = []
#diabasma tou arxeiou character by character
for line in file:
    for character in line:
        #check if the numbers of ASCII are 7 bits in binary system
        if len(bin(ord(character))) == 9:
            charactersList.append(bin(ord(character)))


charactersString = ''
for i in range(len(charactersList)):
    #cut the 0b from all these numbers above
    charactersList[i] = charactersList[i][2:]
    #add in a string  all the first two and last two digits from all numbers
    charactersString +=  (charactersList[i][:2] + charactersList[i][5:]) 
    


#xwrisma tou parapanw string ana 16 bits kai prosthiki autwn se mia lista &convert to integers from binary system 
k = 0
integersList = []
totalNumbers = len(charactersString)//16
for i in range(totalNumbers):
    integersList.append(int(charactersString[k:k+16],2))
    k += 16


#ypologismos twn statistikwn
count_artioi = 0
count_3 = 0
count_5 = 0
count_7 = 0
for i in integersList:
    if i%2 == 0:
        count_artioi += 1
    if i%3 == 0:
        count_3 += 1
    if i%5 == 0:
        count_5 += 1
    if i%7 == 0:
        count_7 += 1
percent_a = count_artioi / totalNumbers * 100
percent_3 = count_3 / totalNumbers * 100
percent_5 = count_5 / totalNumbers * 100
percent_7 = count_7 / totalNumbers * 100

print("Ta statistika einai:\n")
print(f"To pososto twn arithmwn pou einai artioi einai {percent_a} %")
print(f"To pososto twn arithmwn pou diairountai me to 3 einai {percent_3} %")
print(f"To pososto twn arithmwn pou diairountai me to 5 einai {percent_5} %")
print(f"To pososto twn arithmwn pou diairountai me to 7 einai {percent_7} %")

#kleisimo file
file.close()




