# tests/test_text_extractor.py
import unittest
import os
from extractor.text_extractor import extract_text_from_pdf

class TestTextExtractor(unittest.TestCase):
    def setUp(self):
        self.sample_pdf = 'sample.pdf'  # Provide a sample PDF file for testing
        self.output_txt = 'output.txt'

    def test_extract_text(self):
        extract_text_from_pdf(self.sample_pdf, self.output_txt)
        # Check if the output file was created
        self.assertTrue(os.path.exists(self.output_txt))
        # Verify that the extracted text contains expected content (modify as needed)
        with open(self.output_txt, 'r') as f:
            text = f.read()
        self.assertIn('Sample', text)

    def tearDown(self):
        # Clean up by deleting the generated output file
        if os.path.exists(self.output_txt):
            os.remove(self.output_txt)

if __name__ == "__main__":
    unittest.main()
