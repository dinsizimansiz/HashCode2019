from Photo import Photo
from Slide import Slide


def main(filename):

    photos = Photo.takeInput(filename)
    print(Slide(photos).getTags())

if __name__ == "__main__":
    
    main("deneme")