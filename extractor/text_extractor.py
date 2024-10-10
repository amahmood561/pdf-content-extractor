# extractor/text_extractor.py
import PyPDF2

def extract_text_from_pdf(pdf_path, output_txt_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() or ''
    
    with open(output_txt_path, 'w') as text_file:
        text_file.write(text)
    print(f'Text extracted to {output_txt_path}')
