#Importing the required packages

from docxcompose.composer import Composer
from docx import Document as Document_compose
#filename_master is name of the file you want to merge the docx file into
master = Document_compose('test/text1.docx')

composer = Composer(master)
#filename_second_docx is the name of the second docx file
doc2 = Document_compose('test/text2.docx')
#append the doc2 into the master using composer.append function
composer.append(doc2,False)
#Save the combined docx with a name
composer.save("test/combined.docx")