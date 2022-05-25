import webbrowser
import os
import time


def show_pics(html, nombre):
    with open(f'{nombre}.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('La información del pokemon aparecerá en su navegador...')
    time.sleep(2)
    webbrowser.open(f'{nombre}.html')
    time.sleep(2)
    os.remove(f'{nombre}.html')
