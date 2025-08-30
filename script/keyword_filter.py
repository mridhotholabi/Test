# Filter berdasarkan keyword

kata_terlarang = ['hoaks', 'penipuan', 'pornografi']

def filter_keyword(teks):
    teks = teks.lower()
    return any(k in teks for k in kata_terlarang)