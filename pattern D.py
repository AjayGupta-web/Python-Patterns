for row in range(6):
    for col in range(4):
        if ((row==0 or row==5) and (col!=3)) or ((col==0 or col==3) and (row!=0 and row!=5)):
            print('*',end=' ')
        else:
            print(end='  ')
    print()
