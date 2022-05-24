def run():
    META = 10000

    count = 0
    potencia = 2**count

    while potencia < META:
        print("2^" + str(count) + " = " + str(potencia))
        count = count +1
        potencia = 2**count


if __name__ == "__main__":
    run()