import torch
import torch.nn as nn
from torchvision import transforms as T
from torchvision.models import resnet50
import onnxruntime as ort
from config import ONNX


device = 'cpu'
dictionary = {
    'бледная поганка': 0,
    'боровик': 1,
    'волнушка розовая': 2,
    'груздь': 3,
    'дождевик': 4,
    'лиловка лиловоногая': 5,
    'лисичка': 6,
    'ложнодождевик': 7,
    'ложноопенок серно-желтый': 8,
    'моховик зеленый': 9,
    'мухомор красный': 10,
    'опенок осенний': 11,
    'Подберезовик': 12,
    'Подосиновик': 13,
    'польский гриб': 14,
    'рядовка тигровая': 15,
    'сатангриб': 16,
    'сморчок': 17,
    'шампиньон желтокожий': 18
 }
reverse_dictionary = {value : key for key, value in dictionary.items()}


def prediction(image_pil):

    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]

    transforms = T.Compose([
        T.Resize(size=(128,128)),
        T.PILToTensor(),
        T.ConvertImageDtype(torch.float),
        T.Normalize(mean=mean, std=std),
    ])

    image_tensor = transforms(image_pil)
    #prepare image to onnx
    image_tensor = image_tensor.unsqueeze(0).detach().cpu().numpy()

    print(image_tensor.shape)

    ort_session = ort.InferenceSession(ONNX)
    ort_inputs = {ort_session.get_inputs()[0].name: image_tensor}
    ort_outputs = ort_session.run(None, ort_inputs)[0][0]
    softmax = nn.Softmax(dim=0)(torch.tensor(ort_outputs)).detach().numpy()
    
    probability = [(name,proba) for name, proba in enumerate(softmax)]
    probability = sorted(probability, key=lambda x: x[-1], reverse=True)[:3]

    answer = {}
    for element in probability:
        answer[reverse_dictionary[element[0]]] = f'Вероятность - {round(element[-1]* 100, 4)}%'

    return answer



