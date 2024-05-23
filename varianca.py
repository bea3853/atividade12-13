import statistics

def varianca(lista):
    varianca_1 = statistics.variance(lista)
    print(f'Variança das notas:, {varianca_1:.2f}' )
    return varianca_1
