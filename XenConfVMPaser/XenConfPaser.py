__author__ = 'jakob'

import StringIO
import ConfigParser
import re
import DiskObject
import VifObject
import XenConfObject

class XenConfPaser(object):

    __path = ""
    __xenConf = None
    __config = None

    def __init__(self, path):
        self.__path = path
        self.__config = ConfigParser.SafeConfigParser()

    def paser(self):
        try:
            confStr = '[root]\n' + open(self.__path, 'r').read()
            #data = StringIO.StringIO('\n'.join(line.strip() for line in confStr))
            data = StringIO.StringIO(confStr)
            self.__config.readfp(data)
        except Exception as e:
            print "Configuration file could not be loaded ", e
            exit(-1)
            #raise

        dictOptions = self.__ConfigSectionMap("root")
        
        listDiskObjekts = []
        listDisks = re.findall(r'[A-Za-z]+:.*,w|r', dictOptions["disk"])
        for disk in listDisks:
            try:
                diskType = re.findall(r'\A[A-Za-z]+:', disk)[0].rsplit(":")[0]
                diskPath = re.findall(r':.*,',disk)[0].lstrip(":").rstrip(",").split(",")[0]
                diskName = re.findall(r',.*,', disk)[0].strip(",")
                diskReadWrite = re.findall(r',w|r',disk)[0].rstrip(",")
                listDiskObjekts.append(DiskObject.DiskObjekt(diskType,diskPath,diskName,diskReadWrite))
            except:
                print "Error: disk Options in Configuration: ", self.__path,"file could not be loaded."
                exit(-1)
                #raise

        listVifObjekts = []
        listVif = re.findall(r"'.*[ip|mac|bridge|vifname].*'", dictOptions["vif"])
        for vif in listVif:
            try:
                vifName = re.findall(r"vifname ?= ?.*[,|']", vif)[0].rsplit("=")[1].strip(' ').rstrip(",").rstrip("'")
            except:
                print "Info: vif Name is not seted."
                vifName = None
            try:
                vifIp = re.findall(r"ip ?= ?[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}", vif)[0].rsplit("=")[1].strip(' ')
            except:
                print "Info: vif Ip is not seted."
                vifIp = None
            try:
                vifMac = re.findall(r"mac ?= ?..:..:..:..:..:..", vif)[0].rsplit("=")[1].strip(' ')
            except:
                print "Info: vif Mac is not seted."
                vifMac = None
            try:
                vifBridge = re.findall(r"bridge ?= ?.*[,|']", vif)[0].rsplit("=")[1].strip(' ')
            except:
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
            listDiskObjekts,
            self.__path)
        return self.__xenConf
            
    def __raiser(self, ex):
        print ex
        exit(-1)
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
                print("exception on %s! maybe no value?" % option)
                exit(-1)
                #raise
        return dictOptions

    def getXenConfObjekt(self):
        return self.__xenConf