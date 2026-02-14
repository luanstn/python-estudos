def contador (a, b, c):
    """
    isso é um docstring, voce vai usar pois caso coloque um help dá para saber

    :param a: inicio
    :param b: fim
    :param c: pulos
    :return:
    """
    cont = a
    while cont <= b:
        print(cont, end=' ')
        cont = cont + c
    print("fim")

contador(0, 100, 10)

help(contador)