import random


choice = '1'
while choice != '0': 
    print('''
        If you want to see 21 results with the defualt way press 1.\n
    Otherwise If you want to see 21 results with the special way press 2
    ''')
    option = input('Please select: ')
    #deafault way
    if option == '1':
        count_1 = 0
        count_2 = 0
        count_d = 0
        for i in range (100):
            xartia = []
            figures = ["J", "Q", "K"]
            xarti = [i for i in range(1, 11)] + figures
            color = ["H", "S", "C", "D"]
            for i in xarti:
                for j in color:
                    xartia.append([i,j])
            random.shuffle(xartia)
            player1=[]
            sum1=0
            while sum1<16:
                sum1=0
                player1.append(xartia.pop())
                for card in player1:
                    if card[0] in figures:
                        sum1=sum1+10
                    else:
                        sum1=sum1+card[0]
                
            if sum1>21:
                #P2 wins
                count_2 += 1 
            else:
                #P2 joins the game
                player2=[]
                sum2=0
                while sum2<16:
                    sum2=0
                    player2.append(xartia.pop())
                    for card in player2:
                        if card[0] in figures:
                            sum2=sum2+10
                        else:
                            sum2=sum2+card[0]
                    
                if sum2>21:
                    sum2=0
                if sum1>sum2:
                    #P1 wins
                    count_1 += 1 
                elif sum2>sum1:
                    #P2 wins
                    count_2 += 1
                else:
                    #draw
                    count_d += 1
        print('defualt way')
        print()
        print(f"The player 1 won {count_1} times!")
        print(f"The player 2 won {count_2} times!")
        print(f"The match it was draw {count_d} times!")


    #special way
    elif option == '2':

        count_1 = 0
        count_2 = 0
        count_d = 0
        for i in range (100):
            xartia = []
            figures = ["J", "Q", "K"]
            xarti = [i for i in range(1, 11)] + figures
            color = ["H", "S", "C", "D"]
            for i in xarti:
                for j in color:
                    xartia.append([i,j])
            random.shuffle(xartia)
            player1=[]
            sum1=0
            k = 0
            while sum1<16:
                sum1=0
                #moirasma xartiwn ston p1 xekinwntas me figura h me 10
                if k == 0:
                    a = 0
                    #check mexri na uparxei figura h 10
                    for filo in xartia:
                        if (xartia[a][0] == figures[0]) or (xartia[a][0] == figures[1]) or (xartia[a][0] == figures[2]) or (xartia[a][0] == 10):
                            player1.append(xartia[a])
                            xartia.remove(xartia[a])
                            break
                        a += 1
                # print (player1)
                else:
                    player1.append(xartia.pop()) 
                    
                for card in player1:
                    if card[0] in figures:
                        sum1=sum1+10
                    else:
                        sum1=sum1+card[0]
                    
                k += 1
            if sum1>21:
                #P2 wins
                count_2 += 1 
            else:
                #P2 joins the game
                player2=[]
                sum2=0
                k = 0
                while sum2<16:
                    sum2=0
                    #moirasma xartiwn ston p2 xekinwntas me otidhpote allo ektos apo figura h 10
                    if k == 0:
                        a = 0
                        #check mexri na mhn uparxei figura h 10
                        for filo in xartia:
                            if (xartia[a][0] != figures[0]) and (xartia[a][0] != figures[1]) and (xartia[a][0] != figures[2]) and (xartia[a][0] != 10):
                                player2.append(xartia[a])
                                xartia.remove(xartia[a])
                                break
                            a += 1          
                    else:
                        player2.append(xartia.pop())    
                    for card in player2:
                        if card[0] in figures:
                            sum2=sum2+10
                        else:
                            sum2=sum2+card[0]
                if sum2>21:
                    sum2=0
                if sum1>sum2:
                    #P1 wins
                    count_1 += 1 
                elif sum2>sum1:
                    #P2 wins
                    count_2 += 1
                else:
                    #draw
                    count_d += 1
        print('special way')
        print()
        print(f"The player 1 won {count_1} times!")
        print(f"The player 2 won {count_2} times!")
        print(f"The match it was draw {count_d} times!")
    
    print('If you want to quit the programm press 0. Otherwise press whatever number you want (no 0)')
    choice = input()