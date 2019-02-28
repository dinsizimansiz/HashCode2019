from Photo import Photo
from Slide import Slide

def combineVertical(photos):
    vertLists = []
    for i in range(len(photos)):
        if not photos[i].horizonality:
            vertLists.append(photos[i])
    pairMatrix = []
    for i in range(len(photos)):
        temp = []
        for j in range(len(photos)):
            temp.append(-1)
        pairMatrix.append(temp)

    for i in range(len(pairMatrix)):
        for j in range(i + 1, len(pairMatrix)):
            if i == j:
                continue
            pairMatrix[i][j] = getNumberOfTags(vertLists[i], vertLists[j])



def getNumberOfTags(p1, p2):
    tags = p1.tags
    for i in range(len(p2.tags)):
        if p2.tags[i] not in tags:
            tags.append(p2.tags[i])
    return len(tags)


def main(filename):

    photos = Photo.takeInput(filename)
    a = Slide(photos[0])    
    b = Slide([photos[2],photos[3]])


if __name__ == "__main__":
    
    main("deneme")