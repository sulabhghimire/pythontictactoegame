import os
import sys
def clear():
    os.system("cls")
def supHeader(firstPlayerName,secondPlayerName):
    print("\t\t\t\tPlayer One : {} \t\t\t Player Two : {}".format(firstPlayerName,secondPlayerName))
def header():
    print("\n\n\n")
    print("\t\t\t\t\t\t TICTACTOE ")
    print("\n\n")
def list():
    print("\t\t\t\t\t 1. New Game\n")
    print("\t\t\t\t\t 2. How To Play\n")
    print("\t\t\t\t\t 3. Credits\n")
    print("\t\t\t\t\t 4. Exit\n")
    print("\t\t\t\t\t Before starting new game go to how to play\n")
def navigation(taskNumber):
    print(taskNumber)
    if taskNumber == 1:
        playerDetails()
    elif taskNumber == 2:
        howToPlay()
    elif taskNumber == 3:
        cred()
    elif taskNumber == 4:
        sys.exit()
    else:
        secMainPage()
def mainPage():
    clear()
    header()
    list()
    task = int(input("\t\t\t\t\t Enter the task number : "))
    navigation(task)
def secMainPage():
    clear()
    header()
    list()
    print("\t\t\t\t\t Only use 1/2/3/4\n")
    task= int(input("\t\t\t\t\t Enter the task number : "))
    navigation(task)
def playerDetails():
    clear()
    header()
    firstPlayerName  = input("\t\t\t\t\t Input the name of first player  : ")
    secondPlayerName = input("\t\t\t\t\t Input the name of second player : ")
    dict = {'turn':0, 'key1':' ', 'key2':' ', 'key3':' ', 'key4':' ', 'key5':' ', 'key6':' ', 'key7':' ', 'key8':' ', 'key9':' '}
    newGame(dict,firstPlayerName,secondPlayerName)
def checkSign(kwargs,player,move):
    if move == 1 and player == 1:
        kwargs['key1'] = 'X'
    elif move == 2 and player == 1:
        kwargs['key2'] = 'X'
    elif move == 3 and player == 1:
        kwargs['key3'] = 'X'
    elif move == 4 and player == 1:
        kwargs['key4'] = 'X'
    elif move == 5 and player == 1:
        kwargs['key5'] = 'X'
    elif move == 6 and player == 1:
        kwargs['key6'] = 'X'
    elif move == 7 and player == 1:
        kwargs['key7'] = 'X'
    elif move == 8 and player == 1:
        kwargs['key8'] = 'X'
    elif move == 9 and player == 1:
        kwargs['key9'] = 'X'
    elif move == 1 and player == 2:
        kwargs['key1'] = 'O'
    elif move == 2 and player == 2:
        kwargs['key2'] = '0'
    elif move == 3 and player == 2:
        kwargs['key3'] = 'O'
    elif move == 4 and player == 2:
        kwargs['key4'] = 'O'
    elif move == 5 and player == 2:
        kwargs['key5'] = 'O'
    elif move == 6 and player == 2:
        kwargs['key6'] = 'O'
    elif move == 7 and player == 2:
        kwargs['key7'] = 'O'
    elif move == 8 and player == 2:
        kwargs['key8'] = 'O'
    elif move == 9 and player == 2:
        kwargs['key9'] = 'O'
def checkUseOfBox(steep,dict,player,firstPlayerName,secondPlayerName):
    check = 'key' + str(steep)
    if check not in dict.keys():
        newGame(dict,firstPlayerName,secondPlayerName)
    if dict[check]=='X' or dict[check]=='O':
        newGame(dict,firstPlayerName,secondPlayerName)
    else:
        dict['turn'] = dict['turn'] + 1
        checkSign(dict,player,steep)
def checkWin(dict,firstPlayerName,secondPlayerName):
    if dict['key1']=='X' and dict['key2']=='X' and dict['key3']=='X':
        results(1,firstPlayerName,secondPlayerName,dict)
    elif dict['key1'] == 'O' and dict['key2'] == 'O' and dict['key3'] == 'O':
        results(2,firstPlayerName,secondPlayerName,dict)
    elif dict['key4'] == 'O' and dict['key5'] == 'O' and dict['key6'] == 'O':
        results(2,firstPlayerName,secondPlayerName,dict)
    elif dict['key4'] == 'X' and dict['key5'] == 'X' and dict['key6'] == 'X':
        results(1,firstPlayerName,secondPlayerName,dict)
    elif dict['key7'] == 'O' and dict['key8'] == 'O' and dict['key9'] == 'O':
        results(2,firstPlayerName,secondPlayerName,dict)
    elif dict['key7'] == 'X' and dict['key8'] == 'X' and dict['key9'] == 'X':
        results(1,firstPlayerName,secondPlayerName,dict)
    elif dict['key1'] == 'O' and dict['key4'] == 'O' and dict['key7'] == 'O':
        results(2,firstPlayerName,secondPlayerName,dict)
    elif dict['key1'] == 'X' and dict['key4'] == 'X' and dict['key7'] == 'X':
        results(1,firstPlayerName,secondPlayerName,dict)
    elif dict['key2'] == 'O' and dict['key5'] == 'O' and dict['key8'] == 'O':
        results(2,firstPlayerName,secondPlayerName,dict)
    elif dict['key2'] == 'X' and dict['key5'] == 'X' and dict['key8'] == 'X':
        results(1,firstPlayerName,secondPlayerName,dict)
    elif dict['key3'] == 'O' and dict['key6'] == 'O' and dict['key9'] == 'O':
        results(2,firstPlayerName,secondPlayerName,dict)
    elif dict['key3'] == 'X' and dict['key6'] == 'X' and dict['key9'] == 'X':
        results(1,firstPlayerName,secondPlayerName,dict)
    elif dict['key1'] == 'O' and dict['key5'] == 'O' and dict['key9'] == 'O':
        results(2,firstPlayerName,secondPlayerName,dict)
    elif dict['key1'] == 'X' and dict['key5'] == 'X' and dict['key9'] == 'X':
        results(1,firstPlayerName,secondPlayerName,dict)
    elif dict['key7'] == 'O' and dict['key5'] == 'O' and dict['key3'] == 'O':
        results(2,firstPlayerName,secondPlayerName,dict)
    elif dict['key7'] == 'X' and dict['key5'] == 'X' and dict['key3'] == 'X':
        results(1,firstPlayerName,secondPlayerName,dict)
    elif ' ' in dict.values():
        newGame(dict,firstPlayerName,secondPlayerName)
    else:
        results(0,firstPlayerName,secondPlayerName,dict)
def results(playerTag,firstPlayerName,secondPlayerName,kwargs):
    if playerTag == 1:
        clear()
        header()
        print("\t\t\t\t\t\t    |     |    ")
        print("\t\t\t\t\t\t{}   |  {}  |  {}".format(kwargs['key7'], kwargs['key8'], kwargs['key9']))
        print("\t\t\t\t\t\t    |     |    ")
        print("\t\t\t\t\t\t---------------")
        print("\t\t\t\t\t\t    |     |    ")
        print("\t\t\t\t\t\t{}   |  {}  |  {}".format(kwargs['key4'], kwargs['key5'], kwargs['key6']))
        print("\t\t\t\t\t\t    |     |    ")
        print("\t\t\t\t\t\t---------------")
        print("\t\t\t\t\t\t    |     |    ")
        print("\t\t\t\t\t\t{}   |  {}  |  {}".format(kwargs['key1'], kwargs['key2'], kwargs['key3']))
        print("\t\t\t\t\t\t    |     |    ")
        secPlayer = playerTag
        print("\t\t\t\t\t\t Player {} is the winner.".format(firstPlayerName))
    elif playerTag == 2:
        clear()
        header()
        print("\t\t\t\t\t\t    |     |    ")
        print("\t\t\t\t\t\t{}   |  {}  |  {}".format(kwargs['key7'], kwargs['key8'], kwargs['key9']))
        print("\t\t\t\t\t\t    |     |    ")
        print("\t\t\t\t\t\t---------------")
        print("\t\t\t\t\t\t    |     |    ")
        print("\t\t\t\t\t\t{}   |  {}  |  {}".format(kwargs['key4'], kwargs['key5'], kwargs['key6']))
        print("\t\t\t\t\t\t    |     |    ")
        print("\t\t\t\t\t\t---------------")
        print("\t\t\t\t\t\t    |     |    ")
        print("\t\t\t\t\t\t{}   |  {}  |  {}".format(kwargs['key1'], kwargs['key2'], kwargs['key3']))
        print("\t\t\t\t\t\t    |     |    ")
        secPlayer = playerTag
        print("\t\t\t\t\t\t Player {} is the winner.".format(secondPlayerName))
    else:
        clear()
        header()
        print("\t\t\t\t\t\t    |     |    ")
        print("\t\t\t\t\t\t{}   |  {}  |  {}".format(kwargs['key7'], kwargs['key8'], kwargs['key9']))
        print("\t\t\t\t\t\t    |     |    ")
        print("\t\t\t\t\t\t---------------")
        print("\t\t\t\t\t\t    |     |    ")
        print("\t\t\t\t\t\t{}   |  {}  |  {}".format(kwargs['key4'], kwargs['key5'], kwargs['key6']))
        print("\t\t\t\t\t\t    |     |    ")
        print("\t\t\t\t\t\t---------------")
        print("\t\t\t\t\t\t    |     |    ")
        print("\t\t\t\t\t\t{}   |  {}  |  {}".format(kwargs['key1'], kwargs['key2'], kwargs['key3']))
        print("\t\t\t\t\t\t    |     |    ")
        secPlayer = playerTag
        print("\t\t\t\t\t\t The game was tied")
    choice = input("\t\t\t\t\t\t Do you want to play the game again (Y/N) : ")
    choice.lower()
    if choice=='y':
        choiceAgain = input("\t\t\t\t\t\t Do you both want to play as same player (Y/N) : ")
        choiceAgain.lower()
        if choiceAgain=='y':
            dict = {'turn': 0, 'key1': ' ', 'key2': ' ', 'key3': ' ', 'key4': ' ', 'key5': ' ', 'key6': ' ', 'key7': ' ', 'key8': ' ', 'key9': ' '}
            newGame(dict,firstPlayerName,secondPlayerName)
        elif choiceAgain=='n':
            playerDetails()
    elif choice=='n':
        mainPage()
    else:
        results(secPlayer,firstPlayerName,secondPlayerName,kwargs)
def newGame(kwargs,firstPlayerName,secondPlayerName):
    clear()
    supHeader(firstPlayerName,secondPlayerName)
    header()
    print("\t\t\t\t\t\t    |     |    ")
    print("\t\t\t\t\t\t{}   |  {}  |  {}".format(kwargs['key7'],kwargs['key8'],kwargs['key9']))
    print("\t\t\t\t\t\t    |     |    ")
    print("\t\t\t\t\t\t---------------")
    print("\t\t\t\t\t\t    |     |    ")
    print("\t\t\t\t\t\t{}   |  {}  |  {}".format(kwargs['key4'],kwargs['key5'],kwargs['key6']))
    print("\t\t\t\t\t\t    |     |    ")
    print("\t\t\t\t\t\t---------------")
    print("\t\t\t\t\t\t    |     |    ")
    print("\t\t\t\t\t\t{}   |  {}  |  {}".format(kwargs['key1'],kwargs['key2'],kwargs['key3']))
    print("\t\t\t\t\t\t    |     |    ")
    if kwargs['turn']==0 or (kwargs['turn'])%2 == 0 :
        move = int(input("\t\t\t\t\t\tEnter the move {} : ".format(firstPlayerName)))
        player = 1
    else:
        move = int(input("\t\t\t\t\t\tEnter the move {} : ".format(secondPlayerName)))
        player = 2
    checkUseOfBox(move,kwargs,player,firstPlayerName,secondPlayerName)
    checkWin(kwargs,firstPlayerName,secondPlayerName)
def howToPlay():
    clear()
    header()
    print("\t\t\t     |       |     ")
    print("\t\t\t  7  |   8   |   9 ")
    print("\t\t\t     |       |     ")
    print("\t\t\t--------------------")
    print("\t\t\t     |       |     ")
    print("\t\t\t  4  |   5   |   6 ")
    print("\t\t\t     |       |     ")
    print("\t\t\t--------------------")
    print("\t\t\t     |       |     ")
    print("\t\t\t  1  |   2   |   3 ")
    print("\t\t\t     |       |     ")
    print("\t\t\tThe numbering system is shown as above.")
    print("\t\t\tWays to play the Game : ")
    print("\t\t\t-- The first player will always get X.")
    print("\t\t\t-- The second player will always get O.")
    print("\t\t\t-- As shown in above figure press only that specific number where you want to mark.")
    print("\t\t\t-- Once marked can't be remarked again.\n\n")
    input("\t\t\tPress  any key to go back to main page ..")
    mainPage()
def cred():
    clear()
    header()
    print("\t\t\t\t\t Credits \n\n")
    print("\t\t\t\t\t Game Name  : Tictactoe\n")
    print("\t\t\t\t\t Developer  : Sulabh Ghimire\n")
    print("\t\t\t\t\t Start Date : 2076/08/22\n")
    print("\t\t\t\t\t Completed  : 2076/08/23\n")
    input("\t\t\t\t\t Press Any Key to go back !!")
    mainPage()
mainPage()

