import PyPDF2
import os
def pdf_merge():
    merge_pdf = PyPDF2.PdfFileMerger()
    for pdf in os.listdir('./'):
        if os.path.splitext(pdf)[1] == '.pdf':
            print(pdf, "merged")
            merge_pdf.append(pdf)
    merge_pdf.write('super.pdf')
    print("Merging Completed!")
    with open('super.pdf', 'rb') as result_pdf:
        reader = PyPDF2.PdfFileReader(result_pdf)
        print(reader.numPages)

pdf_merge()