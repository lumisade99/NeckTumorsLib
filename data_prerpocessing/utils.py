"""
Вспомогательные функции для предобработки данных и формирования датасета
The module contains functions for data preprocessing and dataset preparation
"""
from os import listdir
from pathlib import Path
from typing import List

import numpy as np
import pydicom


def add_dicom_extension(path: str) -> None:
    """
    Добавляет расширения .dcm для изображений, находящихся в указанной директории
    :param path: директория
    :return:
    """
    files = [f for f in listdir(path)]
    for file in files:
        if file[-1] != 'm':
            p = Path(path + '/' + file)
            p.rename(p.with_suffix('.dcm'))


def get_pixels_hu(scans: List[pydicom.dataset.FileDataset]) -> np.array:
    """
    Переводит стек изображений к шкале Хаунсфильда
    :param scans: контейнер с прочитанными dicom-файлами
    :return: многомерный массив предобработанных пикселей
    """
    image = np.stack([s.pixel_array for s in scans])
    image = image.astype(np.int16)

    intercept = scans[0].RescaleIntercept
    slope = scans[0].RescaleSlope

    if slope != 1:
        image = slope * image.astype(np.float64)
        image = image.astype(np.int16)

    image += np.int16(intercept)

    return np.array(image, dtype=np.int16)

def read_dcms_from_path(path: str) -> List[pydicom.dataset.FileDataset]:
    """
    Читает dicom-файлы, находящиеся в указанной директории
    :param path: путь
    :return: массив с прочитанными dicom-изображениями
    """
    scans = []
    for scan in listdir(path):
        ds = pydicom.dcmread([path] + scan)
        scans.append(ds)
    return scans

