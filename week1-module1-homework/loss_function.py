import math
import random

#Needs to optimize 
def loss_function():
    #Determine how many samples user want to take
    num_samples = input("Input number of samples ( integer number ) which are generated : ")
    if num_samples.isnumeric() == False:
        print(f"number of samples must be an integer number")
        return
    else:
        num_samples = int(num_samples)
        loss_name = input("Input loss name: ")
        for i in range(num_samples):
            sum = 0
            predict = random.uniform(0, 10)
            target = random.uniform(0, 10)
            if loss_name == 'MAE':
                sum += abs(target - predict)
                loss = sum / num_samples
            elif loss_name == 'MSE':
                sum = (target - predict) ** 2
                loss = sum / num_samples
            elif loss_name == 'RMSE':
                sum = (target - predict) ** 2
                loss = math.sqrt(sum / num_samples)

            print(f"loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {loss}")
        return


if __name__ == "__main__":
    loss_function()
        