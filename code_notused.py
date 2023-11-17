# importing required modules
import PyPDF2

# creating a pdf file object
ls = ['bt.pdf'
,'dowhbnload.pdf'
,'downiload.pdf'
,'download.pdf'
,'downloadf.pdf'
,'downloaehtd.pdf'
,'downloayjd.pdf'
,'downlofrfad.pdf'
,'downlowefad.pdf'
,'downloybad.pdf'
,'downrferload.pdf'
,'downsxload.pdf'
,'dowsdnloadf.pdf'
,'ETLdownload.pdf'
,'f.pdf'
,'fd.pdf'
,'kmBrpkVZSdWRWf-p0_1Djw_d9198f7867bf42f2acabc6750523dff1_Vectors-and-lists-in-R.pdf'
,'Pdownload.pdf'
,'rfe.pdf'
,'Sdownload.pdf'
,'sfv.pdf'
,'unit.pdf'
,'wdq.pdf'
,'WHdownload.pdf'
,'yrtbdr.pdf']

def write(filename):
    
    #  f.write(text) 
    #names.append(filename)
    #print(str(contents)+".pdf")  
    #l = []
    #l.append(str(contents[:-1])+".pdf")
    #print(l[0])
    #with open('filenames.txt', 'a', encoding="utf-8") as f:
           # f.write(f"{filename}"+'\n')
    for page in range(len(pdfReader.pages)):
        pageObj = pdfReader.pages[page]
        #print(pageObj.extract_text())
        pdfWriter.add_page(pageObj)
    
        #newFile = open("pdfs/renamed/"f"{filename}.pdf".format(str(filename)), 'wb')
        #pdfWriter.write(newFile)
        

   

def readnames():       
    with open('filenames.txt') as f:
        contents = f.readlines()
        print(contents[0])
        print(len(set(contents)))
        print(len(contents))
        pp = list(set([x for x in contents if contents.count(x) > 1]))
        print(len(pp))
        print(list(set([x for x in contents if contents.count(x) > 1])))
        print(list(set([x for x in contents if contents.count(x) > 0])))
        for i in range(len(contents)):    
            for j in range(len(contents)):    
               if(contents[i] == contents[j]):    
                  print(contents[j]);     
    
#with open('filenames.txt') as f:
#    contents = f.readlines()
    #for i in range(0, len(contents)):    
    #    for j in range(i+1, len(contents)):    
    #        if(contents[i] == contents[j]):    
    #           print(contents[j]);    

readnames() 
len(ls)
for index, i in enumerate((ls)):
   # print(index)
    pdfFileObj = open("pdfs/"+f'{i}', 'rb')
    #print("pdfs/"+f'{i}'+ " is in process")
# creating a pdf reader object
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    pdfWriter = PyPDF2.PdfWriter()
# printing number of pages in pdf file
    pageObj = pdfReader.pages[0]
    #print(len(pdfReader.pages))
    #print(pdfReader.pages)
    text = pageObj.extract_text()
    #print(text[0:100])
    with open('readme.txt', 'w', encoding="utf-8") as f:
         
            f.write(text[0:150].capitalize())
         
          #  f.write(text) 
    with open('readme.txt') as f:
        contents = f.readline()  
     #   print("here "+contents)
        contents2 = f.readline()
      #  print("here2 "+contents2) 
       # print(contents.find("Glossary"))
        if contents.find("Glossary") == 0:
           d = contents2.replace(':','') 
           d = d.replace('?','')
           d = d.replace(',','')
           d = d.replace(';','')
           d = d.replace("'",'')
           name1 = d[:-1]
           #print("here2 "+contents2) 
        #   print(name1)
           write("Glossary "+name1)
        else:
           d = contents.replace(':','') 
           d = d.replace('?','')
           d = d.replace(',','')
           d = d.replace(';','')
           d = d.replace("'",'')
           name2 = d[:-1]
         #  print(name2)
           write(name2)


   # print(type(contents)) 
    #print(contents)
    #d = contents.replace(':','') 
    #d = d.replace('?','')
    #d = d.replace(',','')
    #d = d.replace(';','')
    #d = d.replace("'",'')
    #d = d.replace("'",'')
    #l = []
   # name = d[:-1]
    
#print(l[0])

        #print(newFile)
# creating a page object
#print(type(contents)) 
#print(contents[:-1]) 
#pageObj = pdfReader.pages[0]
#print(pageObj)
# extracting text from page
#print(pageObj.extractText)
#print(pageObj.extract_text())
#text = pageObj.extract_text().title()
#print(text)
#with open('readme.txt', 'w') as f:
#     f.write(text)
#with open('readme.txt') as f:
#    contents = f.readline()  
#print(str(contents)+".pdf")  
#l = []
#l.append(str(contents[:-1])+".pdf")
#print(l[0])
#pdfWriter = PyPDF2.PdfWriter()

#newFile = open(l[0], 'wb')
 
# writing rotated pages to new file
#pdfWriter.write(newFile)
# closing the pdf file object
pdfFileObj.close()



def readnames():       
    with open('filenames.txt') as f:
        contents = f.readlines()
        print(contents[0])
        print(len(set(contents)))
        print(len(contents))
        pp = list(set([x for x in contents if contents.count(x) > 1]))
        print(len(pp))
        print(list(set([x for x in contents if contents.count(x) > 1])))
        print(list(set([x for x in contents if contents.count(x) > 0])))
  
def create_names(pdffiles):
    for index, i in enumerate((pdffiles)):
        pdfFileObj = open("pdfs/"+f'{i}', 'rb')
    # creating a pdf reader object
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        
    # printing number of pages in pdf file
        pageObj = pdfReader.pages[0]
        text = pageObj.extract_text()
        with open('readme.txt', 'w', encoding="utf-8") as f:
            f.write(text[0:150].capitalize())
        with open('readme.txt') as f:
            contents = f.readline()  #read line 1
            contents2 = f.readline()  #readline 2

        if contents.find("Glossary") == 0:
           d = contents2.replace(':','') 
           d = d.replace('?','')
           d = d.replace(',','')
           d = d.replace(';','')
           d = d.replace("'",'')
           name1 = d[:-1]
           write("Glossary "+name1)
        else:
           d = contents.replace(':','') 
           d = d.replace('?','')
           d = d.replace(',','')
           d = d.replace(';','')
           d = d.replace("'",'')
           name2 = d[:-1]
           write(name2)
    return pdfReader

def write(filename):
    with open('filenames.txt', 'a', encoding="utf-8") as f:
            f.write(f"{filename}"+'\n')
    pdfWriter = PyPDF2.PdfWriter()     

    for page in range(len(pdfReader.pages)):
        pageObj = pdfReader.pages[page]
        pdfWriter.add_page(pageObj)
        newFile = open("pdfs/renamed/"f"{filename}.pdf".format(str(filename)), 'wb')
        pdfWriter.write(newFile)
           
  