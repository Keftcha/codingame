mot = input()
liste_palin = []

def add(chaine, liste):
    if len(liste) == 0 or len(liste[0]) == len(chaine):
        liste.append(chaine)
    elif len(liste[0]) < len(chaine):
        liste.clear()
        liste.append(chaine)

tail = head = -1
idx = 0
old_idx = -1

while idx < len(mot):
    
    # we are in the middle of a palindrome, initialisation
    if old_idx == -1:
        old_idx = idx
    
        if idx-1 > -1 and idx < len(mot) and mot[idx-1] == mot[idx]:
            tail = old_idx - ((idx - old_idx) + 1)
            head = idx
        elif idx-1 > -1 and idx+1 < len(mot) and mot[idx-1] == mot[idx+1]:
            tail = old_idx - ((idx - old_idx) + 1)
            head = idx + 1
        else:
            old_idx = -1
            
    # search how long the palindrome is
    elif old_idx != -1:
        if mot[tail] != mot[head]:
            add(mot[tail+1:head], liste_palin)
            idx = old_idx
            old_idx = -1
        elif (tail == 0 or head == len(mot)-1) and mot[tail] == mot[head]:
            add(mot[tail:head+1], liste_palin)
            idx = old_idx
            old_idx = -1
        else:
            tail -= 1
            head += 1
            
    idx += 1

[print(palin) for palin in liste_palin]
