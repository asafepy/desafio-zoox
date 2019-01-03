def escrevaSort(alist):
    tempLista = []

    for i, num in enumerate(alist):
        tempLista.append(num)
        print(sorted(tempLista))


if __name__ == '__main__':
    alist = [7, 5, 81, 3, 99]

    escrevaSort(alist)
