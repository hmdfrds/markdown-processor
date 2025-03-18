import argparse
import os

from processor import convert_markdown_to_html


def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Markdown to HTML processor")
    parser.add_argument("input_file", help="Path to the input Markdown (.md) file")
    parser.add_argument(
        "--output",
        "-o",
        help="Path to the output HTML file (default: same name as input with .html extension)",
    )
    args = parser.parse_args()

    # Validate input file exists
    if not os.path.isfile(args.input_file):
        parser.error(f"Input fine not found: {args.input_file}")

    # Determine output file name
    if args.output:
        output_path = args.output
    else:
        base, _ = os.path.splitext(args.input_file)
        output_path = base + ".html"

    try:
        html_content = convert_markdown_to_html(args.input_file)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Successfully generated HTML file: {output_path}")
    except Exception as e:
        parser.error(f"An error occurred during processing: {e}")


if __name__ == "__main__":
    main()
