import math

class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text[col] += text[pointer]
                pointer += key
        return ''.join(encrypted_text)

    def decrypt(self, text, key):
        num_cols = math.ceil(len(text) / key) 
        num_rows = key 
        num_shaded_boxes = (num_cols * num_rows) - len(text)

        decrypted_text = [''] * num_cols 
        col, row = 0, 0

        for symbol in text:
            decrypted_text[col] += symbol
            col += 1
            if col == num_cols or (col == num_cols - 1 and row >= num_rows - num_shaded_boxes):
                col = 0
                row += 1
        
        return ''.join(decrypted_text)
