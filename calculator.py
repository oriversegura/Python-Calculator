import time


# Main func
def main():
    # Welcome Print Calculator
    print("***** Python Calculator By SeguraDev *****")

    print("Insert two values, neither can be 0!\n")

    while True:
        # take 2 vals to realize all basic mathematics func.
        while True:
            try:
                value1: float = float(input("Type first value: "))
                break
            except:
                print("Ingress valid value!")

        while True:
            try:
                value2: float = float(input("Type second value: "))
                break
            except:
                print("Ingress valid value!")

        print("Calculating results...")
        time.sleep(1)

        def result(value1: float, value2: float) -> str:
            addition = value1 + value2
            substraction = value1 - value2
            multiplication = value1 * value2
            division = value1 / value2
            return f"""
                Results are:
                
                Addition of {value1} and {value2} is  {addition}
                Substraction of {value1} and {value2} is {substraction}
                Multiplication of {value1} and {value2} is {multiplication}
                Division of {value1} and {value2} is {division}
                
                """

        try:
            results = result(value1, value2)
            print(results)
            break
        except:
            print("Do not divide by 0")
            print("Program restart\n")
            time.sleep(1)


if __name__ == "__main__":
    main()
