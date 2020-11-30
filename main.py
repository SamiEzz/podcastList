

def getLinks():
    linksList=[]
    # Using readlines() 
    file1 = open('nplop', 'r') 
    Lines = file1.readlines() 
    
    # Strips the newline character 
    for line in Lines: 
        lineStrip = line.strip()
        if(lineStrip.find("histoire")>0):
            linksList.append(lineStrip)
            print(lineStrip)

    return linksList

def main():
    linksList = getLinks()
    #system("wget "+str(linksList[0]))

main()