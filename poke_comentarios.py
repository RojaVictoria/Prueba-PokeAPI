import random
from get_module import get_info


def obtener_comentarios(pok_n):
    url_previa = f"https://pokeapi.co/api/v2/pokemon-species/{pok_n}"
    data_etapa_previa = get_info(url_previa)
    comentarios = data_etapa_previa["flavor_text_entries"]

    filtro = []
    for item in comentarios:
        if item["language"]["name"] == 'es':
            filtro.append(item["flavor_text"].replace("\n", " "))

    poke_comentario = random.choice(filtro)

    return poke_comentario
