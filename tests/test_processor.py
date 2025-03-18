import unittest
from processor import convert_markdown_to_html_from_string


class TestMarkdownProcessor(unittest.TestCase):
    def test_conversion(self):

        # Sample Markdown input
        md_text = """
# Hello World
- Item 1
- **Item 2**
Visit [Google](https://google.com).
        """

        # Expected HTML output
        expected_html = """
<h1>Hello World</h1>
<ul>
    <li>Item 1</li>
    <li><strong>Item 2</strong></li>
</ul>
<p>Visit <a href="https://google.com">Google</a>.</p>
        """

        result = convert_markdown_to_html_from_string(md_text)
        self.assertEqual(result.strip(), expected_html.strip())


if __name__ == "__main__":
    unittest.main()
