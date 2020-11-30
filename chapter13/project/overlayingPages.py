import PyPDF2

# Create a pdf raeder object
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))

# Create a pdf writer object
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

# Loop through from page 1 up to last 
# page of minutesminutes.pdf
for pageNum in range(1, pdfReader.numPages):
	pageObj = pdfReader.getPage(pageNum)
	pdfWriter.addPage(pageObj)

# Create a new pdf file and write to it
resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()