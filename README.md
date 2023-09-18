# RadImaLib
[![codecov](https://codecov.io/gh/lumisade99/RadImaLib/graph/badge.svg?token=ZK1KPZ2GYV)](https://codecov.io/gh/lumisade99/RadImaLib)

Python library for radiology images processing and analysing
## Table of Contents

* [Background Information](#Background-Information)
* [Dataset Description](#Dataset-Description)
* [Installation](#installation)
* [Examples](#examples)
* [Publications](#Publications)

## Background Information
The main reason for the library creation was our research interest in a 
particular disease, called paraganglioma or carotid body tumor. This tumor is located at the place of carotid artery
bifurcation and its proportion in total number of head and neck tumors is 0.5%. During te research we have collected
the image data of patients with paraganglioma and developed some methods to manipulate with it.
## Dataset Description
The dataset contains 588 records of patients with carotid body tumor. The columns of the dataset are the following:
1. **Sex** - information abount the patient's sex
2. **Age** - patient's age
3. **RescaleIntercept** - linear transformation argument
4. **RescaleSlope** - linear transformation argument
5. **PixelData** - the column contains images themselves, multidimensional arrays of pixel brightnesses, to be more
precisely 

## Installation
~~~
pip install RadImaLib
~~~

## Methods
* ~~~
  add_dicom_extension(path: str) - adds dcm-extension to filenames for a given directory
  ~~~
* ~~~
  get_pixels_hu(scans: List[pydicom.dataset.FileDataset]) - rescale pixels to Hounsfield scale
  ~~~
* ~~~
  read_dcms_from_path(path: str) - reads dicoms from a given directory
  ~~~

## Examples

## Publications
1. Ekaterina Zhabrovets, Tatyana Maximova. Designing AI Componenets for Diagnostics of Carotid Body Tumors (has been
approved to be published in upcoming volume of the journal 'Lecture Notes in Networks and Systems')
2. Жабровец Е.А., Лукина А.С. Информационное обеспечение клинических решений при диагностике редких заболеваний //
Экономика. Право. Инновации.-2023.-№3 (In Russian)
3. Котенко П.К., Жабровец Е.А. Планирование проекта по разработке системы
поддержки принятия медицинских решений при диагностике каротидных опухолей (хемодектом) // Экономика. Право. 
Инновации.-2022.-№ 2 (In Russian)