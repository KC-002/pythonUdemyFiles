import PyPDF2

with open('./VINAYAN Updated.pdf', 'rb') as fstPage:

    f_reader = PyPDF2.PdfFileReader(fstPage)
    copy = f_reader.getPage(0)
    result = PyPDF2.PdfFileWriter()
    result.addPage(copy)

    with open('application.pdf', 'rb') as sndPage:

        s_reader = PyPDF2.PdfFileReader(sndPage)
        for i in range(1, s_reader.getNumPages()):
            pages = s_reader.getPage(i)
            result.addPage(pages)

        with open('combined1.pdf', 'wb') as result_file:
            result.write(result_file)




