# extractor/image_extractor.py
import pdfplumber
from PIL import Image

def extract_images_from_pdf(pdf_path, output_dir):
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            images = page.images
            for j, image in enumerate(images):
                image_data = image['data']
                image_path = f'{output_dir}/image_page_{i+1}_image_{j+1}.png'
                img = Image.frombytes('RGB', (image['width'], image['height']), image_data)
                img.save(image_path)
                print(f'Image saved to {image_path}')
