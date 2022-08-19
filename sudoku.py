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
def unikatyPiony(mozliwosci):# sprawdza czy jakaś możliwość w komórce może być jedyną taką wartością w pionie - jeśli tak to wpisuje ją na sztywno jako jedyną możliwość
    piony=czytajPiony(mozliwosci)
    for x in range(0,len(piony)):#dla każdego pionu
        roznica=[None]*9# pusta tablica do wyłapania pojedynczej wartości
        for i in range(0,len(piony[x])):
            temp=[] #tablica która przechowuje wartości z komórek poza tą w której się znajdujemy
            for j in range(0,len(piony[x])):
                if i!=j:
                    temp.extend(piony[x][j])
            #list(set(piony[x][i])-set(temp)) - sprawdza możliwości na konkretnym miejscu w pionie i odejmuje od nich pozostałe możliwości w pionie - różnica zostaje zapisana
            if roznica[i]==None: 
                roznica[i]=list(set(piony[x][i])-set(temp)) 
            #else:
            #    roznica[i].append(list(set(piony[x][i])-set(temp)))   #else chyba nigdy się nie wykona
        #jesli różnica to pojedyncza wartość to zostaje potraktowana jako jedyna możliwość
        for i in range(0,len(piony[x])):
            if len(roznica[i])==1:
                mozliwosci[i][x]=roznica[i]
    return mozliwosci
def unikatyPoziomy(mozliwosci):#kopia unikatyPiony tylko, że dla poziomów
    poziomy=czytajPoziomy(mozliwosci)
    for x in range(0,len(poziomy)):#
        roznica=[None]*9
        for i in range(0,len(poziomy[x])):
            temp=[] 
            for j in range(0,len(poziomy[x])):
                if i!=j:
                    temp.extend(poziomy[x][j])
            if roznica[i]==None: 
                roznica[i]=list(set(poziomy[x][i])-set(temp)) 
        for i in range(0,len(poziomy[x])):
            if len(roznica[i])==1:
                mozliwosci[x][i]=roznica[i]
    return mozliwosci

def probujemy(sudoku):
    licznik=0
    flaga=False
    while flaga==False:
        licznik+=1
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
        #unikaty wywolujemy przed żeby można było 
        mozliwosci=unikatyPiony(mozliwosci)
        mozliwosci=unikatyPoziomy(mozliwosci)
        #wyłapywanie pojedynczych wartości i wpisanie ich do rozwiazania sudoku
        for i in range(0,9):
            for j in range(0,9):
                if len(mozliwosci[i][j])==1:
                    sudoku[i][j]=mozliwosci[i][j][0]
                    mozliwosci[i][j].pop(0)
        drukujSudoku(sudoku)
        flaga=sprawdzSudoku(sudoku)
    #drukujSudoku(mozliwosci)
    print(licznik)
    return sudoku


"""
sudoku= [[0,3,0,0,0,6,7,5,1],
        [0,4,7,2,0,8,0,0,0],
        [6,0,0,7,0,0,0,0,2],
        [7,0,0,0,0,0,0,3,0],
        [4,0,9,5,0,1,2,0,0],
        [0,1,6,8,0,0,0,0,0],
        [0,6,5,0,0,0,8,0,9],
        [9,0,4,0,0,0,0,0,7],
        [0,0,0,0,6,0,0,0,0]]"""
sudoku= [[0,4,0,8,0,0,0,0,6],
        [0,0,1,0,0,6,0,0,3],
        [0,0,6,3,4,9,8,0,0],#4 dodane
        [2,5,0,6,0,3,0,0,0],
        [0,0,0,0,0,7,0,0,0],#7dodane
        [0,8,7,0,0,0,0,4,2],#2dodane
        [0,0,0,0,9,8,7,0,0],#8 dodane
        [0,0,0,0,0,4,0,1,0],
        [0,0,0,0,0,2,0,0,5]]
#drukujSudoku(sudoku)
#sprawdzSudoku(sudoku)
drukujSudoku(sudoku)
sudoku1=probujemy(sudoku)