![CustomDataset](https://img.shields.io/badge/CustomDataset-706c62?style=for-the-badge)
![DeepLearning](https://img.shields.io/badge/DeepLearning-706c62?style=for-the-badge)
![Pytorch](https://img.shields.io/badge/Pytorch-706c62?style=for-the-badge&logo=Pytorch)
![ResNet50](https://img.shields.io/badge/ResNet50-706c62?style=for-the-badge&logo=Pytorch)
![aiogram](https://img.shields.io/badge/aiogram-706c62?style=for-the-badge&logo=telegram)

## Mushroom Classification
<br />
<div align="center">
  <a>
    <img src="https://media.tenor.com/DcZBJVr8xKQAAAAC/mushroom-dance.gif" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Best-README-Template</h3>
</div>

Классификатор изображений, построенный на CNN Resnet50 и предсказывающий 19 классов грибов. Выводит три наиболее вероятных кандидата с указанием этой самой вероятности.
Цель: создать классификатор, облегчающий задачу сбора грибов, а точнее, отсечь ядовитые грибы
Что было сделано:
* собран датасет из 400-1000 изображений для каждого класса. Датасет был разбит на train, validation и test. Также, были "взвешенны" классы, сильнее штрафовать за более редкие.
* С помощью Pytroch была реализована архитектура Resnet (50 слоев, из которых 48 - convolution) с небольшими правками: последний слой был заменен на 19 выходов. 
  Обучали последний и предпоследний convolution-слой
* Полученная сеть была преобразована в ONNX-модель
* Создан простой бот на библиотеке Aiogram, принимающий фото от юзера и выдающий предсказание



