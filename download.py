import sys
import urllib.request
import argparse
import queue
import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from PIL import Image
from datetime import datetime


start_time = datetime.now()
global RESULT
RESULT = {'Download files': 0, 'Download fail': 0, 'Bytes loaded': 0}


def createParser():
    parser = argparse.ArgumentParser()
    # default='urllist.txt'
    parser.add_argument('urls_file', nargs='?')
    # default='thumbnails/'
    parser.add_argument('-d', '--dir', nargs='?', type=str)
    # default=4
    parser.add_argument('-t', '--threads', nargs='?', type=int)
    # default=128x128
    parser.add_argument('-s', '--size', nargs='?')

    return parser


# Загрузка файлов
def download_file(url, name):
    """Переменные для статистики"""
    global DOWNLOAD_COMPLETE, DOWNLOAD_ERROR
    """Создаем папку"""
    dirname = namespace.dir
    if not os.path.isdir(namespace.dir):
        os.mkdir(namespace.dir)

    """Скачиваем файл"""
    fname = name
    try:
        handle = urllib.request.urlopen(url)
        filepath = os.path.join(dirname, fname)

        with open(filepath, "wb") as f:
            print(f'download file {fname} complete')
            DOWNLOAD_COMPLETE += 1
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f.write(chunk)
    except urllib.error.HTTPError:
        DOWNLOAD_ERROR += 1
        print(f'download file {fname} error')


# 128x128
# Функция изменения размера изображений
def resize():
    new_size = namespace.size
    new_size = new_size.split('x')
    for item in dirs:
        if os.path.isfile(path + item):
            im = Image.open(path + item)
            f, e = os.path.splitext(path + item)
            imResize = im.convert('RGB')
            imResize = imResize.resize((int(new_size[0]), int(new_size[1])), Image.ANTIALIAS)
            imResize.save(f + '.jpg', 'JPEG', quality=90)


parser = createParser()
namespace = parser.parse_args(sys.argv[1:])

q = queue.Queue()

# Проверяем/создаем директорию
try:
    file = open(namespace.urls_file)
    url = [x.strip() for x in file]

except FileNotFoundError:
    print(f'File is missing')

name = [f'{x}.jpg' for x in range(len(url))]
dir_name = namespace.dir

for i in url:
    q.put(i)

# Загружаем файлы
DOWNLOAD_COMPLETE = 0
DOWNLOAD_ERROR = 0
with ThreadPoolExecutor(max_workers=namespace.threads) as executor:
    f = executor.map(download_file, url, name)

path = namespace.dir
dirs = os.listdir(path)

# Редактируем файлы
with ThreadPoolExecutor(max_workers=namespace.threads) as executor:
    x = executor.submit(resize)

# Расчет общего количества байт
root_directory = Path('thumbnails')
sum_byte = sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file())

print(f'Number of downloaded files: {DOWNLOAD_COMPLETE + DOWNLOAD_ERROR}\n'
      f'Number of downloaded bytes: {sum_byte}\n'
      f'Number of requests completed with an error: {DOWNLOAD_ERROR}\n'
      f'Total execution time: {datetime.now() - start_time}')


