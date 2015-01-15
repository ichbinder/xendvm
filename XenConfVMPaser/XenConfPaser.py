__author__ = 'jakob'

import StringIO
import ConfigParser
import re, os
import DiskObject
import VifObject
import XenConfObject
from Logging import FileLogging

class XenConfPaser(object):

    __pathToVMConfig = ""
    __xenConf = None
    __config = None
    __logger = None

    def __init__(self, pathToVMConfig):
        self.__logger = FileLogging.Logger()
        if not os.path.exists(pathToVMConfig):
            self.__logger.error('Configuration file could not be loaded.' + pathToVMConfig)
            print "Xen VM Configuration file could not be loaded: " + pathToVMConfig
            exit(-1)
        else:
            self.__pathToVMConfig = pathToVMConfig
        self.__config = ConfigParser.SafeConfigParser()

    def paser(self):
        try:
            confStr = '[root]\n' + open(self.__pathToVMConfig, 'r').read()
            #data = StringIO.StringIO('\n'.join(line.strip() for line in confStr))
            data = StringIO.StringIO(confStr)
            self.__config.readfp(data)
        except:
            self.__logger.error('Xen VM Configuration file could not be loaded.' + self.__pathToVMConfig)
            exit(-1)
            #print "Configuration file could not be loaded ", e
            #raise

        dictOptions = self.__ConfigSectionMap("root")
        
        listDiskObjekts = []
        listDisks = re.findall(r'[A-Za-z]+:.*,[w|r]', dictOptions["disk"])
        for disk in listDisks:
            try:
                diskType = re.findall(r'\A[A-Za-z]+:', disk)[0].rsplit(":")[0]
                diskPath = re.findall(r':.*,',disk)[0].lstrip(":").rstrip(",").split(",")[0]
                diskName = re.findall(r',.*,', disk)[0].strip(",")
                diskReadWrite = re.findall(r",[r|w]",disk)[0].strip(",")
                listDiskObjekts.append(DiskObject.DiskObjekt(diskType,
                                                             diskPath,
                                                             diskName,
                                                             diskReadWrite))
            except:
                self.__logger.error('Disk Options in Configuration: ' + self.__pathToVMConfig + ' file could not be loaded.')
                #print "Error: disk Options in Configuration: ", self.__path,"file could not be loaded."
                #raise

        listVifObjekts = []
        listVif = re.findall(r"'.*[ip|mac|bridge|vifname].*'", dictOptions["vif"])
        for vif in listVif:
            try:
                vifName = re.findall(r"vifname ?= ?.*[,|']", vif)[0].rsplit("=")[1].strip(' ').rstrip(",").rstrip("'")
            except:
                self.__logger.info('vif Name is not seted.')
                #print "Info: vif Name is not seted."
                vifName = None
            try:
                vifIp = re.findall(r"ip ?= ?[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}", vif)[0].rsplit("=")[1].strip(' ')
            except:
                self.__logger.info('vif Ip is not seted.')
                #print "Info: vif Ip is not seted."
                vifIp = None
            try:
                vifMac = re.findall(r"mac ?= ?..:..:..:..:..:..", vif)[0].rsplit("=")[1].strip(' ')
            except:
                self.__logger.info('vif Mac is not seted.')
                #print "Info: vif Mac is not seted."
                vifMac = None
            try:
                vifBridge = re.findall(r"bridge ?= ?.*[,|']", vif)[0].rsplit("=")[1].strip(' ')
            except:
                self.__logger.info('vif Bridge is not seted.')
                #print "Info: vif Bridge is not seted."
                vifBridge = None
            listVifObjekts.append(VifObject.VifObjekt(vifBridge, vifIp, vifMac, vifName))
        self.__xenConf = XenConfObject.XenConfObjekt(
            listVifObjekts,
            dictOptions["name"] if "name" in dictOptions else self.__raiser("Name is not set in Configuration Xen file"),
            dictOptions["kernel"] if "kernel" in dictOptions else None,
            dictOptions["bootloader"] if "bootloader" in dictOptions else self.__raiser("bootloader is not set in Configuration Xen file"),
            dictOptions["vcpus"] if "vcpus" in dictOptions else self.__raiser("vcpus is not set in Configuration Xen file"),
            dictOptions["memory"] if "memory" in dictOptions else self.__raiser("memory is not set in Configuration Xen file"),
            dictOptions["root"] if "root" in dictOptions else self.__raiser("root is not set in Configuration Xen file"),
            dictOptions["dhcp"] if "dhcp" in dictOptions else None,
            dictOptions["on_poweroff"] if "on_poweroff" in dictOptions else None,
            dictOptions["on_reboot"] if "on_reboot" in dictOptions else None,
            dictOptions["on_crash"] if "on_crash" in dictOptions else None,
            listDiskObjekts,
            self.__pathToVMConfig)
        return self.__xenConf
            
    def __raiser(self, ex):
        FileLogging.Logger.error(ex)
        #raise ValueError(ex)

    def __ConfigSectionMap(self, section):
        dictOptions = {}
        options = self.__config.options(section)
        for option in options:
            try:
                dictOptions[option] = self.__config.get(section, option).strip('"').strip("'")
                if dictOptions[option] == "":
                    raise
            except:
                self.__logger.error("exception on %s! maybe no value?" % option)
                #print("exception on %s! maybe no value?" % option)
                #raise
        return dictOptions

    def getXenConfObjekt(self):
        return self.__xenConf