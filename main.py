from docx import Document

docs = []
docsTitles=[]

# docsTitles.append('test/Teste1.docx')
docsTitles.append('test/text1.docx')
docsTitles.append('test/text2.docx')

i = 0
for item in docsTitles:
    docs.append(Document(item))
    if (i != 0):
        docs[0].add_page_break()
        for element in docs[i].element.body:
            docs[0].element.body.append(element)
    i = i + 1
docs[0].save('test/testReport.docx')