def calculate_f1_scores(tp, fp, fn):
    #Conditionally checking parameter types and values
    if type(tp) != int:
        print(f"tp must be int")
        return
    elif type(fp) != int:
        print(f"fp must be int")
        return
    elif type(fn) != int:
        print(f"fn must be int")
        return
    
    if tp <= 0 or fp <= 0 or fn <= 0:
        print(f"tp and fp and fn must be greater than zero")
        return
    
    #When all conditions are met, calculate the required metrics
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * (precision * recall) / (precision + recall)
    
    #Demonstrate the results
    print(f"precision is {precision}")
    print(f"recall is {recall}")
    print(f"f1-score is {f1}")

    return f1

if __name__ == "__main__":
    #Multiple-choice question 1:
    assert round(calculate_f1_scores(tp =2, fp =3, fn =5), 2) == 0.33
    print(round(calculate_f1_scores(tp =2, fp =4, fn =5), 2))  
    #Answer: 0.31
    