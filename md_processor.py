import argparse
import os


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


if __name__ == "__main__":
    main()
