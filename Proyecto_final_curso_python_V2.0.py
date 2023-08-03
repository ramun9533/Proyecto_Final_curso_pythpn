import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests

def get_price(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    span_tag = soup.find('span', attrs={"class": "andes-money-amount__fraction"})
    price_str = span_tag.text.replace(',', '')
    return int(price_str)

# URLs de los artículos
urls = [
    'https://www.mercadolibre.com.mx/motorola-moto-g53-8-gb-128-gb-65/p/MLM22947162?pdp_filters=category:MLM1055#searchVariation=MLM22947162&position=3&search_layout=stack&type=product&tracking_id=d7676704-bae0-4c80-8d25-29fa31f1b171',
    'https://articulo.mercadolibre.com.mx/MLM-2003591282-celular-cubot-p80-dual-sim-256-gb-global-8-gb-ram-5200mah-android-13-_JM#position=45&search_layout=stack&type=item&tracking_id=d7676704-bae0-4c80-8d25-29fa31f1b171',
    'https://www.mercadolibre.com.mx/realme-gt-2-pro-dual-sim-256-gb-steel-black-12-gb-ram/p/MLM19130693?pdp_filters=item_id:MLM1507221033#is_advertising=true&searchVariation=MLM19130693&position=9&search_layout=stack&type=pad&tracking_id=d7676704-bae0-4c80-8d25-29fa31f1b171&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=9&ad_click_id=MjMzNjkyN2QtZmI2MC00ZDAzLWJiZDUtZGQ1OWI5NWU0MWFl'
]

# Obtener precios de los artículos
precios = [get_price(url) for url in urls]

# Datos de los precios y nombres de los artículos
articulos = ['Moto G53', 'Cubot P80', 'GT 2 Pro']
def imprime(precios, articulos):
    # Crear la gráfica de barras
    plt.bar(articulos, precios)

    # Etiquetas del eje x
    plt.xlabel('Artículos')

    # Etiquetas del eje y
    plt.ylabel('Precio')

    # Título del gráfico
    plt.title('Precios de tres artículos')

    # Mostrar el gráfico
    plt.show()

imprime(precios, articulos)
