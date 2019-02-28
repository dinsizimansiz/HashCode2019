from sys import stdout


class Slide:

    def __init__(self,photos):

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

    def getInterest(self,other):
        
        thisTags = self.getTags()
        otherTags = other.getTags()

        intersection = thisTags.intersection(otherTags)
        thisTags = thisTags - intersection
        otherTags = otherTags - intersection
        
        return min(len(intersection),len(thisTags),len(otherTags))

    
    @staticmethod
    def printSlides(slides,filename=stdout):


        print(len(slides),file=filename)
        for curSlide in slides:
            for photo in curSlide.photos:
                print(photo.id,file=filename,end=" ")
            print(file=filename)        
