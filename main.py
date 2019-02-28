from Photo import Photo
from Slide import Slide

import sys

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
    return pairMatrix



def getNumberOfTags(p1, p2):
    tags = p1.tags
    for i in range(len(p2.tags)):
        if p2.tags[i] not in tags:
            tags.append(p2.tags[i])
    return len(tags)

def printPairs(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            sys.stdout.write(str(matrix[i][j])+ " ")
        print ()


def generateSlides(photos) -> [Slide]:

    verticals = combineVertical(photos)
    horitzonalList = map(lambda x : x.horitzonality ,photos)

    return [0]

def main(filename):

    photos = Photo.takeInput(filename)
    slides = generateSlides(photos)
    Slide.printSlides(slides)


if __name__ == "__main__":
    
    main("deneme")