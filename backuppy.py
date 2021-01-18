import os
import shutil
import time
import datetime
from zipfile import ZipFile
from shutil import make_archive
from optparse import OptionParser, OptionGroup

parser = OptionParser(description="Description : Read the help options before using. This programme is for backup.")
parser.add_option("-s", "--src", dest="src",
                  help="Provide source directory name.", metavar="Directory")

parser.add_option("-d", "--dest", dest="dest",
                  help="Provide destination directory name.", metavar="Directory")

(opts, args) = parser.parse_args()

# Starting Main programme

def data_backup(src,dest):
    """
    For Backup
    """
    now = datetime.datetime.now()
#    print(now.strftime("%d%m%Y"))

    timestamp = str(now.strftime("%d%m%Y_%H%M%S"))
#    print(timestamp)

    # Print the current working directory
    print("Script directory: {0}".format(os.getcwd()))
    
    # path   
    src_path = "C:/tally erp/"
    dest_path = "C:/tally_backup"
  
    os.chdir(src_path)
    # Print the current working directory
    print("Source Directory Name: ", src)
    print("Source Backup Directory: {0}".format(os.getcwd()))
        
    #shutil.copytree(src,dest+'_'+timestamp)
    shutil.copytree(src,dest)
    
    os.chdir(dest_path)

    # Print source and destination name
    print("Destination Directory Name: ", dest)
    print("Destination Backup Directory: {0}".format(os.getcwd()))

    shutil.make_archive(dest+'_'+timestamp,'zip', dest)

    time.sleep(10)

    shutil.rmtree(dest)

if __name__ == "__main__":
    if opts.src == None or opts.dest == None:
        parser.print_help()
        exit(-1)
    data_backup(opts.src,opts.dest)
