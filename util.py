# importing required modules
import PyPDF2
from PyPDF2 import PdfReader

# reader = PdfReader("book1.pdf")
# page = reader.pages[52]
# print(page.extract_text())

# creating a pdf file object
pdfFileObj = open('./books/book7.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(70)

# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()