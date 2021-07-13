import sys
import urllib.request
import argparse
import os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from PIL import Image
from datetime import datetime
from threading import Lock

start_time = datetime.now()


# Проверка типов

def urls_file_type(files):
    if files.find('.txt') > 0:
        return files
    else:
        raise argparse.ArgumentTypeError(f'Invalid value {files}, enter information in "text.txt" format')


def dir_type(dir):
    if dir.find('/') > 0:
        return dir
    else:
        raise argparse.ArgumentTypeError(f'Invalid value {dir}, enter information in "directory/" format')


def threads_type(flow):
    if flow.isdigit():
        return int(flow)
    else:
        raise argparse.ArgumentTypeError(f'Invalid value {flow}, enter information in "int" format')


def size_type(image_size):
    if image_size.find('x') and isinstance(image_size, str):
        return image_size
    else:
        raise argparse.ArgumentTypeError(f'Invalid value {image_size}, enter information in "128x128" format')


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('urls_file', default='urllist.txt', nargs='?', type=urls_file_type)
    parser.add_argument('-d', '--dir', default='thumbnails/', nargs='?', type=dir_type)
    parser.add_argument('-t', '--threads', default=4, nargs='?', type=threads_type)
    parser.add_argument('-s', '--size', default='128x128', nargs='?', type=size_type)

    return parser


# Загрузка файлов
def download_file(url, name):
    """Переменные для статистики"""
    global DOWNLOAD_COMPLETE, DOWNLOAD_ERROR, SUM_BYTE
    """Создаем папку"""
    dirname = namespace.dir
    if not os.path.isdir(namespace.dir):
        os.mkdir(namespace.dir)

    """Скачиваем файл"""
    fname = name
    try:
        handle = urllib.request.urlopen(url)
        filepath = os.path.join(dirname, fname)

        length_in_bytes = os.stat(filepath).st_size
        SUM_BYTE += length_in_bytes

        with open(filepath, "wb") as f:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f.write(chunk)
        lock.acquire()
        DOWNLOAD_COMPLETE += 1
        lock.release()
        print(f'download file {fname} complete')
    except urllib.error.HTTPError:
        lock.acquire()
        DOWNLOAD_ERROR += 1
        lock.release()
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


if __name__ == '__main__':
    lock = Lock()
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    # Проверяем/создаем директорию
    try:
        with open(namespace.urls_file) as file:
            url = [x.strip() for x in file]

    except FileNotFoundError:
        print(f'File is missing')

    file_names = [f'{x}.jpg' for x in range(len(url))]
    dir_name = namespace.dir

    # Загружаем файлы
    DOWNLOAD_COMPLETE = 0
    DOWNLOAD_ERROR = 0
    SUM_BYTE = 0
    with ThreadPoolExecutor(max_workers=namespace.threads) as executor:
        f = executor.map(download_file, url, file_names)

    path = namespace.dir
    dirs = os.listdir(path)

    # Редактируем файлы
    # files_name = os.listdir(path=namespace.dir)
    with ThreadPoolExecutor(max_workers=namespace.threads) as executor:
        x = executor.map(resize, file_names)
        executor.submit(resize)

    # Расчет общего количества байт
    root_directory = Path(namespace.dir)

    print(f'Number of downloaded files: {DOWNLOAD_COMPLETE + DOWNLOAD_ERROR}\n'
          f'Number of downloaded bytes: {SUM_BYTE}\n'
          f'Number of requests completed with an error: {DOWNLOAD_ERROR}\n'
          f'Total execution time: {datetime.now() - start_time}')

    # python download.py urllist.txt --dir=thumbnails/ --threads=4 --size=128x128
