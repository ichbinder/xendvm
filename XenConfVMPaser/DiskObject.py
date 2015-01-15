__author__ = 'jakob'


class DiskObjekt(object):

    __type = ""
    __pathToDisk = ""
    __name = ""
    __readwrite = ""
    __logger = None

    def __init__(self, type, pathToDisk, name, readwrite):
        try:
            if type != "":
                self.__type = type
            else:
                raise
        except:
            #self.__logger.error('Type Options in Configuration file: ' + type + ' could not be loaded.')
            print "Error: type Options in Configuration file: ", type," could not be loaded."
            #raise
        try:
            if pathToDisk != "":
                self.__pathToDisk = pathToDisk
            else:
                raise
        except:
            #self.__logger.error('Path Options in Configuration file: ' + pathToDisk + 'could not be loaded.')
            print "Error: path Options in Configuration file: ", pathToDisk," could not be loaded."
            #raise
        try:
            if name != "":
                self.__name = name
            else:
                raise
        except:
            #self.__logger.error('Name Options in Configuration file: ' + name + ' could not be loaded.')
            print "Error: name Options in Configuration file: ", name," could not be loaded."
            #raise
        try:
            if readwrite != "":
                self.__readwrite = readwrite
            else:
                raise
        except:
            #self.__logger.error('Readwrite Options in Configuration file: ' + readwrite +'could not be loaded.')
            print "Error: readwrite Options in Configuration file: ", readwrite," could not be loaded."
            #raise

    def getType(self):
        return self.__type

    def getPath(self):
        return self.__pathToDisk

    def getName(self):
        return self.__name

    def getReadWrite(self):
        return self.__readwrite
    
    def setPath(self, pathToDisk):
        try:
            if pathToDisk != "":
                self.__pathToDisk = pathToDisk
            else:
                raise
        except:
            #self.__logger.error('Path Options in Configuration file: ' + pathToDisk + 'could not be loaded.')
            print "Error: path Options in Configuration file: ", pathToDisk," could not be loaded."
            #raise