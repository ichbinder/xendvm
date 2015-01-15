'''
Created on 12.11.2014

@author: jakob
'''

class CreateXenConfig(object):

    __xenConfigObjekt = ""
    __savePathForXenConf = ""

    def __init__(self, xenConfigObjekt, savePathForXenConf):
        if xenConfigObjekt != None:
            self.__xenConfigObjekt = xenConfigObjekt
        else:
            print "XenConfObjekt is None, can not save."
            exit(-1)
        self.__savePathForXenConf = savePathForXenConf
        
    def create(self):
        xenConfigString = '#\n# Configuration file for the Xen instance testvm01, created\n'
        xenConfigString += '# by xenbackup-Tool \n'
        xenConfigString += '#\n# Kernel + memory size\n#\n'
        xenConfigString += 'bootloader  = \'' + self.__xenConfigObjekt.getBootloader() + '\'\n\n'
        xenConfigString += 'vcpus       = \'' + self.__xenConfigObjekt.getVcpus() + '\'\n'
        xenConfigString += 'memory      = \'' + self.__xenConfigObjekt.getMemory() + '\'\n\n'
        xenConfigString += '#\n#  Disk device(s).\n#\n'
        xenConfigString += 'root        = \'' + self.__xenConfigObjekt.getRoot() + '\'\n'
        xenConfigString += 'disk        = [\n'
        
        for xenDisk in self.__xenConfigObjekt.getDisk():
            xenConfigString += '                    \'%s:%s,%s,%s\',\n' % (xenDisk.getType(),
                                                                           xenDisk.getPath(),
                                                                           xenDisk.getName(),
                                                                           xenDisk.getReadWrite())
        xenConfigString += '              ]\n\n'
        xenConfigString += '#\n#  Hostname\n#\n'
        xenConfigString += 'name        = \'' + self.__xenConfigObjekt.getName() + '\'\n\n'
        xenConfigString += '#\n#  Networking\n#\n'
        if self.__xenConfigObjekt.getDHCP() != None:
            xenConfigString += 'dhcp        = \'' + self.__xenConfigObjekt.getDHCP() + '\'\n'
        xenConfigString += 'vif         = [ \''
        for vifObjekt in self.__xenConfigObjekt.getVif():
            if vifObjekt.getVifname() != None:
                xenConfigString += 'vifname=' + vifObjekt.getVifname() + ','
            if vifObjekt.getIp() != None:
                xenConfigString += 'ip=' + vifObjekt.getIp() + ','
            if vifObjekt.getMac() != None:
                xenConfigString += 'mac=' + vifObjekt.getMac() + ','
            if vifObjekt.getBridge() != None:
                xenConfigString += 'bridge=' + vifObjekt.getBridge()
            xenConfigString = xenConfigString.rstrip(',')
            xenConfigString += '\','
        xenConfigString = xenConfigString.rstrip(',')
        xenConfigString += ' ]\n\n'
        xenConfigString += '#\n#  Behaviour\n#\n'
        if self.__xenConfigObjekt.getOnPoweroff() != None:
            xenConfigString += 'on_poweroff = \'' + self.__xenConfigObjekt.getOnPoweroff() + '\'\n'
        if self.__xenConfigObjekt.getOnReboot() != None:
            xenConfigString += 'on_reboot   = \'' + self.__xenConfigObjekt.getOnReboot() + '\'\n'
        if self.__xenConfigObjekt.getOnCrash() != None:
            xenConfigString += 'on_crash    = \'' + self.__xenConfigObjekt.getOnCrash() + '\'\n'
        
        wIpFree = open(self.__savePathForXenConf, 'w')
        wIpFree.writelines(xenConfigString)
        wIpFree.close()