def factorial(n):
    if n < 0:
        raise ValueError('n must be greater than zero')
    if n == 0 or n == 1:
        return 1
    #Call factorial function recursively
    return factorial(n - 1) * n


def sin_approx(x, n):
    sum = 0
    for i in range(n):
        sum += ((-1)**i) * (x**(2*i+1) / factorial(2*i+1))
    return sum

def cos_approx(x, n):
    sum = 0
    for i in range(n):
        sum += ((-1)**i) * (x**(2*i) / factorial(2*i))
    return sum

def sinh_approx(x, n):
    sum = 0
    for i in range(n):
        sum += x**(2*i+1) / factorial(2*i+1)
    return sum

def cosh_approx(x, n):
    sum = 0
    for i in range(n):
        sum += x**(2*i) / factorial(2*i)
    return sum

if __name__ == "__main__":
    print(sin_approx(3.14, 10))
    print(cos_approx(3.14, 10))
    print(sinh_approx(3.14, 10))
    print(cosh_approx(3.14, 10))