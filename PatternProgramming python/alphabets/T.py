#Printing Alphabent 'T'
for row in range(7):
    for col in range(5):
        if(row == 0 and col in {0,1,2,3,4}):
            print('*',end=' ')
        elif(col == 2 and row in {1,2,3,4,5,6}):
            print('*',end=' ')
        else:
            print('  ',end='')
    print()