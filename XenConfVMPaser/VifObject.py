__author__ = 'jakob'



class VifObjekt(object):

    #__backend = ""
    __bridge = ""
    __ip = ""
    __mac = ""
    __vifname = ""

    def __init__(self, bridge, ip, mac, vifname):
        #self.__backend = backend
        self.__bridge = bridge
        self.__ip = ip
        self.__mac = mac
        self.__vifname = vifname

    #def getBackend(self):
    #    return self.__backend

    def getBridge(self):
        return self.__bridge

    def getIp(self):
        return self.__ip

    def getMac(self):
        return self.__mac

    def getVifname(self):
        return self.__vifname