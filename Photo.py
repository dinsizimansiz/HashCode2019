
class Photo:

    def __init__(self,props):

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
                    curPhoto["id"] = index-1
                    numberOfTags = int(words[1])
                    for i in range(numberOfTags):
                        curPhoto["tags"].append(words[i+2])

                    images.append(Photo(curPhoto))

        return images