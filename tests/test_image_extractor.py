# tests/test_image_extractor.py
import unittest
import os
from extractor.image_extractor import extract_images_from_pdf

class TestImageExtractor(unittest.TestCase):
    def setUp(self):
        self.sample_pdf = 'sample_with_images.pdf'  # Provide a sample PDF with images
        self.output_dir = 'test_images'

    def test_extract_images(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        extract_images_from_pdf(self.sample_pdf, self.output_dir)
        # Check if at least one image file was created
        files = os.listdir(self.output_dir)
        image_files = [f for f in files if f.endswith('.png')]
        self.assertGreater(len(image_files), 0)

    def tearDown(self):
        # Clean up by deleting the generated image files
        if os.path.exists(self.output_dir):
            for file in os.listdir(self.output_dir):
                os.remove(os.path.join(self.output_dir, file))
            os.rmdir(self.output_dir)

if __name__ == "__main__":
    unittest.main()
