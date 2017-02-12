#coding: utf-8

#Consignes : https://github.com/jhroy/syllabus-edm5240-H2017/blob/master/devoir1.md

mats1=list(range(30000,100000))
for mat1 in mats1:
    print("{}".format(mat1))

mats2=list(range(0,18000))

#A partir de là, on peut utiliser deux méthodes.
#1) Celle-ci (il faut désactiver l'autre) :
for mat2 in mats2:
    if mat2<10:
        print("0000{}".format(mat2))
    elif 10<=mat2<100:
        print("000{}".format(mat2))
    elif 100<=mat2<1000:
        print("00{}".format(mat2))
    elif 1000<=mat2<10000:
        print("0{}".format(mat2))
    else:
        print("{}".format(mat2))

#2) Ou celle-là (il faut désactiver la première) :
for mat2 in mats2:
    print(str(mat2).zfill(5))
