import numpy as np

def Key_length(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range (256):
        j = (j + S[i] + key[i % key_length]) % 256
        # Swapping
        S[i], S[j] = S[j], S[i]
    return S

def Generate(S, n):
    i = 0
    j = 0
    key = []
    while n > 0:
        n = n - 1
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        # Swapping
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        key.append(K)
    return key


key = input("Enter your key: ")
plaintext = input("Enter your plaintext: ")

def preparing_key_array(s):
    generate_key = [ord(c) for c in s]
    return generate_key

key = preparing_key_array(key)
#
S = Key_length(key)

keystream = np.array(Generate(S,len(plaintext)))
print("The key stream text: ",keystream)


plaintext = np.array([ord(i) for i in plaintext])

(cipher) = keystream ^ plaintext

print("The cipher text: ", cipher)
print("The cipher in hexa: ",[chr(c) for c in cipher])
