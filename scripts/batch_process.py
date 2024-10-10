# scripts/batch_process.py

#This script will allow batch processing of multiple PDF files, providing options to extract text, tables, and images for all files in a specified directory.


import os
import argparse
from extractor.text_extractor import extract_text_from_pdf
from extractor.table_extractor import extract_tables_from_pdf
from extractor.image_extractor import extract_images_from_pdf

def batch_process(directory, output_dir, text=False, tables=False, images=False):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each PDF file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(directory, filename)
            base_name = os.path.splitext(filename)[0]
            print(f'Processing {pdf_path}...')

            if text:
                text_output = os.path.join(output_dir, f'{base_name}.txt')
                extract_text_from_pdf(pdf_path, text_output)

            if tables:
                table_output_dir = os.path.join(output_dir, f'{base_name}_tables')
                if not os.path.exists(table_output_dir):
                    os.makedirs(table_output_dir)
                extract_tables_from_pdf(pdf_path, table_output_dir)

            if images:
                image_output_dir = os.path.join(output_dir, f'{base_name}_images')
                if not os.path.exists(image_output_dir):
                    os.makedirs(image_output_dir)
                extract_images_from_pdf(pdf_path, image_output_dir)

def main():
    parser = argparse.ArgumentParser(description="Batch PDF Content Extractor")
    parser.add_argument("input_dir", help="Directory containing PDF files")
    parser.add_argument("output_dir", help="Directory to save the extracted content")
    parser.add_argument("--text", action="store_true", help="Extract text from PDFs")
    parser.add_argument("--tables", action="store_true", help="Extract tables from PDFs")
    parser.add_argument("--images", action="store_true", help="Extract images from PDFs")
    
    args = parser.parse_args()

    batch_process(args.input_dir, args.output_dir, text=args.text, tables=args.tables, images=args.images)

if __name__ == "__main__":
    main()
