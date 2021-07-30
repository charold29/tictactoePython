#tablero vacio
board =[[filas for filas in range(3)] for columnas in range(3)]

#valores iniciales
board[0][0] = 1
board[0][1] = 2
board[0][2] = 3
board[1][0] = 4
board[1][1] = 'X'
board[1][2] = 6
board[2][0] = 7
board[2][1] = 8
board[2][2] = 9
        
#Estados : 0 ejecutado 7 terminado

def DisplayBoard(eBoard):
    if eBoard == 0:
        
        for columnas in board:
            print('\n+-------+-------+-------+',end='')
            print('\n|       |       |       |\n|',end='')
            
            for filas in columnas:
                print('  ',filas,'  |',end='')

            print('\n|       |       |       |',end='')
        print('\n+-------+-------+-------+',)

def MakeListOfFreeFields(eBoard):

    if eBoard == 0:
        cuadrosVacios = []
        for columna in board:
            for n in columna:
                if type(n)==int:
                    cuadrosVacios.append((board.index(columna),columna.index(n)))
    return cuadrosVacios

def ListaNumerosLibres():
    numeros = []
    for columna in board:
            for n in columna:
                if type(n)==int:
                    numeros.append(n)
    return numeros

def DrawMove(eBoard):
    from random import randrange
    if eBoard != 7:
        
        listaRandom = []

        for i in range(100):
            listaRandom.append(randrange(1,10))

        listaRandomSinRepetir = []

        for num in listaRandom:
            if num not in listaRandomSinRepetir:
                listaRandomSinRepetir.append(num)
        
        libres = MakeListOfFreeFields(eBoard)

        listaRandomSinRepetir.remove(5) 

        for n in listaRandomSinRepetir:
            print(n)
            for x in libres:
                if n == board[x[0]][x[1]]:
                    board[x[0]][x[1]] = 'X'
            break
        
    print('Randoms',listaRandomSinRepetir)
    DisplayBoard(eBoard)

def DrawMove2(eBoard):
    from random import randrange
    if eBoard != 7:
        
        libres = MakeListOfFreeFields(eBoard)
        numLibres = ListaNumerosLibres()
        nRandom = randrange(len(numLibres))
        mov = numLibres[nRandom]
        for x in libres:
            if mov == board[x[0]][x[1]]:
                print('Maquina elige: ',mov)
                board[x[0]][x[1]] = 'X'
                
    DisplayBoard(eBoard)

def EnterMove(eBoard):
    if eBoard != 7:
        numLibres = ListaNumerosLibres()
        
        mov = int(input("Ingresa tu movimiento: "))
        while mov not in numLibres:
            print('No puede hacer ese movimiento')
            mov = int(input("Ingresa tu movimiento: "))
            

        libres = MakeListOfFreeFields(eBoard)
        for x in libres:
            if mov == board[x[0]][x[1]]:
                board[x[0]][x[1]] = 'O'
            

    DisplayBoard(eBoard)

def VictoryFor():
    eList = [] #lista de evaluacion
    for tablero in board:
        for c in tablero:
            eList.append(c)

    cont=0
    for columna in board:
        for n in columna:
            if type(n)!=int:
                cont+=1

    if eList[0]==eList[1]==eList[2]:
        return eList[0]
    if eList[0]==eList[3]==eList[6]:
        return eList[0]
    if eList[6]==eList[7]==eList[8]:
        return eList[6]
    if eList[2]==eList[5]==eList[8]:
        return eList[2]
    if eList[0]==eList[4]==eList[8]:
        return eList[0]
    if eList[2]==eList[4]==eList[6]:
        return eList[2]
    if eList[1]==eList[4]==eList[7]:
        return eList[1]
    if eList[3]==eList[4]==eList[5]:
        return eList[3]
    
    if cont==9:
        return 'Empate'
    else:
        return 0

estado = 0 # ejecutado

DisplayBoard(estado) # Tablero inicial sin cambios
while(VictoryFor()==0):
    EnterMove(estado)
    if VictoryFor()!=0:
        print('Han ganado las',VictoryFor())
        break
    DrawMove2(estado)
    if VictoryFor()!=0:
        print('Han ganado las',VictoryFor())
        break