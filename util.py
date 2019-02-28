#!/usr/bin/env python3

from sys import stdout


class Photo:

    def __init__(self, props):

        self.horizonality = props["horizonality"]
        self.id = props["id"]
        self.tags = props["tags"]

    @staticmethod
    def takeInput(filename):

        images = []
        content = None
        totalPhotos = None
        with open(filename) as fp:
            content = fp.readlines()

        contentLength = len(content)

        for index in range(contentLength):
            if index == 0:
                totalPhotos = int(content[index])
                index += 1
            else:
                if index >= contentLength:
                    break
                else:
                    curPhoto = {}
                    words = content[index].split()
                    curPhoto["horizonality"] = True if words[0] == "H" else False
                    curPhoto["tags"] = []
                    curPhoto["id"] = index - 1
                    numberOfTags = int(words[1])
                    for i in range(numberOfTags):
                        curPhoto["tags"].append(words[i + 2])

                    images.append(Photo(curPhoto))

        return images


class Slide:

    def __init__(self, photos):

        if type(photos) == list:
            self.photos = photos
        else:
            self.photos = [photos]

    def getTags(self):

        unionOfSets = set()
        for i in self.photos:
            unionOfSets |= set(i.tags)

        return unionOfSets

    def isVertical(self):
        return len(self.photos) == 2

    def getInterest(self, other):

        thisTags = self.getTags()
        otherTags = other.getTags()

        intersection = thisTags.intersection(otherTags)
        thisTags = thisTags - intersection
        otherTags = otherTags - intersection

        return min(len(intersection), len(thisTags), len(otherTags))

    @staticmethod
    def printSlides(slides, filename=stdout):

        print(len(slides), file=filename)
        for curSlide in slides:
            for photo in curSlide.photos:
                print(photo.id, file=filename, end=" ")
            print(file=filename)
