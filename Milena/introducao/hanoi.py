



def hanoi(n, origem, auxiliar, dest):
    if n==1:
        print("\nMova disco %d da origem %d para destino %d"%(n,origem,dest))
        return

    hanoi(n-1,origem,dest,auxiliar)
    print("Mova disco %d da torre origem %d para destino %d"%(n,origem,dest))

    hanoi(n-1,auxiliar,origem,dest)


