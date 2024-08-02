import PyPDF2
import os



def waterMarkPDF(stamp_pdf, target_pdf, new_name):

    if stamp_pdf and target_pdf in os.listdir('./'):

        template = PyPDF2.PdfFileReader(open(f'{target_pdf}', 'rb'))

        watermark = PyPDF2.PdfFileReader(open(f'{stamp_pdf}', 'rb'))

        output = PyPDF2.PdfFileWriter()

        for i in range(template.getNumPages()):
            page = template.getPage(i)
            page.mergePage(watermark.getPage(0))
            output.addPage(page)
        with open(f'{new_name}.pdf', 'wb') as file:
            output.write(file)


new_name = str(input('Enter the new pdf name:'))

waterMarkPDF('wtr.pdf', 'super.pdf', new_name)
