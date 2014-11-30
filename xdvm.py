#!/usr/bin/env python
# encoding: utf-8

'''
Created on 21.10.2014

@author: jakob
'''

from XenConfVMPaser import XenConfPaser
import Cli, os, re
import subprocess

def clearNewline(clearFile):
    with open(clearFile,'r+') as ipFile:
        tmp = ipFile.readlines()
        ipFile.seek(0)
        ipFile.truncate()
        ipFile.seek(0)
        for l in tmp:
            if not re.match(r'^\s*$', l):
                ipFile.write(l)

if __name__ == '__main__':
    
    cli = Cli.Cli()
    cli.paser()
    
    ipfreefile = "~/ipfree.txt"
    ipdropfile = "~/ipdrop.txt"
    
    if not os.path.isfile(ipfreefile):
        print "ipfree.txt not found!\n"
        exit(-1)
    else:
        clearNewline(ipfreefile)
        
    if not os.path.isfile(ipdropfile):
        print "ipdrop.txt not found!\n"
        exit(-1)
    else:
        clearNewline(ipdropfile)
    
    #vmconf = "/etc/xen/%s.cfg" % (cli.get_hostname())   
    vmconf = "%s.cfg" % (cli.get_hostname())
    #vmconf = "%s.cfg" % (cli.get_hostname())
    if not os.path.isfile(vmconf):
        print "Config " + vmconf + " dosnt not exist!"
        exit(-1)
    
    xcp = XenConfPaser.XenConfPaser(vmconf)
    xcp.paser()
    ip = xcp.getXenConfObjekt().getVif()[0].getIp()
    mac = xcp.getXenConfObjekt().getVif()[0].getMac()
    IpMac = ("%s;%s" % (ip, mac)).lower()
    
    if cli.get_vg() != None:
        cliOptions = "xen-delete-image --lvm %s %s" % (cli.get_vg(), cli.get_hostname())
    else:
        cliOptions = "xen-delete-image --lvm VolGroup %s" % (cli.get_hostname())
 
    p = subprocess.Popen(cliOptions, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    while(True):
        retcode = p.poll() #returns None while subprocess is running
        line = p.stdout.readline()
        print line[:-1]
        if(retcode is not None):
            break

    if os.path.isfile(vmconf):
        rIpFree = open(ipdropfile, 'r')
        lines = rIpFree.readlines()
        rIpFree.close()
        for index, ipMacListelement in enumerate(lines):
            if "\n" in ipMacListelement:
                ipMacListelement = ipMacListelement[:-1]
            if ipMacListelement == IpMac:
                ipMacListelement = "\n" + ipMacListelement
                with open(ipfreefile, "a") as aIpDrop:
                    aIpDrop.write(ipMacListelement)
                del lines[index]
                wIpFree = open(ipdropfile, 'w')
                wIpFree.writelines(lines)
                wIpFree.close()
        clearNewline(ipfreefile)
        clearNewline(ipdropfile)
                

    
