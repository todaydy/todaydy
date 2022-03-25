##文件名必须首先命名为数字如1.pdf, 2.pdf, 3.pdf
import os
from PyPDF2 import PdfFileMerger

#target_path='/Users/lenita/Desktop/pdf/'
pdf_lst = [f for f in os.listdir() if f.endswith('.pdf')]

tmp = []
for item in pdf_lst:
   tmp.append(item[:-4])
res = [int(i) for i in tmp if isinstance(i, str)]

ss = sorted(res)
ll = []
for j in ss:
   sj = str(j)+".pdf"
   ll.append(sj)

pdf_lst = [os.path.join(os.getcwd(), filename) for filename in ll]

file_merger = PdfFileMerger()
for pdf in pdf_lst:
   file_merger.append(pdf)     #合并pdf
#file_merger.write('/Users/lenita/Desktop/merged.pdf')
file_merger.write('merged.pdf')

