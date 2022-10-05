def my_function():
    r=input("entrez la valeur de rayon de la section : ")
    p=input("entrez la valeur de pression en pascale : ")
    try:
        r=float(r)
        p=float(p)
        F=3.141592654*r**(2)*p
        print("la valeur de la force est : ",F,"N")
    except:
        print("la valeur de rayon ou etla pression est inccorect")
        my_function()
my_function()
