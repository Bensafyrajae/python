chaine = input("Entrez une chaîne de caractères : ")


resultat = ""


for caractere in chaine:
    if not resultat or caractere != resultat[-1]:
        resultat += caractere

print(resultat)