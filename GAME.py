def Gamebord(xplayerList,yplayerList):
    # print(xplayerList)
    # print(yplayerList)
    zero = 'X' if xplayerList[0] else ('Y' if yplayerList[0] else 0)
    one = 'X' if xplayerList[1] else ('Y' if yplayerList[1] else 1)
    two = 'X' if xplayerList[2] else ('Y' if yplayerList[2] else 2)
    three = 'X' if xplayerList[3] else ('Y' if yplayerList[3] else 3)
    four = 'X' if xplayerList[4] else ('Y' if yplayerList[4] else 4)
    five = 'X' if xplayerList[5] else ('Y' if yplayerList[5] else 5)
    six = 'X' if xplayerList[6] else ('Y' if yplayerList[6] else 6)
    seven = 'X' if xplayerList[7] else ('Y' if yplayerList[7] else 7)
    eight = 'X' if xplayerList[8] else ('Y' if yplayerList[8] else 8)
    # print (zero)
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")
def checkWin(xplayerc,yplayerc):
    if (xplayerc[0] and xplayerc[1] and xplayerc[2]) or (xplayerc[3] and xplayerc[4] and xplayerc[5]) or (xplayerc[6] and xplayerc[7] and xplayerc[8]) or (xplayerc[0] and xplayerc[3] and xplayerc[6]) or (xplayerc[1] and xplayerc[4] and xplayerc[7]) or (xplayerc[2] and xplayerc[5] and xplayerc[8]) or (xplayerc[0] and xplayerc[4] and xplayerc[8]) or (xplayerc[2] and xplayerc[4] and xplayerc[6]):
        print("X Player Win")
        return 1
    elif(yplayerc[0] and yplayerc[1] and yplayerc[2]) or (yplayerc[3] and yplayerc[4] and yplayerc[5]) or (yplayerc[6] and yplayerc[7] and yplayerc[8]) or (yplayerc[0] and yplayerc[3] and yplayerc[6]) or (yplayerc[1] and yplayerc[4] and yplayerc[7]) or (yplayerc[2] and yplayerc[5] and yplayerc[8]) or (yplayerc[0] and yplayerc[4] and yplayerc[8]) or (yplayerc[2] and yplayerc[4] and yplayerc[6]):
        print("Y Player Win")
        return 1
    drawns=sum(xplayerc)+sum(yplayerc)
    if drawns==9:
        print("Game Draw")
        return 1
    else:
        # print (drawns)
        return -1




if __name__ == "__main__":
    xPlayer = [0,0,0,0,0,0,0,0,0]
    yPlayer = [0,0,0,0,0,0,0,0,0]
    turn = 1
    while(True):
        Gamebord(xPlayer,yPlayer)
        if turn==0:
            print("X's turn")
            xvlu=int(input())
            xPlayer[xvlu]=1
            turn=1
        else:
            print("Y's turn")
            yvlu=int(input())
            yPlayer[yvlu]=1
            turn=0
        win=checkWin(xPlayer,yPlayer)
        if win!=-1:
            print("Game Over")
            break
        # Gamebord(xPlayer,yPlayer)