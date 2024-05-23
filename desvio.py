import statistics

def desvio(lista):
    desvio_p = statistics.median(lista)
    print('Desvio Padrão das notas:', desvio_p )
    return desvio_p
