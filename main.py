import torch
from PIL import Image
import requests
from io import BytesIO
from transformers import BlipProcessor, BlipForConditionalGeneration

# Lista de URLs de imagens
image_urls = [
    "https://images.tcdn.com.br/img/img_prod/450253/osciloscopio_e_multimetro_funcao_2_em_1_profissional_et201_visor_lcd_sistema_integrado_multifunciona_1995_1_20190927211652.jpg",
    "https://images.tcdn.com.br/img/img_prod/1158281/48x38x17_montagem_painel_eletrico_quadro_comando_480x380x170_1721_1_9ff9fb836c3be53e6a4a60af5ac13fa9.png",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUg8VV3_4XLspihOaXAbgRQ8HGknXyJ2IVsw&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzs1D77a1bCl9XFMycB12gpa9UCpEoT-44jg&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSgJES9MScFWjpnetEkSNEyh-VqH5sjon-LQ&s",
    "https://comercialbatista.agilecdn.com.br/15654_1.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGmSwUHOPs66vKfa7dNU7YVuEupi4rOOpYDg&s",
    "https://m.media-amazon.com/images/I/41Q4u08JxlL._AC_UF894,1000_QL80_.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHmSlKoeq7yIwB9NtVO_786Rcfm9hrEwQUgA&s",
]

# Carregar modelo e processador
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Iterar sobre as URLs das imagens
for idx, url in enumerate(image_urls):
    try:
        # Baixar e abrir a imagem
        response = requests.get(url)
        image = Image.open(BytesIO(response.content)).convert("RGB")

        # Processar imagem
        inputs = processor(images=image, return_tensors="pt")

        # Gerar legenda
        output = model.generate(**inputs)
        caption = processor.decode(output[0], skip_special_tokens=True)

        # Exibir legenda
        print(f"[Imagem {idx + 1}] Legenda gerada: {caption}\n")
    except Exception as e:
        print(f"[Imagem {idx + 1}] Erro ao processar imagem: {e}\n")
