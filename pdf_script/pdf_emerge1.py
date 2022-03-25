from PyPDF2 import PdfFileMerger
import os

files = sorted(os.listdir())
print(files)
#files = os.listdir()
merger = PdfFileMerger()
for file in files:
   if file[-4:] == ".pdf":
     merger.append(open(file, 'rb'))  
with open('newfile.pdf', 'wb') as fout:
   merger.write(fout)

##将脚本和PDFs放到同一文件夹里,运行
