boleto = input("¿Tiene usted boleto? si/no ").lower()

if boleto in ["si", "sí"]:
    print("Puede entrar")
elif boleto == "no":
    print("No puede entrar")
else:
    print("Respuesta no válida")