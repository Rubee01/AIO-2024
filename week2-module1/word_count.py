def word_count(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        data = file.read()
        file.close()

    # Initialize the dictionary and preprocess the words
    output_dict = {}
    words = data.lower().split()
    for word in words:
        if word not in output_dict.keys():
            output_dict[word] = 1
        else:
            output_dict[word] += 1

    return output_dict


if __name__ == "__main__":
    # Question 3 multiple-choice
    output = word_count('D:/P1_data.txt')
    print(output['man'])
