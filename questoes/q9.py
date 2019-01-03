def listas(l1, l2, l3):
    l1 = set(l1)
    l2 = set(l2)
    l3 = set(l3)

    # Os números aparecem nas 3 listas
    print(l1 & l2 & l3)

    # Os números aparecem em ao menos duas listas
    b = (l1 & l2) & (l1 & l3) & (l2 & l3)
    c = (l1 & l2) | (l1 & l3) | (l2 & l3)
    print(c - b)

    # Os números aparecem em apenas uma lista
    print((l1 - l2 - l3) | (l2 - l3 - l1) | (l3 - l2 - l1))


if __name__ == '__main__':
    l1 = [1, 2, 3]
    l2 = [2, 4, 3, 5]
    l3 = [0, 2, 5, 9]
    listas(l1, l2, l3)
