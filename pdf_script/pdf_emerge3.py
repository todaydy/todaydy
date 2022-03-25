from PyPDF2 import PdfFileMerger, PdfFileReader
from glob import glob
print(sorted(glob(pathname="pdf/*.pdf")))

mergepdf = PdfFileMerger()
for temp in sorted(glob(pathname="pdf/*.pdf")):
#for temp in b:
   mergepdf.append(PdfFileReader(temp))
mergepdf.write("all.pdf")
