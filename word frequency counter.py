def word_frequency_counter():
    # Get input sentence from user
    sentence = input("MY dog went under the fence and entered the yard next door: ")

    # Split the sentence into words
    words = sentence.split()

    # Initialize an empty dictionary to store word counts
    word_counts = {}

    # Count occurrences of each word
    for word in words:
        # Remove punctuation and convert to lowercase for better counting
        cleaned_word = word.strip(".,!?;:\"'").lower()
        if cleaned_word:
            word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1

    # Print the word count dictionary
    print("Word frequencies:")
    print(word_counts)


# Call the function
word_frequency_counter()