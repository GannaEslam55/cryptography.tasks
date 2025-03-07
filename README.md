# task1
import string

def generate_matrix(key):
    key = "".join(dict.fromkeys(key + string.ascii_lowercase.replace('j', '')))
    return [list(key[i:i+5]) for i in range(0, 25, 5)]

def find_pos(matrix, letter):
    for r, row in enumerate(matrix):
        if letter in row:
            return r, row.index(letter)

def process_text(text):
    text = text.lower().replace("j", "i")
    text = "".join(filter(str.isalpha, text))
    return [(text[i], text[i+1] if i+1 < len(text) and text[i] != text[i+1] else 'x') for i in range(0, len(text), 2)]

def playfair(text, matrix, encrypt=True):
    result = ""
    for a, b in process_text(text):
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)
        if r1 == r2:
            c1, c2 = (c1+1, c2+1) if encrypt else (c1-1, c2-1)
        elif c1 == c2:
            r1, r2 = (r1+1, r2+1) if encrypt else (r1-1, r2-1)
        else:
            c1, c2 = c2, c1
        result += matrix[r1 % 5][c1 % 5] + matrix[r2 % 5][c2 % 5]
    return result

key = input("Enter keyword: ").lower()
matrix = generate_matrix(key)
print("\n".join(" ".join(row) for row in matrix))

choice = input("Encrypt or Decrypt? (E/D): ").lower()
text = input("Enter text: ")
print("Result:", playfair(text, matrix, encrypt=(choice == 'e')))

# task2
from itertools import permutations
import string

alphabet = string.ascii_lowercase
encrypted_message = input("Enter the encrypted message: ")

count = 0
for key in permutations(alphabet):
    key_str = ''.join(key)
    decrypted_text = encrypted_message.lower().translate(str.maketrans(key_str, alphabet))
    print(f"Key: {key_str}\nDecrypted: {decrypted_text}\n")
    count += 1
    if count == 10:  # Limit output to first 10 results
        break
# bonus
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





