def segmentFormat12(aLine):
    originalaLine=aLine
    aLine=aLine.replace(" ","")
    print(aLine)
    aLineArray = []
    if (len(aLine)!=13):
        print('Error: this segment is too long or too short')
        return('Error: this segment is too long or too short\n' + originalaLine)
        print(aLine)
        return aLine
    else : 
        for i in range(0, len(aLine)):
            aLineArray.append(aLine[i])
            if (i==1 or i==3 or i==7 or i==9):
                aLineArray.append(':')
            if (i==5) :
                aLineArray.append('--> ')
    return(''.join(aLineArray))

def formatSegmentFile():
    f= open("exampleSubtitleTimestampFile.txt", "r")
    target = open("subtitlesFormatted.txt", "w+")
    lineNum = 1
    for line in f:
        newLine = str(segmentFormat12(line))
        print(newLine)
        target.write(str(lineNum)+'\n')
        lineNum+=1
        target.write(newLine+ '\n\n')
    target.write('Check subtitlesFormatted.txt for the edited text')
    target.close()
    
        
#test cases 
# segmentFormat(391234)
# segmentFormat(123546)
# segmentFormat12("123456 135663")
formatSegmentFile()

#error test cases
# segmentFormat(39123)
# segmentFormat(0)
# segmentFormat12("123456 3335663")

#add in strip so that fcn doesnt fail because of extra whitespace in a line
#[DONE]add in conditional for string !len 6 or string len!12
#[DONE] Read in lines from a text file and output formatted segments to new txt file.
