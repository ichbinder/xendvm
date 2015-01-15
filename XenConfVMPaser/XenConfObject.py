__author__ = 'jakob'

from Logging import FileLogging

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
    __dhcp = ""
    __on_poweroff = ""
    __on_reboot = ""
    __on_crash = ""
    __logger = None

    def __init__(self, vif, name, kernel, bootloader, vcpus, memory, root, dhcp, on_poweroff, on_reboot, on_crash, disk, xenConfigPath):
        self.__logger = FileLogging.Logger()
        self.__vif = vif
        try:
            if name != "":
                self.__name = name
            else:
                raise
        except:
            self.__logger.error('Name Options in Configuration file: ' + name + ' could not be loaded.')
            #print "Error: name Options in Configuration file: ", name," could not be loaded."
            #raise
        try:
            if kernel != "":
                self.__kernel = kernel
            else:
                raise
        except:
            self.__logger.error('Kernel Options in Configuration file: ' + kernel + ' could not be loaded.')
            #print "Error: kernel Options in Configuration file: ", kernel," could not be loaded."
            #raise
        try:
            if bootloader != "":
                self.__bootloader = bootloader
            else:
                raise
        except:
            self.__logger.error('Bootloader Options in Configuration file: ' + bootloader + ' could not be loaded.')
            #print "Error: bootloader Options in Configuration file: ", bootloader," could not be loaded."
            #raise
        try:
            if vcpus != "":
                self.__vcpus = vcpus
            else:
                raise
        except:
            self.__logger.error('Vcpus Options in Configuration file: ' + vcpus + ' could not be loaded.')
            #print "Error: vcpus Options in Configuration file: ", vcpus," could not be loaded."
            #raise
        try:
            if memory != "":
                self.__memory = memory
            else:
                raise
        except:
            self.__logger.error('Memory Options in Configuration file: ' + memory + ' could not be loaded.')
            #print "Error: memory Options in Configuration file: ", memory," could not be loaded."
            #raise
        try:
            if dhcp != None:
                self.__dhcp = dhcp
            else:
                self.__dhcp = None
        except:
            self.__logger.error('Root Options in Configuration file: ' + dhcp + ' could not be loaded.')
            #print "Error: root Options in Configuration file: ", dhcp," could not be loaded."
            #raise
        
        try:
            if root != "":
                self.__root = root
            else:
                raise
        except:
            self.__logger.error('Root Options in Configuration file: ' + root + ' could not be loaded.')
            #print "Error: root Options in Configuration file: ", root," could not be loaded."
            #raise
        try:
            if on_poweroff != None:
                self.__on_poweroff = on_poweroff
            else:
                raise
        except:
            self.__logger.error('Root Options in Configuration file: ' + on_poweroff + ' could not be loaded.')
            #print "Error: root Options in Configuration file: ", on_poweroff," could not be loaded."
            #raise
        try:
            if on_reboot != None:
                self.__on_reboot = on_reboot
            else:
                raise
        except:
            self.__logger.error('Root Options in Configuration file: ' + on_reboot + ' could not be loaded.')
            #print "Error: root Options in Configuration file: ", on_reboot," could not be loaded."
            #raise
        try:
            if on_crash != None:
                self.__on_crash = on_crash
            else:
                raise
        except:
            self.__logger.error('Root Options in Configuration file: ' + on_crash + ' could not be loaded.')
            #print "Error: root Options in Configuration file: ", on_crash," could not be loaded."
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

    def getDHCP(self):
        return self.__dhcp
    
    def getOnPoweroff(self):
        return self.__on_poweroff

    def getOnReboot(self):
        return self.__on_reboot
    
    def getOnCrash(self):
        return self.__on_crash
    
    def getXenConfigPath(self):
        return self.__xenConfigPath