def mean_difference(y, y_hat, n, p):
    y_root = y ** (1/n)
    y_hat_root = y_hat ** (1/n)
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss

if __name__ == "__main__":
    print(mean_difference(y=100, y_hat=99.5, n=2, p=1))