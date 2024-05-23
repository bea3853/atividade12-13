# Desafio 1
# VOCÊ É UM DEV E PRECISA CRIAR UM SISTEMA PARA UMA ESCOLA. 
# SISTEMA DE NOTAS DE ALUNOS QUE MOSTRE COM ESTATISTICA A MODA E A MEDIA, VARIANÇA E DESVIO DE PADRÃO, DAS NOTAS DE ALUNOS DE UM COLÉGIO, ALÉM DE MOSTRAR MENOR E A  MAIOR NOTA, SEPARE EM FUNÇÕES DIFERENTES 
# 1 -  ***VOCÊ CRIAR SEUS PRÓPRIOS MÓDULOS***
# 2 - ***OU USAR STATISTICS ****

from media import media
from varianca import varianca
from moda import moda 
from mediana import mediana
from desvio import desvio



def main():
    n1 = float(input('Nota 1'))
    n2 = float(input('Nota 2'))
    n3 = float(input('Nota 3'))
    n4 = float(input('Nota 4'))
    n5 = float(input('Nota 5'))
    n6 = float(input('Nota 6'))
    n7 = float(input('Nota 7'))
    n8 = float(input('Nota 8'))
    n9 = float(input('Nota 9'))
    n10 = float(input('Nota 10'))

    #lista vazia
    lista_notas = []

    # lista_notas += (n1,n2,n3,n4,n5, n6,)  
    # adicionar varios indices de uma vez na lista

    lista_notas.extend((n1,n2,n3,n4,n5, n6,n7,n8,n9,n10))
    print(lista_notas)
    varianca(lista_notas)
    media(lista_notas)
    moda(lista_notas)
    desvio(lista_notas)
    mediana(lista_notas)

    




main()