# main.py
import argparse
import os
from extractor.text_extractor import extract_text_from_pdf
from extractor.table_extractor import extract_tables_from_pdf
from extractor.image_extractor import extract_images_from_pdf

def main():
    parser = argparse.ArgumentParser(description="PDF Content Extractor")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("--text", help="Extract text to a specified .txt file", metavar="output.txt")
    parser.add_argument("--tables", help="Extract tables to a specified directory", metavar="output_dir")
    parser.add_argument("--images", help="Extract images to a specified directory", metavar="output_dir")
    
    args = parser.parse_args()

    if not os.path.exists(args.pdf_path):
        print(f"The file {args.pdf_path} does not exist.")
        return

    if args.text:
        extract_text_from_pdf(args.pdf_path, args.text)

    if args.tables:
        if not os.path.exists(args.tables):
            os.makedirs(args.tables)
        extract_tables_from_pdf(args.pdf_path, args.tables)

    if args.images:
        if not os.path.exists(args.images):
            os.makedirs(args.images)
        extract_images_from_pdf(args.pdf_path, args.images)

if __name__ == "__main__":
    main()
