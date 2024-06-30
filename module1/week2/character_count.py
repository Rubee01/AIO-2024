def character_count(string: str):
    # Initialize the dictionary that will store the output
    output_dict = {}
    # Scan the string
    for i in string:
        # If the character is not already existed in the dictionary, add new element to 1
        if i not in output_dict.keys():
            output_dict[i] = 1
        # If the character is already existed in the dictionary, add its counter by 1
        else:
            output_dict[i] += 1

    return output_dict


if __name__ == "__main__":
    # Question 2 multiple-choice
    output = character_count('smiles')
    print(output)
