#PDF Protector App this is a test

#start in the command prompt with "pip3 install PyPDF2"

from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter

pdf_in_file = open("test.pdf",'rb')

inputpdf = PdfFileReader(pdf_in_file)
pages_no = inputpdf.numPages
output = PdfFileWriter()

for i in range(pages_no):
    inputpdf = PdfFileReader(pdf_in_file)
    
    output.addPage(inputpdf.getPage(i))
    output.encrypt('password')

    with open("test_protected.pdf", "wb") as outputStream:
        output.write(outputStream)

pdf_in_file.close()