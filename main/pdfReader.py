# importing required modules
import PyPDF2

# creating a pdf file object
ls = ['h.pdf']


class pdfmaster:

    def __init__(self,pdffiles):
        self.pdffiles = pdffiles
        

    def main(self):
        try:
            for index, i in enumerate((self.pdffiles)):
                pdfFileObj = open("pdfs/"+f'{i}', 'rb')
    # creating a pdf reader object
                pdfReader = PyPDF2.PdfReader(pdfFileObj)
    # printing number of pages in pdf file
                pageObj = pdfReader.pages[0]
                text = pageObj.extract_text()
                with open('readme.txt', 'w', errors='ignore' ) as f:
                    f.write(text.capitalize())
                with open('readme.txt') as f:
                    contents = f.readlines()  #read line 1
                    contents2 = f.readline()  #readline 2  
                    contents3 = f.readline()  #readline 3 
                    contents4 = f.readline()  #readline 4 
                    contents5 = f.readline()  #readline 5 
                    contents6 = f.readline()  #readline 6
                    #lf = [contents,contents2,contents3,contents4,contents5,contents6]
                    print(len(contents))
                    print(contents)
                    print(contents.index('alghamdi\n')) 
                    #contents.index('alghamdi\n')
                    print(contents.index('alghamdi\n')+1)
                    print(contents[contents.index('alghamdi\n')+1].capitalize())
                    print(contents[contents.index('alghamdi\n')+2].capitalize()[:-1])

                    result = pdfmaster.filterss(contents)
                 

                
                #lf.append(contents,contents2,contents3,contents4,contents5,contents6)
                #print(lf)           
                #res = pdfmaster.filterss(contents4,contents4)
                    with open('filenames.txt', 'a', encoding="utf-8") as f:
                        f.write(f"{result}"+'\n')
                        pdfWriter = PyPDF2.PdfWriter()     
                    for page in range(len(pdfReader.pages)):
                        pageObj = pdfReader.pages[page]
                        pdfWriter.add_page(pageObj)
                        newFile = open("pdfs/renamed/"f"{result}.pdf".format(result), 'wb')
                        pdfWriter.write(newFile)    
            pdfFileObj.close()  
        except FileNotFoundError:  
            return print("No file added, found or wrong file extenstion only pdf allowed")  
        except UnicodeDecodeError or UnicodeEncodeError or UnicodeError or TypeError:
            return print('error with unicoding')    
        finally:
            return print("Thank you")          

      

   
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
    
    def filterss(text2):
      
        #if #text1.find("alghamdi") == 0:
                #d = text2.replace(':','') 
                #d = d.replace('?','')
                #d = d.replace(',','')
                #d = d.replace(';','')
                #d = d.replace("'",'')
        result = text2[text2.index('alghamdi\n')+1].capitalize()[:-1]
        pob = text2[text2.index('alghamdi\n')]
        print(pob)
        if pob == pob.find('\n'):
            pob= text2[text2.index('alghamdi\n')-1].capitalize()[:-1]
            print(pob+"kr")
            return pob
        else:
              #  name1 = d[:-1]
            return result
       # else:
          #      d = text1.replace(':','') 
          #      d = d.replace('?','')
          #      d = d.replace(',','')
          #      d = d.replace(';','')
         #       d = d.replace("'",'')
         #       name2 = d[:-1]
              #  return name2
                
        


pdcoco = pdfmaster(ls)        
pdcoco.main()
#pdfmaster.readnames()
