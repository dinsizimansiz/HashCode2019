#!/usr/bin/env python3

import sys
import os


from util import Photo, Slide


def combineVertical(photos):
    vertLists = []
    for i in range(len(photos)):
        if not photos[i].horizonality:
            vertLists.append(photos[i])
            if len(vertLists) == 2000:
                break
    if len(vertLists) == 0:
        return ([],[])
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


def createMaxPair(verticalPhotos,pairMatrix):
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
        verticalPairs.append(Slide([verticalPhotos[x], verticalPhotos[y]]))
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
            sys.stdout.write(str(matrix[i][j]) + " ")
        print()


def getInterestMatrix(slides):
    interestMatrix = []
    for i in range(len(slides)):
        interestMatrix.append([])
        for j in range(len(slides)):
            interestMatrix[i].append(-1)
    for i in range(len(slides)):
        for j in range(i+1,len(slides)):
            interestMatrix[i][j] = slides[i].getInterest(slides[j])
    return interestMatrix


def generateSlides(photos) -> [Slide]:
    slides = []
    (verticalPhotos,pairMatrix) = combineVertical(photos)
    if verticalPhotos != []:
        verticalSlides = createMaxPair(photos,verticalPhotos,pairMatrix)
    else:
        verticalSlides = []
    horizontalSlides = list(map(lambda photo : Slide(photo),filter(lambda x : x.horizonality ,photos)))
    tempSlides = horizontalSlides[0:6000] + verticalSlides
    interestMatrix = getInterestMatrix(tempSlides)
    array = [False for i in range(len(tempSlides))]
    count = len(tempSlides)
    x = -1
    y = -1
    maxNumber = -1
    for i in range(len(tempSlides)):
        for j in range(len(tempSlides)):
            if(interestMatrix[i][j] > maxNumber):
                x = i
                y = j
                maxNumber = interestMatrix[i][j]
    interestMatrix[x][y] = -1
    count -= 2
    slides.append(tempSlides[x])
    slides.append(tempSlides[y])
    array[x] = True
    array[y] = True
    while(count):
        maxNumber = -1
        newX = -1
        newY = -1
        for i in range(len(interestMatrix)):
            if(interestMatrix[i][y] > maxNumber and not array[i]):
                maxNumber = interestMatrix[i][y]
                newX = i
                newY = y
        y = newX
        # print(interestMatrix[newX][newY])
        interestMatrix[newX][newY] = -1
        array[newX] = True
        slides.append(tempSlides[newX])
        count -= 1

    #return  verticalSlides + horizontalSlides
    return slides


def main():
    inputs = [os.path.join(".", "inputs", path) for path in os.listdir("./inputs")]
    outputs = []
    for inp in inputs:
        outputs.append(os.path.join(".", "outputs", os.path.basename(inp)))

    for inp, out in zip(inputs, outputs):
        photos = Photo.takeInput(inp)
        
        print("Processing:", inp)
        slides = generateSlides(photos)
        Slide.printSlides(slides, filename=open(out, "w"))


if __name__ == "__main__":
    main()
