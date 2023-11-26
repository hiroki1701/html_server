import markdown
import sys

# コマンドライン引数からMarkdownファイル名を取得
if len(sys.argv) < 2:
    print("使用方法: python script.py <markdownファイル名>")
    sys.exit(1)

markdown_file = sys.argv[1]
html_file = markdown_file.replace('.md', '.html')

# Markdownファイルの読み込み（UTF-8エンコーディングを指定）
with open(markdown_file, 'r', encoding='utf-8') as f:
    text = f.read()

# MarkdownをHTMLに変換
html_content = markdown.markdown(text)

# UTF-8メタタグを含むHTMLの基本構造を作成
html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>{markdown_file}</title>
</head>
<body>
{html_content}
</body>
</html>
"""

# HTMLファイルとして保存（UTF-8エンコーディングを指定）
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)