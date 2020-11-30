# password = rosebud

import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
print(pdfReader.isEncrypted)

# pageObj = pdfReader.getPage(0)
# print(pageObj)

print(pdfReader.decrypt('rosebud'))
pageObj = pdfReader.getPage(0)
# print(pageObj)
print(pageObj.extractText())