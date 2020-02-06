nombre = input("Ingresa la palabra: ")
letras = list(nombre)
print("Es palindromo") if letras == list(reverse(word)) else print("No es palindromo")