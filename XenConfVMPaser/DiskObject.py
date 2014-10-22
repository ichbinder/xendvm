__author__ = 'jakob'


class DiskObjekt(object):

    __type = ""
    __path = ""
    __name = ""
    __readwrite = ""
    __logger = None

    def __init__(self, type, path, name, readwrite):
        try:
            if type != "":
                self.__type = type
            else:
                raise
        except:
            print "Error: type Options in Configuration file: ", type," could not be loaded."
            exit(-1)
            #raise
        try:
            if path != "":
                self.__path = path
            else:
                raise
        except:
            print "Error: path Options in Configuration file: ", path," could not be loaded."
            exit(-1)
            #raise
        try:
            if name != "":
                self.__name = name
            else:
                raise
        except:
            print "Error: name Options in Configuration file: ", name," could not be loaded."
            exit(-1)
            #raise
        try:
            if readwrite != "":
                self.__readwrite = readwrite
            else:
                raise
        except:
            print "Error: readwrite Options in Configuration file: ", readwrite," could not be loaded."
            exit(-1)
            #raise

    def getType(self):
        return self.__type

    def getPath(self):
        return self.__path

    def getName(self):
        return self.__name

    def getReadWrite(self):
        return self.__readwrite