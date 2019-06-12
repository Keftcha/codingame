def encode(word):
    word = list(word)
    new_word = []
    idx = 1
    while len(word) > 0:
        ajout = "".join(word[:idx])
        del word[:idx]
        if idx % 2 == 0:
            new_word.insert(0, ajout)
        elif idx % 2 == 1:
            new_word.append(ajout)
        idx += 1
        
    return "".join(new_word)


def decode(word):
    word = list(word)
    old_word = []
    while len(word) > 1:
        idx = 0
        while (idx + 1) * ((idx * 1) / 2) < len(word) - 1:
            idx += 1
        nb_lettres_pas_prendre = int((idx - 1 + 1) * (((idx - 1) * 1) / 2))
        
        if idx % 2 == 0:
            old_word.insert(0, "".join(word[:-nb_lettres_pas_prendre]))
            del word[:-nb_lettres_pas_prendre]
        elif idx % 2 == 1:
            old_word.insert(0, "".join(word[nb_lettres_pas_prendre:]))
            del word[nb_lettres_pas_prendre:]
        
    old_word.insert(0, "".join(word[0]))
    return("".join(old_word))
        

n = input()
message = input()

if n[0] == "-":
    fonction = encode
    n = int(n[1:])
else:
    fonction = decode
    n = int(n)

while n > 0:
    message = fonction(message)
    n -= 1

print(message)
