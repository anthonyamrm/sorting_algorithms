import time
import csv
import os
import random
import statistics

def gerar_lista_aleatoria(tamanho):
    return random.sample(range(tamanho * 10), tamanho)

def calcular_desvio_padrao(tempos):
    return statistics.stdev(tempos)

# Radix sort in Python
# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10

    return array


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
        sorted_list = radixSort(copy)
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
    with open("radix_500.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["radix_500: "])  # Cabeçalho
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
        sorted_list = radixSort(copy)
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
    with open("radix_1000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["radix_1000: "])  # Cabeçalho
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
        sorted_list = radixSort(copy)
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
    with open("radix_5000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["radix_5000: "])  # Cabeçalho
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
        sorted_list = radixSort(copy)
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
    with open("radix_30000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["radix_30000: "])  # Cabeçalho
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
        sorted_list = radixSort(copy)
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
    with open("radix_80000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["radix_80000: "])  # Cabeçalho
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
        sorted_list = radixSort(copy)
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
    with open("radix_100000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["radix_100000: "])  # Cabeçalho
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
        sorted_list = radixSort(copy)
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
    with open("radix_150000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["radix_150000: "])  # Cabeçalho
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
        sorted_list = radixSort(copy)
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
    with open("radix_200000.csv", "w", newline="", encoding="utf-8") as aarquivo:
        escritor = csv.writer(aarquivo)
        escritor.writerow(["radix_200000: "])  # Cabeçalho
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
