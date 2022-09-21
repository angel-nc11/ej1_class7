import operaciones.op as op

def main():
    s= op.suma(10,5)
    print("la suma es: ",s)

    r= op.resta(10, 5)
    print("la resta es: ",r)

    m= op.multiplicacion(10, 5)
    print("la multiplicacion es: ",m)

    d= op.div(10, 5)
    print("La division es: ",d)


if __name__ == '__main__':
    main()

