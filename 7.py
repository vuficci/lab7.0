def count_vowels_consonants(s):
    vowels = "vvvvvvvvv"
    consonants = "ppppppp"
    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = sum(1 for char in s if char in consonants)
    return vowel_count, consonant_count

user_input = input("Введите строку: ")
vowels, consonants = count_vowels_consonants(user_input)

print("Количество гласных букв:", vowels)
print("Количество согласных букв:", consonants)