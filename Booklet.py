#This program counts page order for printing dual side booklets on A4 lists

from pyperclip import copy as CopyToClipboard
from argparse import ArgumentParser

#Take args
parser = ArgumentParser()
parser.add_argument("pages", type=int, help="number of pages in book")
parser.add_argument("-f","--format", type=str, choices = ["A4","A5","A6","A7","A8"], default = "A5", help="booklet format and size (default = A5)")
parser.add_argument("-e","--empty_page_value", type=int, default = 1, help="page number, which will be printed instead of blank pages in the end of booklet (default = 1)")
parser.add_argument("-m","--ms_office_limit", action='store_true', help="slice output to avoid limitation in MS Office products (255 chars) (default = false)")
args = parser.parse_args()
PagesCount = args.pages
Format = args.format
EmptyPageValue = args.empty_page_value
MSOfficeFix = args.ms_office_limit

#Some defaults
MSOfficeMaxPages = 255
CopyToBuffer = True
#Formats dictionary
Formats = {"A4":2, "A5":4, "A6":8, "A7":16, "A8":32}
PagesOnList = Formats[Format]
BlankPages = 0
LastPages = 0
Book = []
Booklet = []

#Create normal book and empty booklet
for i in range(PagesCount):
    Book.append(i+1)
    Booklet.append(0)
#Adding empty pages to the books
LastPages = PagesCount%PagesOnList
if(LastPages != 0):
    BlankPages = PagesOnList-LastPages
for i in range(BlankPages):
    Book.append(EmptyPageValue)
    Booklet.append(0)
#Include empty pages in total number of pages
PagesCount += BlankPages
#Function for A5 booklet
def BookletA5():
    Booklet[::4] = Book[:PagesCount//2-1:-2]
    Booklet[1::4] = Book[:PagesCount//2:2]
    Booklet[2::4] = Book[1:PagesCount//2:2]
    Booklet[3::4] = Book[-2:PagesCount//2-1:-2]
if Format == "A4":
    #Simple book
    Booklet = Book
elif Format == "A5":
    #Slicing pages for dual sided A5 booklet (flip on short edge)
    BookletA5()
elif Format == "A6":
    BookletA5()
    #Replacing pages for dual sided A6 booklet (flip on long edge)
    for Page in range(PagesCount//PagesOnList):
        i = Page*PagesOnList
        List = Booklet[i:i+PagesOnList]
        Booklet[i+2:i+4] = List[4:6]
        Booklet[i+4:i+6] = List[2:4]
elif Format == "A7":
    BookletA5()
    #Replacing pages for dual sided A7 booklet (flip on short edge)
    for Page in range(PagesCount//PagesOnList):
        i = Page*PagesOnList
        List = Booklet[i:i+PagesOnList]
        Booklet[i+2:i+4] = List[4:6]
        Booklet[i+4:i+6] = List[8:10]
        Booklet[i+6:i+8] = List[12:14]
        Booklet[i+8:i+10] = List[6:8]
        Booklet[i+10:i+12] = List[2:4]
        Booklet[i+12:i+14] = List[14:16]
        Booklet[i+14:i+16] = List[10:12]
elif Format == "A8":
    BookletA5()
    #Replacing pages for dual sided A8 booklet (flip on long edge)
    for Page in range(PagesCount//PagesOnList):
        i = Page*PagesOnList
        List = Booklet[i:i+PagesOnList]
        Booklet[i+2:i+4] = List[4:6]
        Booklet[i+4:i+6] = List[8:10]
        Booklet[i+6:i+8] = List[12:14]
        Booklet[i+8:i+10] = List[16:18]
        Booklet[i+10:i+12] = List[20:22]
        Booklet[i+12:i+14] = List[24:26]
        Booklet[i+14:i+16] = List[28:30]
        Booklet[i+16:i+18] = List[6:8]
        Booklet[i+18:i+20] = List[2:4]
        Booklet[i+20:i+22] = List[14:16]
        Booklet[i+22:i+24] = List[10:12]
        Booklet[i+24:i+26] = List[22:24]
        Booklet[i+26:i+28] = List[18:20]
        Booklet[i+28:i+30] = List[30:32]
        Booklet[i+30:i+32] = List[26:28]
else:
    print("Wrong format")
    exit
#Output
print(Format + ":")
Output = str(Booklet)
Output = str(Output).replace(" ","")
Output = str(Output).replace("[","")
Output = str(Output).replace("]","")

#Slice output for MSOffice
if (MSOfficeFix == True and len(Output) > MSOfficeMaxPages):
    #For each A4 list
    BufferOutput = ""
    PreviousOutput = ""
    #Output while len < MSOfficeMaxPages
    for Page in range(PagesCount//PagesOnList):
        i = Page*PagesOnList
        BufferOutput += str(Booklet[i:i+PagesOnList])
        BufferOutput = str(BufferOutput).replace(" ","")
        BufferOutput = str(BufferOutput).replace("[","")
        BufferOutput = str(BufferOutput).replace("]",",")
        if len(PreviousOutput + BufferOutput) - 1 > MSOfficeMaxPages:
            #Remove last comma sign
            print(PreviousOutput[:-1])
            PreviousOutput = ""
        PreviousOutput = PreviousOutput + BufferOutput
        BufferOutput = ""
    print(PreviousOutput[:-1])
else:
    #Basic output
    print(Output)
    if CopyToBuffer == True:
        CopyToClipboard(Output)
        print("(Copied to clipboard)")

#Details
print("\nEmpty pages: "+str(BlankPages)+" (Shown as: "+str(EmptyPageValue)+")")
print("A4 lists: "+str(PagesCount//PagesOnList)+" ("+str(PagesOnList)+" pages on each dual-sided list)")

