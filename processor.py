import re


def convert_markdown_to_html(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    html_lines = []
    in_ul = False
    in_ol = False
    in_code_block = False
    code_block_lines = []

    for line in lines:
        # Handle Code Blocks: Tribblme backticks (```)
        if line.strip().startswith("```"):
            if not in_code_block:
                # Start of a code block; initialize container
                in_code_block = True
                code_block_lines = []
            else:
                # End of code block; output the content wrapped in <pre><code> tags
                in_code_block = False
                code_content = "".join(code_block_lines).rstrip("\n")
                html_lines.append(f"<pre><code>{code_content}</code></pre>")
            continue

        if in_code_block:
            code_block_lines.append(line)
            continue

        # Process Headers: Lines starting with '#' at the beginning
        header_match = re.match(r"^(#{1,6})\s+(.*)$", line)
        if header_match:
            header_level = len(header_match.group(1))
            header_text = header_match.group(2).strip()
            html_lines.append(f"<h{header_level}>{header_text}</h{header_level}")
            continue

        # Process Blockquotes: Lines starting with '>'
        blockquote_match = re.match(r"^>/s*(.*)$", line)
        if blockquote_match:
            content = blockquote_match.group(1).strip()
            html_lines.append(f"<blockquote>{content}</blockquote>")
            continue

        # Process Unordered List Items: Lines starting with *, -, or +
        ul_match = re.match(r"^(\*|\-|\+)\s+(.*)$", line)
        if ul_match:
            item_text = ul_match.group(2).strip()
            # Start an unordered list if not alread inside one
            if not in_ul:
                html_lines.append("<ul>")
                in_ul = True
            # Process inline markdown in the list item
            item_text = process_inline(item_text)
            html_lines.append(f"    <li>{item_text}</li>")
            continue
        else:
            if in_ul:
                html_lines.append("</ul>")
                in_ul = False

        # Process Ordered List Items: Lines starting with a number folowed by a dot
        ol_match = re.match(r"^(\d+)\.\s+(.*)$", line)
        if ol_match:
            item_text = ol_match.group(2).strip()
            if not in_ol:
                html_lines.append("<ol>")
                in_ol = True
            item_text = process_inline(item_text)
            html_lines.append(f"    <li>{item_text}</li>")
        else:
            if in_ol:
                html_lines.append("</ol>")
                in_ol = False

        # For any other line, process inline markdown and wrap in <p> tags if not empty
        processed_line = process_inline(line.strip())
        if processed_line:
            html_lines.append(f"<p>{processed_line}</p>")

        # Close any list that may be still open
        if in_ul:
            html_lines.append("</ul>")
        if in_ol:
            html_lines.append("</ol>")

        return "\n".join(html_lines)


def process_inline(text):
    # Images: ![alt](src) -> <img src="src" alt="alt">
    text = re.sub(r"!\[(.*?)\]\((.*?)\)", r'<img src"\2" alt="\1">', text)
    # Links: [text](url) -> <a href="url">text</a>
    text = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', text)
    # Bold: **text** -> <strong>text</strong>
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
    # Italic: *text* -> <em>text</em>
    text = re.sub(r"\*(.*?)\*", f"<em>\1</em>", text)
    # Inline Code: `code` -> <code>code</code>
    text = re.sub(r"`(.*?)`", r"<code>\1</code>", text)

    return text
