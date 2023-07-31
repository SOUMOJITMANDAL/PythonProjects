def sum(a, b, c):
    return a + b + c
def printBoard(xState,zState):
    n0= 'X' if xState[0] else ('0' if zState[0] else 0)
    n1= 'X' if xState[1] else ('0' if zState[1] else 1)
    n2= 'X' if xState[2] else ('0' if zState[2] else 2)
    n3= 'X' if xState[3] else ('0' if zState[3] else 3)
    n4= 'X' if xState[4] else ('0' if zState[4] else 4)
    n5= 'X' if xState[5] else ('0' if zState[5] else 5)
    n6= 'X' if xState[6] else ('0' if zState[6] else 6)
    n7= 'X' if xState[7] else ('0' if zState[7] else 7)
    n8= 'X' if xState[8] else ('0' if zState[8] else 8)
    print(f" {n0} | {n1} | {n2} ")
    print(f"___|___|___")
    print(f" {n3} | {n4} | {n5} ")
    print(f"___|___|___")
    print(f" {n6} | {n7} | {n8} ")

def checkwin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 4], [1, 4, 7], [2, 5, 8]]
    for win in wins:
        if (sum(xState[win[0]], xState[win[1]], xState[win[2]] )== 3):
           print("X wins .")
           return 1
        if (sum(zState[win[0]], zState[win[1]], zState[win[2]] )== 3):
           print("Z wins .")
           return 0
    return -1



if __name__ ==  "__main__" :    # main function
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print(" Welcome to Tic Tac Toe ")
    while(True):
        printBoard(xState, zState)
        if(turn == 1):
            print("X's Chance")
            value = int(input("Please enter a value :"))
            xState[value] = 1
        else:
            print("Y's Chance")
            value = int(input("Please enter a value :"))
            zState[value] = 1
        cwin= checkwin(xState, zState)
        if (cwin != -1):
            print("Match over ")
            break
        turn = 1 - turn





