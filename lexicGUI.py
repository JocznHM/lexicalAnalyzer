"""
    This program is a lexical analyzer that receives an alphabet and
    the source code of some programming language and returns the tokens found in the source code.

    It is an example of a simple lexical analyzer for teaching purposes for the subject
    "lenguajes y autómatas 1" of the "Insituto Tecnológico de San Luis Potosí".

    This program was made with Python 3.9.0 and customtkinter 5.1.2


    -----------------------------------------------------
    |author: Carlos Joczan Hernandez Morquecho (JocznHM)|
    -----------------------------------------------------
"""

#imports the customtkinter library
import customtkinter as tk


"""
    This function receives the alphabet and the source code and returns the tokens found in the source code.
    params:
        alfabeto: The alphabet of the language.
        programa_fuente: The source code.
    return:
        tokens: The tokens found in the source code.

"""
def analizador_lexico(alfabeto, programa_fuente):
    #delete the text in the result text area
    resultado_text.delete("1.0", tk.END)
    tokens = []
    i = 0

    while i < len(programa_fuente):
        #create a token variable for add characters and create token
        token = ""
        """
            while position is less than the length of the source code and the character is in the alphabet
            then add the character to the token variable and increase the position
        """
        while i < len(programa_fuente) and programa_fuente[i] in alfabeto:
            resultado_text.insert(tk.END, "el caracter es valido... Caracter: (" +
                                  programa_fuente[i] + ") \n")
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
            resultado_text.insert(tk.END, "Error: caracter no válido: el caracter es( " + programa_fuente[i] + ") \n")
            return None
    #return tokens list
    return tokens


"""
    Function to analyze the source code and show the tokens founds.
"""
def analizar():
    #get the alphabet and the source code from the entries and the text area
    alfabeto = alfabeto_entry.get()
    codigo_fuente = codigo_fuente_entry.get("1.0", tk.END)

    #call the lexical analyzer function
    tokens = analizador_lexico(alfabeto, codigo_fuente)

    #if tokens is not None then show the tokens founds
    if tokens is not None:
        resultado_text.insert(tk.END, "Tokens encontrados:\n")
        for token in tokens:
            resultado_text.insert(tk.END, token + "\n")


# create the main window
ventana = tk.CTk()
ventana.title("Analizador Léxico con Python")
ventana.geometry("680x440")
ventana.resizable(False, False)

# Entry and label for the alphabet
alfabeto_label = tk.CTkLabel(ventana, text="Alfabeto:")
alfabeto_label.pack(padx=10, pady=5)
alfabeto_entry = tk.CTkEntry(ventana, width=580, height=10)
alfabeto_entry.pack(padx=10, pady=5)

# Text area and label for the source code
codigo_fuente_label = tk.CTkLabel(ventana, text="Código Fuente:")
codigo_fuente_label.pack(padx=10, pady=5)
codigo_fuente_entry = tk.CTkTextbox(ventana, width=580, height=100)
codigo_fuente_entry.pack(padx=10, pady=5)

# Button that triggers the function to analyze the source code.
frame_button = tk.CTkFrame(ventana)
frame_button.pack(pady=10)
analizar_button = tk.CTkButton(frame_button, text="Analizar", command=analizar)
analizar_button.pack()

# Text area and label for the result
label_resultado = tk.CTkLabel(ventana, text="Resultado:")
label_resultado.pack(padx=10, pady=5)
resultado_text = tk.CTkTextbox(ventana, width=580, height=120)
resultado_text.pack(padx=10, pady=5)

ventana.mainloop()
