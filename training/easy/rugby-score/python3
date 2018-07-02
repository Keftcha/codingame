score = int(input())

nb_essais = 0
while score >= nb_essais * 5:
    nb_transformation = 0
    while score >= nb_transformation * 2:
        nb_penalite = 0
        while score >= nb_penalite * 3:
            reste = score - nb_essais * 5
            reste = reste - nb_transformation * 2
            reste = reste - nb_penalite * 3
            if reste == 0 and nb_essais >= nb_transformation:
                print(nb_essais, nb_transformation, nb_penalite)
            nb_penalite += 1
        nb_transformation += 1
    nb_essais += 1
