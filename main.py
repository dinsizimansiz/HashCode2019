from Photo import Photo
from Slide import Slide

import sys
import os



def combineVertical(photos):
    vertLists = []
    for i in range(len(photos)):
        if not photos[i].horizonality:
            vertLists.append(photos[i])
    pairMatrix = []
    for i in range(len(vertLists)):
        temp = []
        for j in range(len(vertLists)):
            temp.append(-1)
        pairMatrix.append(temp)
    for i in range(len(pairMatrix)):
        for j in range(i + 1, len(pairMatrix)):
            if i == j:
                continue
            pairMatrix[i][j] = getNumberOfTags(vertLists[i], vertLists[j])
    return (vertLists,pairMatrix)

def createMaxPair(photos,verticalPhotos,pairMatrix):
    used_photos = []
    for i in range(len(verticalPhotos)):
        used_photos.append(False)
    x = -1
    y = -1
    verticalPairs = []
    while(True):
        maxNumber = -1
        for i in range(len(pairMatrix)):
            if(used_photos[i]):
                continue
            for j in range(len(pairMatrix)):
                if(used_photos[j]):
                    continue
                if(pairMatrix[i][j]>maxNumber):
                    maxNumber = pairMatrix[i][j]
                    x = i
                    y = j
        verticalPairs.append(Slide([verticalPhotos[x],verticalPhotos[y]]))
        used_photos[x] = True
        used_photos[y] = True
        flag_number = 0
        for i in range(len(used_photos)):
            if(used_photos[i]==False):
                flag_number += 1
            if(flag_number==2):
                break
        if (flag_number < 2):
            break
    return verticalPairs


def getNumberOfTags(p1, p2):
    tags = []
    for i in range(len(p1.tags)):
        tags.append(p1.tags[i])
    for i in range(len(p2.tags)):
        if p2.tags[i] not in tags:
            tags.append(p2.tags[i])
    return len(tags)

def printPairs(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            sys.stdout.write(str(matrix[i][j])+ " ")
        print ()



def getInterestMatrix(slides):

    interestMatrix = []
    
    for i,_ in enumerate(slides):
        slides.append([])
        for j in range(i):
            slides[i][j] = slides[i].getInterest(slides[j])

    return interestMatrix

def generateSlides(photos) -> [Slide]:

    slides = []
    (verticalPhotos,pairMatrix) = combineVertical(photos)
    verticalSlides = createMaxPair(photos,verticalPhotos,pairMatrix)
    horitzonalSlides = list(map(lambda photo : Slide(photo),filter(lambda x : x.horizonality ,photos)))
    #interestMatrix = getInterestMatrix(horitzonalSlides + verticalSlides)


    return  verticalSlides + horitzonalSlides
    #return slides 

def main():

    inputs = [ os.path.join(".","inputs",path) for path in os.listdir("./inputs")]
    outputs = []
    for inp in inputs :
        outputs.append(os.path.join(".","outputs",os.path.basename(inp)))
    

    for inp,out in zip(inputs,outputs):
        photos = Photo.takeInput(inp)
        

        slides = generateSlides(photos)
        Slide.printSlides(slides,filename=open(out,"w"))

if __name__ == "__main__":
    
    main()
