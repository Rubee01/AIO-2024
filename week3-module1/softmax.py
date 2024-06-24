import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    # Due to the input data being torch tensor, we import and utilize the torch tensor built-in function
    def forward(self, x):
        return torch.exp(x) / torch.sum(torch.exp(x))
    

class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        stable_input = x - torch.max(x)
        return torch.exp(stable_input) / torch.sum(torch.exp(stable_input))


if __name__ == "__main__":
    data = torch.Tensor([1, 2, 3])
    softmax_stable = SoftmaxStable()
    output = softmax_stable(data)
    print(output)
