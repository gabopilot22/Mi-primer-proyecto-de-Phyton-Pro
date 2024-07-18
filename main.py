None
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print("Bien, tu palabra se encuentra en el diccionario")
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("Opps,no esta en el diccionario")
    brake
