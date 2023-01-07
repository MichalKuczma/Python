def nitka_komplementarna(dna):
    nitka_komplementarna_dict={
        'A':'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }

    nitka_komplementarna_str = ""

    for char in dna:
        nitka_komplementarna_str += nitka_komplementarna_dict[char]

    return nitka_komplementarna_str

print(nitka_komplementarna("AGCAT"))



