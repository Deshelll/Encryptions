from PIL import Image
import numpy as np

def extract_text_from_image(image_path):
    img = Image.open(image_path)
    # ѕреобразование изображени€ в RGB
    img = img.convert("RGB")
    data = np.array(img)

    binary_text = ''
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            # »звлекаем наименее значимый бит из первого канала пиксел€
            binary_text += str(data[i, j, 0] & 1)
            
    zero_byte_index = binary_text.find('00000000')
    if zero_byte_index != -1:
        binary_text = binary_text[:zero_byte_index]

    # ѕреобразовать двоичные данные обратно в текст
    text = ''
    for i in range(0, len(binary_text), 8):
        byte = binary_text[i:i+8]
        if len(byte) == 8:
            text += chr(int(byte, 2))

    return text
