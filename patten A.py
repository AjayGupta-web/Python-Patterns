for a in range(5):
    for b in range(10):
        if (a==0 and b==5) or (a==1 and (b==4 or b==6)) or (a==2 and (b==3 or b==4 or b==5 or b==6 or b==7) or (a==3 and (b==2 or b==8) or (a==4 and (b==1 or b==9)))):
            print('*',end='')
        else:
            print(end=' ')
    print()

    