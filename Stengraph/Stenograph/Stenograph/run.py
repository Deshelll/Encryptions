from ctypes.wintypes import PINT
import Stenograph
import Extract


source_image = 'C:\\Users\\early\\Desktop\\Stengraph\\Stenograph\\img\\3.png'
stego_image = 'C:\\Users\\early\\Desktop\\Stengraph\\Stenograph\\img\\4.png'
text_to_embed = 'Hello world'

Stenograph.embed_text_in_image(source_image, text_to_embed, stego_image)

extracted_text = Extract.extract_text_from_image(stego_image)
print("VOT TEXT:", extracted_text)
