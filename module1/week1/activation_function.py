import math

def is_number(n):
    try:
        float(n)    # Type - casting the string to ‘float ‘.
                    # If string is not a valid ‘float ‘ ,
                    # it ’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True

def activation_function():
    #Input x-coordinate
    x = input("Input x: ")
    if is_number(x) == False:
        print(f"x must be a number")
        return
    else:
        x = float(x)
        func = input("Input activation Function (sigmoid|relu|elu): ")
        if func == "sigmoid":
            sigmoid = 1 / (1 + math.exp(-x))
            print(f"sigmoid: f({x}) = {sigmoid}")
            return
        elif func == 'relu':
            if x <= 0:
                print(f"relu: f({x}) = 0.0")
                return
            else:
                print(f"relu: f({x}) = {x}")
                return
        elif func == 'elu':
            alpha = 0.01    #Default alpha
            if x <= 0:
                elu = alpha * (math.exp(x) - 1)
                print(f"elu: f({x}) = {elu}")
                return
            else:
                print(f"elu: f({x}) = {x}")
                return
        else:
            print(f"{func} is not supported")


if __name__ == "__main__":
    activation_function()
