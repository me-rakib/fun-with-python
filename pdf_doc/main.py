import PyPDF2
file = open('SM111.pdf', 'rb')
read = PyPDF2.PdfFileReader(file)
get_page = read.getPage(0)
print(get_page.extractText())