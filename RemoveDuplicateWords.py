def remove_additional_duplicates_from_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        words = file.read().split()
        # Use a dictionary to keep track of words we've seen
        seen_words = {}
        no_duplicates_words = []
        for word in words:
            if word not in seen_words:
                # If we haven't seen the word before, add it to the output list
                no_duplicates_words.append(word)
                seen_words[word] = True
    
    with open(output_file_path, 'w') as file:
        for word in no_duplicates_words:
            file.write(word + '\n')

# Test the function
input_file_path = 'inputList.txt'
output_file_path = 'outputList.txt'
remove_additional_duplicates_from_file(input_file_path, output_file_path)
