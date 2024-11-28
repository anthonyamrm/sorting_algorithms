import time
import csv
import os
import random
import statistics

def gerar_lista_aleatoria(tamanho):
    return random.sample(range(tamanho * 10), tamanho)

def calcular_desvio_padrao(tempos):
    return statistics.stdev(tempos)

def selectionSOrt(arr):
    n = len(arr)
    for i in range(n - 1):
      
        # Assume the current position holds
        # the minimum element
        min_idx = i
        
        # Iterate through the unsorted portion
        # to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
              
                # Update min_idx if a smaller element is found
                min_idx = j
        
        # Move minimum element to its
        # correct position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

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
        sorted_list = selectionSOrt(copy)
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
    with open("selection_500.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["selection_500: "])  # Cabeçalho
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
        sorted_list = selectionSOrt(copy)
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
    with open("selection_1000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["selection_1000: "])  # Cabeçalho
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
        sorted_list = selectionSOrt(copy)
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
    with open("selection_5000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["selection_5000: "])  # Cabeçalho
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
        sorted_list = selectionSOrt(copy)
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
    with open("selection_30000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["selection_30000: "])  # Cabeçalho
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
        sorted_list = selectionSOrt(copy)
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
    with open("selection_80000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["selection_80000: "])  # Cabeçalho
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
        sorted_list = selectionSOrt(copy)
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
    with open("selection_100000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["selection_100000: "])  # Cabeçalho
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
        sorted_list = selectionSOrt(copy)
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
    with open("selection_150000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["selection_150000: "])  # Cabeçalho
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
        sorted_list = selectionSOrt(copy)
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
    with open("selection_200000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["selection_200000: "])  # Cabeçalho
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
