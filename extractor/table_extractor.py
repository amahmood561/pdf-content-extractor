# extractor/table_extractor.py
import pdfplumber
import pandas as pd

def extract_tables_from_pdf(pdf_path, output_dir):
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            tables = page.extract_tables()
            for j, table in enumerate(tables):
                # Convert table to DataFrame
                df = pd.DataFrame(table[1:], columns=table[0])
                csv_file = f'{output_dir}/table_page_{i+1}_table_{j+1}.csv'
                df.to_csv(csv_file, index=False)
                print(f'Table saved to {csv_file}')
