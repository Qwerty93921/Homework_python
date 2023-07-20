def divide_into_syllables(word):
    syllables = []
    current_syllable = ""

    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    for char in word:
        if char.lower() in vowels:
            syllables.append(current_syllable)
            current_syllable = char
        else:
            current_syllable += char
    
    syllables.append(current_syllable)
    return syllables

input_file = 'input_2.txt'
output_file = 'output_2.txt'

with open(input_file, 'r') as first_file:
    words = first_file.read().splitlines()

syllable_words = []

for word in words:
    syllables = divide_into_syllables(word)
    syllable_words.append(syllables)

with open(output_file, 'w') as second_file:
    for word_syllables in syllable_words:
        second_file.write('\n'.join(word_syllables) + '\n')

print("Текст по слогам добавлен в файл")
