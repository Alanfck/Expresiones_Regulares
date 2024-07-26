
"""

Las expresiones regulares son una forma compacta de expresar.

Expresiones Regulares Basicas:

*   Cadena Vacia
*   Cualquier simbolo del alfabeto es una expresion regular.
*   Si R1 y R2 (AND) es una expresion regular, entonces R1 y R2 tambien es una expresion regualar (Es una concatenacion).
*   Cerradura de Klein (Estrella): Si R es una expresion regular, entonces R* tambien es una expresion regular(es concatenar R, cero o mas veces).
*   Disyuncion: Si R1 y R2 (OR) son expresiones regulares tambien lo es R1 | R2
*   Agrupacion: Si R es una expresion regular, entonces (R) tambien lo es.

"""

#importamos el modulo de expresiones regulares
import re

cadena = "" #cadena vacia
exp_reg = "" # quiero reconocer cadenas pero cadenas que no tengan nada de texto, si la cadena cambia y deja de ser vacia, en este caso no lo reconocera

def eval_exp_reg(exp_reg,cadena): #definimos una funcion en python
  resultado = re.fullmatch(exp_reg, cadena)
  if resultado: #si resultado tiene algo, se ejecuta el if
    print("aceptado")
  else: #si el resulatado es NONE(NULO)
    print("rechazado")
  print(resultado)


eval_exp_reg(exp_reg,cadena)

#expresion regular como un simbolo
exp_reg = "a" #un solo simbolo
cadena = "a" #la cadena debe coicidir toda con la expresion regular, por ejemplo "hola" tiene a, pero no es igual a la letra "a"
eval_exp_reg(exp_reg,cadena)

#concatenacion
exp_reg = "ab" # es pegar una letra con otra
cadena = "ab"
eval_exp_reg(exp_reg,cadena)

#cerradura de Klein

exp_reg = "a*" #Me interesa 0 o mas veces la letra a
cadena = "a" #si pones varias veces la cadena a, lo va aceptar, mientras no agregue otra letra
eval_exp_reg(exp_reg, cadena)

# agrupacion

exp_reg = "(ab)*" # En la expresion regular, el "()" es un "metacaracter", en la cadena no deberia estar, si necesitas leer los "()", los debes escapar y poner \(ab\)
cadena = "ababab"
eval_exp_reg(exp_reg, cadena)

# Disyuncion (OR)
exp_reg = "0|1" #
cadena = "0"
eval_exp_reg(exp_reg, cadena)

#Se pueden combinar
exp_reg = "(0|1)*" #se pueden combinar todas, para leer diferentes numeros
cadena = "0101010101"
eval_exp_reg(exp_reg, cadena)

"""

Otros ejemplos...

"""

#Expresion regular "R?"

exp_reg = "a?" # 0 o 1 vez la expresion regular, el signo "? " es para leer 0 o 1 vez
cadena = "a"
eval_exp_reg(exp_reg, cadena)

#Expresion Regular equivalente
exp_reg = "|a"
cadena = "a"
eval_exp_reg(exp_reg, cadena)

#Expresion regular "R+"
exp_reg = "a+" # 1 o más veces la expresión regular R.
cadena = "aaa"
eval_exp_reg(exp_reg, cadena)

#Expresion regular equivalente
exp_reg = "aa*|a" # 1 o más veces la expresión regular R.
cadena = ""
eval_exp_reg(exp_reg, cadena)

#Expresion regular "R{3}"
exp_reg = "a{3}" # La expresión regular R concatenada 3 veces.
cadena = "aaa"
eval_exp_reg(exp_reg, cadena)

#Expresion regular equivalente
exp_reg = "aaa" # La expresión regular R concatenada 3 veces.
cadena = "aaa"
eval_exp_reg(exp_reg, cadena)

#Expresion regular "R{3,5}"
exp_reg = "a{3,5}" # La expresión regular R concatenada 3 veces o 4 veces o 5 veces.
cadena = "aaaa"
eval_exp_reg(exp_reg, cadena)

#Expresion regular equivalente
exp_reg = "aaa|aaaa|aaaaa" # La expresión regular R concatenada 3 veces o 4 veces o 5 veces.
cadena = "aaaaa"
eval_exp_reg(exp_reg, cadena)

#Expresion regular "R{3,}"
exp_reg = "a{3,}" # La expresión regular R concatenada 3 veces o más
cadena = "aaa"
eval_exp_reg(exp_reg, cadena)

#Expresion regular equivalente
exp_reg = "aaaa*" # La expresión regular R concatenada 3 veces o más
cadena = "aaa"
eval_exp_reg(exp_reg, cadena)

#Expresion regular "\d"
exp_reg = "\d" # 1 sólo dígito (puede ser 0, 1, 2, 3, 4, 5, 6, 7, 8 o 9).
cadena = "1"
eval_exp_reg(exp_reg, cadena)

#Expresion regular equivalente
exp_reg = "0|1|2|3|4|5|6|7|8|9 " # 1 sólo dígito (puede ser 0, 1, 2, 3, 4, 5, 6, 7, 8 o 9).
cadena = "0"
eval_exp_reg(exp_reg, cadena)

#Expresion regular "\d"
exp_reg = "[abc]" # Las letras “a” o “b” o “c”
cadena = "a"
eval_exp_reg(exp_reg, cadena)

#Expresion regular equivalente
exp_reg = "a|b|c " # Las letras “a” o “b” o “c”
cadena = "b"
eval_exp_reg(exp_reg, cadena)

