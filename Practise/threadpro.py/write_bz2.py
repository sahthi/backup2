import bz2
content="lots of content here"
with bz2.BZ2File('file.bz2','wb') as f:
       f.write(content)




