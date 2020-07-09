#Script for counting booklet printing page ordering
#Allows you to make dual-sided booklets in various formats, using basic A4 paper

from pyperclip import copy as CopyToClipboard
from argparse import ArgumentParser
from argparse import RawTextHelpFormatter

#Take args
#Adding ArgumentParser with formatting in help and without default help page
parser = ArgumentParser(add_help=False, formatter_class=RawTextHelpFormatter)
parser.add_argument("pages", type=int, help="Number of pages in book.")
parser.add_argument("format", type=str, choices = ["A4","A5","A6","A7","A8"], help="Booklet format and size.")
parser.add_argument("-p","--parts", type=int, default = 1, help="Divide bookbind pages on equal parts.\nWARNING: Output may contain empty pages!\n(default = 1)")
parser.add_argument("-e","--empty", type=int, default = 1, help="Page number, which will be printed instead\nof blank pages in the end of booklet.\nWARNING: 0 value may be throwed while printing!\n(default = 1)")
parser.add_argument("-m","--ms_office_fix", action='store_true', help="\nSlice output to avoid limitation\nin MS Office products (255 chars).\n(default = false)")
parser.add_argument("-n","--no_buffer", action='store_true', help="\nDo not copy output to buffer.\n(default = false)")
parser.add_argument("-h","--help", action='help', help="\nShow this help message and exit.\n(default = false)")
args = parser.parse_args()

#Main function
def CreateBooklet(PagesCount, StartPage, Format, EmptyPageValue, MSOfficeFix, NoBuffer):
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
    for i in range(StartPage, PagesCount+StartPage):
        Book.append(i)
        Booklet.append(0)
    #Adding empty pages to the books
    LastPages = PagesCount % PagesOnList
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
        exit()
    #Output
    #print(Format + ":")
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
        if CopyToBuffer == True and NoBuffer == False:
            CopyToClipboard(Output)
            print("(Copied to clipboard)")
    #Details
    #print("Empty pages: "+str(BlankPages)+" (Shown as: "+str(EmptyPageValue)+")")
    #print("A4 papers count: "+str(PagesCount//PagesOnList)+" ("+str(PagesOnList)+" pages on each dual-sided paper)")

#Start here
PagesCount = args.pages
Format = args.format
Parts = args.parts
EmptyPageValue = args.empty
MSOfficeFix = args.ms_office_fix
NoBuffer = args.no_buffer
#Check negative args
if PagesCount < 0:
    print("Number of pages should be positive")
    exit()
#Check parts count
if (Parts < 1 or Parts > PagesCount):
    print("Wrong number of parts: "+str(Parts))
    exit()
#Check parts division
if PagesCount % Parts != 0:
    print("Not balanced parts (PagesCount % Parts != 0)")
    exit()
#No buffer when few parts
if Parts != 1:
    NoBuffer = True
#Countig pages in one part
PagesInPart = PagesCount//Parts
StartPos = 0
for i in range(Parts):
    #Call main function
    CreateBooklet(PagesInPart, StartPos*PagesInPart+1, Format, EmptyPageValue, MSOfficeFix, NoBuffer)
    StartPos +=1

