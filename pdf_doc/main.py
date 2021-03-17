import PyPDF2
pdfFileObj = open('201CS132 - Md Rakib Hasan - SM110 - Report 1.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfObj = pdfReader.getPage(0)
print(pdfObj.extractText())