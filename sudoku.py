# Tutaj pisz swój kod, młody padawanie ;-)
def drukujSudoku(sudoku):
    for i in range(0,len(sudoku)):
        if i%3==0:
            print('- - - - - - - - - - - - - - -')
        for j in range (0,len(sudoku[i])):
            if j%3==0:
                print('|',end='')
            print(' '+str(sudoku[i][j])+' ', end='')
        print('|')
def czytajKwadraty(sudoku):
    kwadraty=[[],[],[],[],[],[],[],[],[]]
    for i in range(0,len(sudoku)):
        temp=i//3
        for j in range(0,len(sudoku)):
            if j==3 or j==6: #zwiększenie temp o 3 żeby poprawnie umieścić wartość w tablicy kwadratów
                temp+=3
            kwadraty[temp].append(sudoku[i][j])
    return kwadraty
def sprawdzKwadraty(kwadraty):
    for kwadrat in kwadraty:
        kwadrat.sort()
    for kwadrat in kwadraty:
    #sprawdza posortowany kwadrat czy wartości są od 1 do 9
        for i in range(1,10):
            if i!=kwadrat[i-1]:
                return False
    return True
def czytajPoziomy(sudoku):
    poziomy=[[],[],[],[],[],[],[],[],[]]
    for i in range(0,len(sudoku)):
        for j in range(0,len(sudoku)):
            poziomy[i].append(sudoku[i][j])
    return poziomy
def sprawdzPoziomy(poziomy):
    for poziom in poziomy:
        poziom.sort()
    for poziom in poziomy:
        for i in range(1,10):
            if i!=poziom[i-1]:
                return False
    return True
def czytajPiony(sudoku):
    piony=[[],[],[],[],[],[],[],[],[]]
    for i in range(0,len(sudoku)):
        for j in range(0,len(sudoku)):
            piony[j].append(sudoku[i][j])
    return piony
def sprawdzPiony(piony): 
    for pion in piony:
        pion.sort()
    for pion in piony:
        for j in range(1,10):
            if j!=pion[j-1]:
                return False
    return True
def sprawdzSudoku(sudoku):
    kwadraty=czytajKwadraty(sudoku)
    sprKwadraty=sprawdzKwadraty(kwadraty)
    piony=czytajPiony(sudoku)
    sprPiony=sprawdzPiony(piony)
    poziomy=czytajPoziomy(sudoku)
    sprPoziomy=sprawdzPoziomy(poziomy)
    if sprKwadraty and sprPiony and sprPoziomy:
        print('zajebiscie mordo')
        return True
    else:
        print('sory winetu')
        return False
def probujemy(sudoku):
    licznik=False
    while licznik==False:
        mozliwosci=[[[],[],[],[],[],[],[],[],[]],
                   [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]]]
        kwadraty=czytajKwadraty(sudoku)
        piony=czytajPiony(sudoku)
        poziomy=czytajPoziomy(sudoku)
        #print(poziomy)
        #print(piony)
        #print(kwadraty)
        for i in range(0,9):
            temp=i//3
            for j in range(0,9):
                if j==3 or j==6: #zwiększenie temp o 3 żeby poprawnie umieścić kwadrat w tablicy
                    temp+=3
                if sudoku[i][j]==0:
                    for liczba in range(1,10):
                        if liczba not in poziomy[i] and liczba not in piony[j] and liczba not in kwadraty[temp]:
                            mozliwosci[i][j].append(liczba)
        drukujSudoku(mozliwosci)
        for i in range(0,9):
            for j in range(0,9):
                if len(mozliwosci[i][j])==1:
                    sudoku[i][j]=mozliwosci[i][j][0]
                    mozliwosci[i][j].pop(0)
        
        drukujSudoku(sudoku)
        licznik=sprawdzSudoku(sudoku)
    drukujSudoku(mozliwosci)
    return sudoku


"""
sudoku= [[2,1,9,5,4,3,6,7,8],
        [5,4,3,8,7,6,9,1,2],
        [8,7,6,2,1,9,3,4,5],
        [4,3,2,7,6,5,8,9,1],
        [7,6,5,1,9,8,2,3,4],
        [1,9,8,4,3,2,5,6,7],
        [3,2,1,6,5,4,7,8,9],
        [6,5,4,9,8,7,1,2,3],
        [9,8,7,3,2,1,4,5,6]]
        """
"""
sudoku= [[2,0,9,0,0,0,6,0,0],
        [0,4,0,8,7,0,0,1,2],
        [8,0,0,0,1,9,0,4,0],
        [0,3,0,7,0,0,8,0,1],
        [0,6,5,0,0,8,0,3,0],
        [1,0,0,0,3,0,0,0,7],
        [0,0,0,6,5,0,7,0,9],
        [6,0,4,0,0,0,0,2,0],
        [0,8,0,3,0,1,4,5,0]]
        """
"""
sudoku= [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]
        """
sudoku= [[0,3,0,0,0,6,7,5,1],
        [0,4,7,2,0,8,0,0,0],
        [6,0,0,7,0,0,0,0,2],
        [7,0,0,0,0,0,0,3,0],
        [4,0,9,5,0,1,2,0,0],
        [0,1,6,8,0,0,0,0,0],
        [0,6,5,0,0,0,8,0,9],
        [9,0,4,0,0,0,0,0,7],
        [0,0,0,0,6,0,0,0,0]]
#drukujSudoku(sudoku)
#sprawdzSudoku(sudoku)
drukujSudoku(sudoku)
sudoku1=probujemy(sudoku)