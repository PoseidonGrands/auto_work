import pdfkit
import os

from pydocx import PyDocX


# url网站内容转pdf
pdfkit.from_url('https://www.bilibili.com/', 'test.pdf')

# html转pdf
html = """
<html>
<head>
<meta charset="utf-8" />
</head>
<body>
<p>你好</p>
</body>
</html>
"""
pdfkit.from_string(html, 'test_2.pdf')

# word转pdf
word_name = '简历1'
# word_html = PyDocX.to_html('简历1.docx')
# word_html = PyDocX.to_html(word_name + '.docx')
# pdfkit.from_string(word_html, word_name + '.pdf')

# 指定要转换的 Word 文档路径和输出的 PDF 文件路径
word_file = os.path.join(os.getcwd(), "test_2.docx")
pdf_file = os.path.join(os.getcwd(), "test666.pdf")

# word转pdf问题未解决
