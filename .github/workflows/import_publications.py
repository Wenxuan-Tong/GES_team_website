import os
import re
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

def slugify(value):
    """
    将字符串转换为适合作为文件名的 slug 格式
    """
    value = str(value).lower()
    value = re.sub(r'[\s\W-]+', '-', value)
    value = value.strip('-')
    return value

def main():
    bib_file = "publications.bib"
    if not os.path.exists(bib_file):
        print(f"Error: {bib_file} not found!")
        return

    # 读取 publications.bib 文件
    with open(bib_file, encoding='utf-8') as bibtex_file:
        parser = BibTexParser(common_strings=True)
        parser.customization = convert_to_unicode
        bib_database = bibtexparser.load(bibtex_file, parser=parser)

    # 输出目录：content/publications
    output_dir = os.path.join("content", "publications")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    # 对于每个 BibTeX 条目，生成一个 Markdown 文件
    for entry in bib_database.entries:
        # 使用条目的 ID 作为文件名基础
        entry_id = entry.get("ID", "unknown")
        filename = slugify(entry_id) + ".md"
        file_path = os.path.join(output_dir, filename)

        # 获取出版物相关字段
        title = entry.get("title", "No Title")
        authors = entry.get("author", "Unknown Authors")
        year = entry.get("year", "1970")  # 若没有年份，默认使用 1970
        journal = entry.get("journal", "")
        booktitle = entry.get("booktitle", "")
        entry_type = entry.get("ENTRYTYPE", "").capitalize()

        # 构造一个 BibTeX 格式的字符串用于前言展示
        bibtex_str = bibtexparser.dumps({'entries': [entry]}).strip()

        # 生成 Markdown 文件内容（前言部分采用 YAML 格式）
        markdown_content = f"""---
title: "{title}"
date: "{year}-01-01"
authors: "{authors}"
publication_type: "{entry_type}"
journal: "{journal}"
booktitle: "{booktitle}"
bibtex: |
  {bibtex_str.replace('\n', '\n  ')}
---

<!--
自动生成的出版物条目。
请根据需要在此处添加摘要、链接、封面图片或其他说明信息。
-->
"""

        # 写入 Markdown 文件
        with open(file_path, "w", encoding="utf-8") as md_file:
            md_file.write(markdown_content)
            print(f"Generated file: {file_path}")

if __name__ == "__main__":
    main()
