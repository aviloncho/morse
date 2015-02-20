#Programa para transformar texto a codigo morse.
# -*- coding: utf-8 -*-

def fileMayus(pFileName):
    #Read each line of pFile parameter to save in mayus to mayus file
    with open('fuente.txt', 'w') as mayus:
        with open(pFileName, 'r') as lFile:
            line = lFile.readline()
            while line != '':
                mayus.write(line.upper())
                line = lFile.readline()

def countCaractersInFile(pFileName):
    #Inicialize variables to count
    lCntPal = 0
    lCntVoc = 0
    lCntCon = 0
    lCntDig = 0

    with open(pFileName, 'r') as lFile:
        with open('totales.txt', 'w') as TotFile:
            line = lFile.readline()
            while line != '':
                TotFile.write(line)
                lCntPal += len(line.split(' '))
                for i in range(0, len(line)):
                    if (line[i] == 'A') | (line[i] == 'E') | (line[i] == 'I') | (line[i] == 'O') | (line[i] == 'U'):
                        lCntVoc += 1
                    elif (line[i] == '0') | (line[i] == '1') | (line[i] == '2') | (line[i] == '3') | (line[i] == '4') | (line[i] == '5') | (line[i] == '6') | (line[i] == '7') | (line[i] == '8') | (line[i] == '9'):
                        lCntDig += 1
                    elif (line[i] == 'B') | (line[i] == 'C') | (line[i] == 'D') | (line[i] == 'F') | (line[i] == 'G') | (line[i] == 'H') | (line[i] == 'J') | (line[i] == 'K') | (line[i] == 'L') | (line[i] == 'M') | (line[i] == 'N') | (line[i] == 'Ñ') | (line[i] == 'P') | (line[i] == 'Q') | (line[i] == 'R') | (line[i] == 'S') | (line[i] == 'T') | (line[i] == 'V') | (line[i] == 'W') | (line[i] == 'X') | (line[i] == 'Y') | (line[i] == 'Z'):
                        lCntCon += 1
                line = lFile.readline()
            TotFile.write('\nCANTIDAD DE PALABRAS: '+str(lCntPal))
            TotFile.write('\nCANTIDAD DE VOCALES: '+str(lCntVoc))
            TotFile.write('\nCANTIDAD DE CONSONANTES: '+str(lCntCon))
            TotFile.write('\nCANTIDAD DE DIGITOS NUMERICOS: '+str(lCntDig))

fileMayus('original.txt')
countCaractersInFile('fuente.txt')
