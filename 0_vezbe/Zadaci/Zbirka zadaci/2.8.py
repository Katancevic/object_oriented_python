while True: 
    try:
        x = int(input("Unesite broj: "))

    except ValueError:
        print("Oops! To nije validan broj.")
        break
