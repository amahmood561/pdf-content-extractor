# PDF Content Extractor

**PDF Content Extractor** is a Python tool designed to extract content from PDF files, including text, tables, and images. It provides a command-line interface (CLI) for easy usage and supports batch processing of multiple PDFs. The project can be useful for data analysis, document processing, automation tasks, or anyone needing to extract information from PDFs.

## Features

- **Text Extraction**: Extracts all text from a PDF and saves it to a `.txt` file.
- **Table Extraction**: Extracts tables and saves them as CSV files.
- **Image Extraction**: Extracts images embedded in PDF pages and saves them as image files.
- **Batch Processing**: Supports batch processing for multiple PDF files.
- **Command-Line Interface (CLI)**: Simple and easy-to-use CLI for executing tasks.
- **Basic Logging**: Prints extraction status and file output locations for better tracking.

## Project Structure

```
pdf-content-extractor/
├── extractor/
│   ├── __init__.py
│   ├── text_extractor.py        # Module for text extraction
│   ├── table_extractor.py       # Module for table extraction
│   ├── image_extractor.py       # Module for image extraction
├── tests/
│   ├── test_text_extractor.py   # Unit tests for text extraction
│   ├── test_table_extractor.py  # Unit tests for table extraction
│   ├── test_image_extractor.py  # Unit tests for image extraction
├── scripts/
│   ├── batch_process.py         # Batch processing script
├── requirements.txt             # List of dependencies
├── README.md                    # Project documentation
├── LICENSE                      # License information
├── setup.py                     # Setup file for packaging
└── main.py                      # CLI for individual file processing
```

## Prerequisites

Make sure you have the following installed:
- **Python 3.8+**
- **Redis** (if you choose to use Celery in the future for background tasks)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/pdf-content-extractor.git
   cd pdf-content-extractor
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

You can use the tool from the command line to extract content from a single PDF file or batch process multiple PDFs in a directory.

### 1. Extract Content from a Single PDF (`main.py`)

To use the CLI for a single PDF, run the following command:

#### Extract Text
```bash
python main.py /path/to/pdf/file.pdf --text /path/to/output.txt
```

#### Extract Tables
```bash
python main.py /path/to/pdf/file.pdf --tables /path/to/output/directory
```

#### Extract Images
```bash
python main.py /path/to/pdf/file.pdf --images /path/to/output/directory
```

#### Example Command for Multiple Options
```bash
python main.py /path/to/pdf/file.pdf --text /path/to/output.txt --tables /path/to/output/tables --images /path/to/output/images
```

### 2. Batch Processing (`batch_process.py`)

You can also batch process all PDF files in a directory:

#### Example Batch Process Command
```bash
python scripts/batch_process.py /path/to/input/directory /path/to/output/directory --text --tables --images
```

### Command-Line Arguments

- **`pdf_path` / `input_dir`**: Path to the input PDF file or directory containing multiple PDFs.
- **`output_dir`**: Directory where the extracted content will be saved.
- **`--text`**: Extract text and save it as `.txt`.
- **`--tables`**: Extract tables and save them as `.csv`.
- **`--images`**: Extract images and save them as `.png`.

## Running Unit Tests

To run the unit tests, use the following command:
```bash
python -m unittest discover tests
```

## Configuration

You can add custom configuration settings, such as paths or parameters, in the `config/settings.py` file.

## Example Workflow

1. Extract text from a PDF:
   ```bash
   python main.py example.pdf --text output.txt
   ```

2. Extract tables to a specific directory:
   ```bash
   python main.py example.pdf --tables output_tables/
   ```

3. Batch process multiple PDFs:
   ```bash
   python scripts/batch_process.py input_pdfs/ output/ --text --tables --images
   ```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Make your changes and ensure the tests pass.
4. Submit a pull request.

## Future Enhancements

- Add support for background processing with Celery.
- Implement a web interface for the tool.
- Add more advanced text and table extraction options.
- Improve logging and error handling.

## Contact

Feel free to reach out with any questions or suggestions:
- **Email**: [amahmood561@gmail.com](mailto:[amahmood561@gmail.com)
- **GitHub**: [https://github.com/amahmood561](https://github.com/amahmood561)

---

