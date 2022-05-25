import poke_validation as pv
from get_module import get_info
from poke_comentarios import obtener_comentarios
from poke_span import genera_span
from string import Template
from show import show_pics


name = input('Ingrese el nombre del pokemon a buscar\n(Nota: Si el pokémon tiene espacios reemplace por "-".\nNo '
             'coloque ningún tipo de signo de puntuación adicional. \nEjemplo: Mr. Mime, se debe ingresar como '
             'mr-mime o Mr-Mime): ')
name = pv.validate(name)
url_base = f'https://pokeapi.co/api/v2/pokemon/{name}'
data_base = get_info(url_base)
name = name.capitalize()
poke_n = data_base["id"]
stats = data_base["stats"]

indicadores = []
for item in stats:
    indicadores.append(item["base_stat"])


poke_hp, poke_at, poke_de, poke_ate, poke_dee, poke_ve = indicadores

# imagen (url)
poke_img = data_base['sprites']['front_default']

# etapa previa
url_previa = f"https://pokeapi.co/api/v2/pokemon-species/{poke_n}"
data_etapa_previa = get_info(url_previa)

poke_etapa_previa = data_etapa_previa['evolves_from_species']
if poke_etapa_previa is not None:
    poke_etapa_previa = poke_etapa_previa['name'].capitalize()
else:
    poke_etapa_previa = ""
if poke_etapa_previa != "":
    poke_etapa_previa = f"Etapa Previa: {poke_etapa_previa}"

# tipos
tipos_lista = data_base["types"]

tipos = []
for item in tipos_lista:
    tipos.append(item["type"]["name"])


# descripción
poke_comentario = obtener_comentarios(poke_n)

# span tipos
span_tipo = f"{genera_span(tipos)}"

# fortalezas y debilidades
url_damage = [item["type"]["url"] for item in tipos_lista]

# indicadores de combate
url_damage = []
for item in tipos_lista:
    url_damage.append(item["type"]["url"])

if len(url_damage) == 1:
    data_rel1 = get_info(url_damage[0])

else:
    data_rel1 = get_info(url_damage[0])
    data_rel2 = get_info(url_damage[1])

# super eficaz contra
if len(url_damage) == 1:
    supef_contra = data_rel1["damage_relations"]["double_damage_to"]
else:
    supef_contra = data_rel1["damage_relations"]["double_damage_to"] + data_rel2["damage_relations"]["double_damage_to"]


supef_co = [item["name"] for item in supef_contra]
supef_co = set(supef_co)


# debil contra
if len(url_damage) == 1:
    debil_contra = data_rel1["damage_relations"]["double_damage_to"]
else:
    debil_contra = data_rel1["damage_relations"]["double_damage_to"] + data_rel2["damage_relations"]["double_damage_to"]

deb_co = [item["name"] for item in debil_contra]
deb_co = set(deb_co)


# resistente contra
if len(url_damage) == 1:
    resistente_contra = data_rel1["damage_relations"]["half_damage_from"]
else:
    resistente_contra = data_rel1["damage_relations"]["half_damage_from"] + data_rel2["damage_relations"]["half_damage_from"]

res_co = [item["name"] for item in resistente_contra]
res_co = set(res_co)


# poco eficaz contra
if len(url_damage) == 1:
    pocoeficaz_contra = data_rel1["damage_relations"]["half_damage_to"]
else:
    pocoeficaz_contra = data_rel1["damage_relations"]["half_damage_to"] + data_rel2["damage_relations"]["half_damage_to"]

poef_co = [item["name"] for item in pocoeficaz_contra]
poef_co = set(poef_co)


# inmune contra
if len(url_damage) == 1:
    inmune_contra = data_rel1["damage_relations"]["no_damage_from"]
else:
    inmune_contra = data_rel1["damage_relations"]["no_damage_from"] + data_rel2["damage_relations"]["no_damage_from"]

inm_co = [item["name"] for item in inmune_contra]
inm_co = set(inm_co)


# ineficaz contra
if len(url_damage) == 1:
    ineficaz_contra = data_rel1["damage_relations"]["no_damage_to"]
else:
    ineficaz_contra = data_rel1["damage_relations"]["no_damage_to"] + data_rel2["damage_relations"]["no_damage_to"]

inef_co = [item["name"] for item in ineficaz_contra]
inef_co = set(inef_co)


# span indicadores
span_supef_co = genera_span(supef_co)

span_deb_co = genera_span(deb_co)

span_res_co = genera_span(res_co)

span_poef_co = genera_span(poef_co)

span_inm_co = genera_span(inm_co)

span_inef_co = genera_span(inef_co)


# html de salida
with open('index.html', 'r', encoding='utf-8') as infile:
    entrada = infile.read()

document_template = Template(entrada)


# variables para html
html = document_template.safe_substitute(
    poke_n = poke_n,
    poke_name = name,
    poke_etapa_previa = poke_etapa_previa,
    poke_hp = poke_hp,
    poke_at = poke_at,
    poke_de = poke_de,
    poke_ate = poke_ate,
    poke_dee = poke_dee,
    poke_ve = poke_ve,
    poke_img = poke_img,
    span_tipo = span_tipo,
    poke_comentario = poke_comentario,
    span_supef_co = span_supef_co,
    span_deb_co = span_deb_co,
    span_res_co = span_res_co,
    span_poef_co = span_poef_co,
    span_inm_co = span_inm_co,
    span_inef_co = span_inef_co)


show_pics(html, 'output')
