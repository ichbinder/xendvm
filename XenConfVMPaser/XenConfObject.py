__author__ = 'jakob'


class XenConfObjekt(object):

    __vif = None
    __name = ""
    __kernel = ""
    __bootloader = ""
    __vcpus = ""
    __memory = ""
    __root = ""
    __disk = None
    __xenConfigPath = ""
    __logger = None

    def __init__(self, vif, name, kernel, bootloader, vcpus, memory, root, disk, xenConfigPath):
        self.__vif = vif
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
            if kernel != "":
                self.__kernel = kernel
            else:
                raise
        except:
            print "Error: kernel Options in Configuration file: ", kernel," could not be loaded."
            exit(-1)
            #raise
        try:
            if bootloader != "":
                self.__bootloader = bootloader
            else:
                raise
        except:
            print "Error: bootloader Options in Configuration file: ", bootloader," could not be loaded."
            exit(-1)
            #raise
        try:
            if vcpus != "":
                self.__vcpus = vcpus
            else:
                raise
        except:
            print "Error: vcpus Options in Configuration file: ", vcpus," could not be loaded."
            exit(-1)
            #raise
        try:
            if memory != "":
                self.__memory = memory
            else:
                raise
        except:
            print "Error: memory Options in Configuration file: ", memory," could not be loaded."
            exit(-1)
            #raise
        try:
            if root != "":
                self.__root = root
            else:
                raise
        except:
            print "Error: root Options in Configuration file: ", root," could not be loaded."
            exit(-1)
            #raise
        self.__disk = disk
        self.__xenConfigPath = xenConfigPath

    def getVif(self):
        return self.__vif

    def getName(self):
        return self.__name

    def getKernel(self):
        return self.__kernel

    def getBootloader(self):
        return self.__bootloader

    def getVcpus(self):
        return self.__vcpus

    def getMemory(self):
        return self.__memory

    def getDisk(self):
        return self.__disk
    
    def getRoot(self):
        return self.__root
    
    def getXenConfigPath(self):
        return self.__xenConfigPath