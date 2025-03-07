import string
from collections import Counter

def frequency_analysis(ciphertext):
    ciphertext = ciphertext.lower()
    letter_counts = Counter(filter(str.isalpha, ciphertext))
    return sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

def decrypt(ciphertext, mapping):
    table = str.maketrans(mapping)
    return ciphertext.translate(table)

english_freq_order = "etaoinshrdlcumwfgypbvkjxqz"  # Common English letter order

ciphertext = input("Enter encrypted text: ")
letter_freq = frequency_analysis(ciphertext)

decryption_map = {}
for (cipher_letter, _), plain_letter in zip(letter_freq, english_freq_order):
    decryption_map[cipher_letter] = plain_letter

decrypted_text = decrypt(ciphertext, decryption_map)

print("Most likely decrypted text:", decrypted_text)
