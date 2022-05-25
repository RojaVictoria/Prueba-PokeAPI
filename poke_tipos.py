
#Se crea este módulo por la necesidad especial de los pokémon que tienen un solo tipo y son legendarios, bebé o mítico
def tipos(lista):
    if len(lista) == 1:
        #Se obtiene el tipo de pokemon normal, Ej: Volador
        tipo = [lista[0]['type']['name']]
    else:
        #Se obtiene el tipo de pokemon normal, Ej: Volador, Hielo
        tipo = [lista[0]['type']['name'], lista[1]['type']['name']]

    return tipo


def tipoEspecial(lista, listaespecies):
    if len(lista) == 1:
        #Se obtiene el tipo de pokemon normal, Ej: Volador
        tipo = [lista[0]['type']['name']]
        #En caso de cumplir con la condición particular se agrega el tipo particular
        if listaespecies['is_baby'] == True:
            tipo.append('baby')
        elif listaespecies['is_legendary'] == True:
            tipo.append('legendary')
        elif listaespecies['is_mythical'] == True:
            tipo.append('mythical')
    else:
        #Se obtiene el tipo de pokemon normal, Ej: Volador, Hielo
        tipo = [lista[0]['type']['name'], lista[1]['type']['name']]
        #En caso de cumplir con la condición particular se agrega el tipo particular
        if listaespecies['is_baby'] == True:
            tipo.append('baby')
        elif listaespecies['is_legendary'] == True:
            tipo.append('legendary')
        elif listaespecies['is_mythical'] == True:
            tipo.append('mythical')

    return tipo