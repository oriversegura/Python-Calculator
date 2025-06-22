import math
import pprint
import time


# Main func
def main() -> None:
    # Welcome Print Calculator
    print('***** Python Calculator By SeguraDev *****')

    cicle : bool = True
    # take 2 vals to realize all basic mathematics func.
    while cicle == True:

        try:
            value1 : float = float(input("Type first value: "))
            value2 : float = float(input("Type second value: "))
        except UnboundLocalError or ValueError:
            print("Ingress valid value!")
        try:
            if type(value1) is not float or type(value2) is not float:
                print("Ingress valid value!")
        except UnboundLocalError or ValueError:
            print("Chugaste")

        else:
            print("Calculating results...")
            time.sleep(0.2)

        def result(value1 : float, value2 : float) -> float:
            addition = value1 + value2
            substraction = value1 - value2
            multiplication = value1 * value2
            division = value1 / value2
            return f'''
                Results are:
                
                Addition of {value1} and {value2} is  {addition}
                Substraction of {value1} and {value2} is {substraction}
                Multiplication of {value1} and {value2} is {multiplication}
                Division of {value1} and {value2} is {division}
                
                    '''

        try:
            results = result(value1, value2)
            print(results)

        except ZeroDivisionError as e:
            print(e)

        cicle = False
if __name__ == "__main__":
    main()