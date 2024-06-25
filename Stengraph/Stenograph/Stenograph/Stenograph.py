
from PIL import Image
import numpy as np

def embed_text_in_image(image_path, text, output_path):
    img = Image.open(image_path)
    
    # Проверяем, поддерживает ли изображение альфа-канал
    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        img = img.convert("RGBA")
    else:
        img = img.convert("RGB")

    data = np.array(img)

    # Преобразовать текст в двоичный формат
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    binary_len = len(binary_text)

    # Внедрить двоичный текст в изображение
    index = 0
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if index < binary_len:
                # Изменить наименее значимый бит первого канала для внедрения текста
                data[i, j, 0] = (data[i, j, 0] & ~1) | int(binary_text[index])
                index += 1
            else:
                break
        if index >= binary_len:
            break

    # Сохранить модифицированное изображение
    new_img = Image.fromarray(data)
    new_img.save(output_path)


    