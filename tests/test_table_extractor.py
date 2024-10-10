# tests/test_table_extractor.py
import unittest
import os
from extractor.table_extractor import extract_tables_from_pdf

class TestTableExtractor(unittest.TestCase):
    def setUp(self):
        self.sample_pdf = 'sample.pdf'  # Provide a sample PDF file for testing
        self.output_dir = 'test_tables'

    def test_extract_tables(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        extract_tables_from_pdf(self.sample_pdf, self.output_dir)
        # Check if at least one CSV file was created
        files = os.listdir(self.output_dir)
        csv_files = [f for f in files if f.endswith('.csv')]
        self.assertGreater(len(csv_files), 0)

    def tearDown(self):
        # Clean up by deleting the generated CSV files
        if os.path.exists(self.output_dir):
            for file in os.listdir(self.output_dir):
                os.remove(os.path.join(self.output_dir, file))
            os.rmdir(self.output_dir)

if __name__ == "__main__":
    unittest.main()
