# Markdown Processor

A simple Python-based Markdown Processor that converts Markdown (.md) files to HTML.

## Features

- Converts Markdown headers to HTML headings (h1–h6).
- Supports blockquotes, unordered and ordered lists.
- Handles inline formatting for **bold**, *italic*, links, images, and inline code.
- Processes code blocks (triple backticks).
- Command-line interface (CLI) for file conversion.

## Requirements

- Python 3.6 or higher (uses only standard libraries)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hmdfrds/markdown-processor.git
   cd markdown-processor

## Usage

Run the processor from the command line:

```bash
python md_processor.py input.md [--output output.html]
```

If `--output` is omitted, the HTML file will be saved with the same base name as the input file.

## Testing

```bash
python -m unittest tests/test_processor.py
```

## License

MIT License.
