import gzip
content="lots of content here"
with open('file.txt.gz','wb') as f:
      f.write(content)
