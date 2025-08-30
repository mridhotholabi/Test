# Preprocessing teks
import string

def bersihkan_teks(teks):
    teks = teks.lower()
    for p in string.punctuation:
        teks = teks.replace(p, '')
    return teks