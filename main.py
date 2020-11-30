import json

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

def getReadme():
    linksList=[]
    # Using readlines() 
    file1 = open('nplop', 'r') 
    Lines = file1.readlines() 
    print("# Podcasts Histoire :")
    # Strips the newline character 
    for line in Lines: 
        lineStrip = line.strip()
        title=lineStrip[lineStrip.find("histoire")+9:lineStrip.find(".mp3?")]
        title=title.replace("-"," ")
        link = lineStrip[lineStrip.find("http"):-1]
        #if(lineStrip.find("histoire")>0):
        linksList.append(lineStrip)
        #print("## "+title+" :")
        print("## ["+title+"]"+"("+link+")")


def getJson():
    linksList={}
    # Using readlines() 
    file1 = open('nplop', 'r') 
    Lines = file1.readlines() 
    print("# Podcasts Histoire :")
    # Strips the newline character 
    for line in Lines: 
        lineStrip = line.strip()
        title=lineStrip[lineStrip.find("icon")+4:lineStrip.find(".mp3?")]
        title=title.replace("-"," ")
        link = lineStrip[lineStrip.find("http"):-1]
        if(lineStrip.find("icon")>0):
            linksList[title]=link
            #print("## "+title+" :")
    print(json.dumps(linksList, indent=4,separators=(',', ':')))

def main():
    getReadme()
    #linksList = getLinks()
    #system("wget "+str(linksList[0]))

main()