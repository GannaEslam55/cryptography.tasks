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
