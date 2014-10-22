#!/usr/bin/env python
# encoding: utf-8
'''
Created on 10.10.2014

@author: jakob
'''

import sys
import os
from optparse import OptionParser 

class Cli(object):
    
    __version__ = 0.1
    __updated__ = '2014-10-10'
    
    __parser = None
    __opts = None

    def __init__(self):
        program_name = os.path.basename(sys.argv[0])
        program_version = "v%s" % (self.__version__)
        program_build_date = "%s" % (self.__updated__)

        program_version_string = '%s %s (%s)' % (program_name, program_version, program_build_date)
        program_longdesc = "Create XEN VM" 
        program_license = "Copyright 2014 Jakob Warnow Licensed under the GPL2"
        
        self.__parser = OptionParser(version=program_version_string, epilog=program_longdesc, description=program_license)
        
        self.__parser.add_option("--hostname", dest="hostname", help="Specify the image name to delete.", action='store')
        self.__parser.add_option("--vg", dest="vg", help="Specify the LVM volume group which contains the image(s).", action='store')  
        
    def paser(self):
        (opts, args) = self.__parser.parse_args()
        self.__opts = opts
        mandatories = ['hostname']
        
        for m in mandatories:
            if not opts.__dict__[m]:
                print "mandatory option --%s is missing\n" % (m)
                self.__parser.print_help()
                exit(-1)
                
    def get_hostname(self):
        return self.__opts.hostname
    
    def get_vg(self):
        return self.__opts.vg