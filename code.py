from PyPDF2 import PdfFileWriter, PdfFileReader

def order_pages():

    for i in ordem:
        lista_ordenada.append(i - 1)

    output_pdf = PdfFileWriter()

    with open(original_file, 'rb') as readfile:
        input_pdf = PdfFileReader(readfile)
#        total_pages = input_pdf.getNumPages()

        for page in lista_ordenada:
            output_pdf.addPage(input_pdf.getPage(page))

        with open(target_file, "wb") as writefile:
            output_pdf.write(writefile)

def merge_pdf():

    pdf2merge = [capa, report, capa_details, appendix]

    pdfWriter = PdfFileWriter()

    # loop through all PDFs
    for filename in pdf2merge:
        # rb for read binary
        pdfFileObj = open(filename, 'rb')
        pdfReader = PdfFileReader(pdfFileObj)
        # Opening each page of the PDF
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
    # save PDF to file, wb for write binary
    pdfOutput = open(merged_file, 'wb')
    # Outputting the PDF
    pdfWriter.write(pdfOutput)
    # Closing the PDF writer
    pdfOutput.close()

def merge_pdf_juntar():

    pdf2merge = [P1, P2, P3, P4, P5, P6, P7, P8, P9]

    pdfWriter = PdfFileWriter()

    # loop through all PDFs
    for filename in pdf2merge:
        # rb for read binary
        pdfFileObj = open(filename, 'rb')
        pdfReader = PdfFileReader(pdfFileObj)
        # Opening each page of the PDF
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
    # save PDF to file, wb for write binary
    pdfOutput = open(merged_file, 'wb')
    # Outputting the PDF
    pdfWriter.write(pdfOutput)
    # Closing the PDF writer
    pdfOutput.close()

dir = r'C:\teste'

print('Dir setado ok')


P1 = dir + '\Paginas\F1.pdf'
P2 = dir + '\Paginas\F2.pdf'
P3 = dir + '\Paginas\F3.pdf'
P4 = dir + '\Paginas\F4.pdf'
P5 = dir + '\Paginas\F5.pdf'
P6 = dir + '\Paginas\F6.pdf'
P7 = dir + '\Paginas\F7.pdf'
P8 = dir + '\Paginas\F8.pdf'
P9 = dir + '\Paginas\F9.pdf'

print ('Paginas ok')

merged_file = dir + '\merged.pdf'

merge_pdf_juntar()

print ('Paginas PF juntas ok')

capa = r'C:\teste.pdf'
report = dir + '\teste.pdf'
capa_details = r'C:\teste.pdf'
appendix = r'C:\teste.pdf'

merged_file = dir + '\Deletar.pdf'

original_file = merged_file
target_file = dir + '\target.pdf'

ordem = [1,8,10,2,3,11,4,5,6,12,7,9]
lista_ordenada = []

merge_pdf()
order_pages()

print ('Report ok')
