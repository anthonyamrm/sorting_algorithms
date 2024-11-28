import time
import csv
import os
import random
import statistics

def gerar_lista_aleatoria(tamanho):
    return random.sample(range(tamanho * 10), tamanho)

def calcular_desvio_padrao(tempos):
    return statistics.stdev(tempos)

def insertionSort(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
    return arr


def main1():


    tempo_bucket = []
    aux = 0
    soma = 0
    sorted_list = []

    # Rodar o código 5 vezes, mas considerar apenas as últimas 4 execuções
    while aux != 5:
        vetor_500 = gerar_lista_aleatoria(500)
        print(vetor_500[:10])
        copy = vetor_500.copy()

        # Começa a contagem do tempo
        start = time.perf_counter()
        sorted_list = insertionSort(copy)
        end = time.perf_counter()

        # Adicionar o tempo de execução apenas se não for a primeira iteração
        
        tempo_bucket.append(1000*(end - start))


        aux += 1

    print('SORTED LIST (última execução):')
    print(sorted_list)

    # Calculando a média do tempo de execução considerando apenas as 4 últimas iterações
    soma = sum(tempo_bucket)
    media = soma / len(tempo_bucket)
    desvio = calcular_desvio_padrao(tempo_bucket)

    # Escrevendo os tempos de execução no arquivo CSV
    with open("insertion_500.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["insertion_500: "])  # Cabeçalho
        for valor in tempo_bucket:
            escritor.writerow([valor])
        escritor.writerow(["Média do tempo de execução:", media])
        escritor.writerow(["Desvio padrão do tempo de execução:", desvio])

def main2():
    

    tempo_bucket = []
    aux = 0
    soma = 0
    sorted_list = []

    # Rodar o código 5 vezes, mas considerar apenas as últimas 4 execuções
    while aux != 5:
        vetor_1000 = gerar_lista_aleatoria(1000)
        print(vetor_1000[:10])
        copy = vetor_1000.copy()

        # Começa a contagem do tempo
        start = time.perf_counter()
        sorted_list = insertionSort(copy)
        end = time.perf_counter()

        # Adicionar o tempo de execução apenas se não for a primeira iteração
        
        tempo_bucket.append(1000*(end - start))

        aux += 1

    print('SORTED LIST (última execução):')
    print(sorted_list)

    # Calculando a média do tempo de execução considerando apenas as 4 últimas iterações
    soma = sum(tempo_bucket)
    media = soma / len(tempo_bucket)
    desvio = calcular_desvio_padrao(tempo_bucket)

    # Escrevendo os tempos de execução no arquivo CSV
    with open("insertion_1000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["insertion_1000: "])  # Cabeçalho
        for valor in tempo_bucket:
            escritor.writerow([valor])
        escritor.writerow(["Média do tempo de execução:", media])
        escritor.writerow(["Desvio padrão do tempo de execução:", desvio])

def main3():

    tempo_bucket = []
    aux = 0
    soma = 0
    sorted_list = []

    # Rodar o código 5 vezes, mas considerar apenas as últimas 4 execuções
    while aux != 5:
        vetor_5000 = gerar_lista_aleatoria(5000)
        print(vetor_5000[:10])
        copy = vetor_5000.copy()

        # Começa a contagem do tempo
        start = time.perf_counter()
        sorted_list = insertionSort(copy)
        end = time.perf_counter()

        # Adicionar o tempo de execução apenas se não for a primeira iteração
        
        tempo_bucket.append(1000*(end - start))

        aux += 1

    print('SORTED LIST (última execução):')
    print(sorted_list)

    # Calculando a média do tempo de execução considerando apenas as 4 últimas iterações
    soma = sum(tempo_bucket)
    media = soma / len(tempo_bucket)
    desvio = calcular_desvio_padrao(tempo_bucket)

    # Escrevendo os tempos de execução no arquivo CSV
    with open("insertion_5000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["insertion_5000: "])  # Cabeçalho
        for valor in tempo_bucket:
            escritor.writerow([valor])
        escritor.writerow(["Média do tempo de execução:", media])
        escritor.writerow(["Desvio padrão do tempo de execução:", desvio])

def main4():

    tempo_bucket = []
    aux = 0
    soma = 0
    sorted_list = []

    # Rodar o código 5 vezes, mas considerar apenas as últimas 4 execuções
    while aux != 5:
        vetor_30000 = gerar_lista_aleatoria(30000)
        print(vetor_30000[:10])
        copy = vetor_30000.copy()

        # Começa a contagem do tempo
        start = time.perf_counter()
        sorted_list = insertionSort(copy)
        end = time.perf_counter()

        # Adicionar o tempo de execução apenas se não for a primeira iteração
        
        tempo_bucket.append(1000*(end - start))

        aux += 1

    print('SORTED LIST (última execução):')
    print(sorted_list)

    # Calculando a média do tempo de execução considerando apenas as 4 últimas iterações
    soma = sum(tempo_bucket)
    media = soma / len(tempo_bucket)
    desvio = calcular_desvio_padrao(tempo_bucket)

    # Escrevendo os tempos de execução no arquivo CSV
    with open("insertion_30000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["insertion_30000: "])  # Cabeçalho
        for valor in tempo_bucket:
            escritor.writerow([valor])
        escritor.writerow(["Média do tempo de execução:", media])
        escritor.writerow(["Desvio padrão do tempo de execução:", desvio])

def main5():
    

    tempo_bucket = []
    aux = 0
    soma = 0
    sorted_list = []

    # Rodar o código 5 vezes, mas considerar apenas as últimas 4 execuções
    while aux != 5:
        vetor_80000 = gerar_lista_aleatoria(80000)
        print(vetor_80000[:10])
        copy = vetor_80000.copy()

        # Começa a contagem do tempo
        start = time.perf_counter()
        sorted_list = insertionSort(copy)
        end = time.perf_counter()

        # Adicionar o tempo de execução apenas se não for a primeira iteração
        
        tempo_bucket.append(1000*(end - start))

        aux += 1

    print('SORTED LIST (última execução):')
    print(sorted_list)

    # Calculando a média do tempo de execução considerando apenas as 4 últimas iterações
    soma = sum(tempo_bucket)
    media = soma / len(tempo_bucket)
    desvio = calcular_desvio_padrao(tempo_bucket)

    # Escrevendo os tempos de execução no arquivo CSV
    with open("insertion_80000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["insertion_80000: "])  # Cabeçalho
        for valor in tempo_bucket:
            escritor.writerow([valor])
        escritor.writerow(["Média do tempo de execução:", media])
        escritor.writerow(["Desvio padrão do tempo de execução:", desvio])

def main6():

    tempo_bucket = []
    aux = 0
    soma = 0
    sorted_list = []

    # Rodar o código 5 vezes, mas considerar apenas as últimas 4 execuções
    while aux != 5:
        vetor_100000 = gerar_lista_aleatoria(100000)
        print(vetor_100000[:10])
        copy = vetor_100000.copy()

        # Começa a contagem do tempo
        start = time.perf_counter()
        sorted_list = insertionSort(copy)
        end = time.perf_counter()

        # Adicionar o tempo de execução apenas se não for a primeira iteração
        
        tempo_bucket.append(1000*(end - start))

        aux += 1

    print('SORTED LIST (última execução):')
    print(sorted_list)

    # Calculando a média do tempo de execução considerando apenas as 4 últimas iterações
    soma = sum(tempo_bucket)
    media = soma / len(tempo_bucket)
    desvio = calcular_desvio_padrao(tempo_bucket)

    # Escrevendo os tempos de execução no arquivo CSV
    with open("insertion_100000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["insertion_100000: "])  # Cabeçalho
        for valor in tempo_bucket:
            escritor.writerow([valor])
        escritor.writerow(["Média do tempo de execução:", media])
        escritor.writerow(["Desvio padrão do tempo de execução:", desvio])

def main7():

    tempo_bucket = []
    aux = 0
    soma = 0
    sorted_list = []

    # Rodar o código 5 vezes, mas considerar apenas as últimas 4 execuções
    while aux != 5:
        vetor_150000 = gerar_lista_aleatoria(150000)
        print(vetor_150000[:10])
        copy = vetor_150000.copy()

        # Começa a contagem do tempo
        start = time.perf_counter()
        sorted_list = insertionSort(copy)
        end = time.perf_counter()

        # Adicionar o tempo de execução apenas se não for a primeira iteração
        
        tempo_bucket.append(1000*(end - start))

        aux += 1

    print('SORTED LIST (última execução):')
    print(sorted_list)

    # Calculando a média do tempo de execução considerando apenas as 4 últimas iterações
    soma = sum(tempo_bucket)
    media = soma / len(tempo_bucket)
    desvio = calcular_desvio_padrao(tempo_bucket)


    # Escrevendo os tempos de execução no arquivo CSV
    with open("insertion_150000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["insertion_150000: "])  # Cabeçalho
        for valor in tempo_bucket:
            escritor.writerow([valor])
        escritor.writerow(["Média do tempo de execução:", media])
        escritor.writerow(["Desvio padrão do tempo de execução:", desvio])

def main8():

    tempo_bucket = []
    aux = 0
    soma = 0
    sorted_list = []

    # Rodar o código 5 vezes, mas considerar apenas as últimas 4 execuções
    while aux != 5:
        vetor_200000 = gerar_lista_aleatoria(200000)
        print(vetor_200000[:10])
        copy = vetor_200000.copy()

        # Começa a contagem do tempo
        start = time.perf_counter()
        sorted_list = insertionSort(copy)
        end = time.perf_counter()

        # Adicionar o tempo de execução apenas se não for a primeira iteração
        
        tempo_bucket.append(1000*(end - start))

        aux += 1

    print('SORTED LIST (última execução):')
    print(sorted_list)

    # Calculando a média do tempo de execução considerando apenas as 4 últimas iterações
    soma = sum(tempo_bucket)
    media = soma / len(tempo_bucket)
    desvio = calcular_desvio_padrao(tempo_bucket)

    # Escrevendo os tempos de execução no arquivo CSV
    with open("insertion_200000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["insertion_200000: "])  # Cabeçalho
        for valor in tempo_bucket:
            escritor.writerow([valor])
        escritor.writerow(["Média do tempo de execução:", media])
        escritor.writerow(["Desvio padrão do tempo de execução:", desvio])

main1()
main2()
main3()
main4()
main5()
main6()
main7()
main8()
