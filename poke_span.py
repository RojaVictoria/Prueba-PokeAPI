def genera_span(lista):
    tipo_es = {
        "normal": "Normal", "fire": "Fuego", "flying": "Volador",
        "water": "Agua", "electric": "Eléctrico",
        "grass": "Planta", "ice": "Hielo", "fighting": "Lucha",
        "poison": "Veneno", "ground": "Tierra", "psychic": "Psíquico",
        "bug": "Bicho", "rock": "Roca", "ghost": "Fantasma",
        "dragon": "Dragón", "dark": "Siniestro", "steel": "Acero",
        "fairy": "Hada", "baby": "Bebé", "legendary": "Legendario",
        "mythical": "Mítico"}

    span_str = ""
    for item in lista:
        item_es = tipo_es.get(item)
        span_str = span_str + f'<span class="label {item}">{item_es}</span>'
    return span_str
