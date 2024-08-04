def encontrar_Pequeño(lista):
    pequeño=min(lista)
    grande= max(lista)
    return pequeño,grande
lista=[2,44,66,321,31,6,1,7,9]
pequeño,grande=encontrar_Pequeño(lista)
print(f"el numero mas pequeño es {pequeño} y el mas grande {grande}")
