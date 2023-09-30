def analizador_lexico(alfabeto, programa_fuente):
    tokens = []
    i = 0

    while i < len(programa_fuente):
        # create a token variable for add characters and create token
        token = ""
        """
            while position is less than the length of the source code and the character is in the alphabet
            then add the character to the token variable and increase the position
        """
        while i < len(programa_fuente) and programa_fuente[i] in alfabeto:
            token += programa_fuente[i]
            i += 1
        """
            if token is not empty then add the token to the tokens list,
            else if the character is a space then increase the position,
            else show an error and return None to finish the function
        """
        if token:
            tokens.append(token)
        elif programa_fuente[i].isspace():
            i += 1
        else:
            print("Error: Símbolo no válido en la posición " + str(i))
            return None
    # return tokens list
    return tokens



# Alfabeto permitido
alfabeto_permitido = input("Ingrese el alfabeto permitido: ")

# Cadena de programa fuente
programa_fuente = input("Ingrese el programa fuente: ")

resultado = analizador_lexico(alfabeto_permitido, programa_fuente)

print(resultado)
