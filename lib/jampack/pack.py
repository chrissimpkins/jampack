#!/usr/bin/env python
# encoding: utf-8

import os
import shutil
import tarfile
import zipfile
from Naked.toolshed.system import stdout, stderr

#------------------------------------------------------------------------------
# jampack
# Copyright 2015 Christopher Simpkins
# MIT license
#------------------------------------------------------------------------------


# Application start
def main():
    import sys
    from Naked.commandline import Command
    from Naked.toolshed.state import StateObject

    #------------------------------------------------------------------------------------------
    # [ Instantiate command line object ]
    #   used for all subsequent conditional logic in the CLI application
    #------------------------------------------------------------------------------------------
    c = Command(sys.argv[0], sys.argv[1:])
    #------------------------------------------------------------------------------
    # [ Instantiate state object ]
    #------------------------------------------------------------------------------
    state = StateObject()
    #------------------------------------------------------------------------------------------
    # [ NAKED FRAMEWORK COMMANDS ]
    # Naked framework provides default help, usage, and version commands for all applications
    #   --> settings for user messages are assigned in the lib/jampack/settings.py file
    #------------------------------------------------------------------------------------------
    if c.help():      # User requested jampack help information
        from jampack.settings import help as jampack_help
        print(jampack_help)
        sys.exit(0)
    elif c.usage():   # User requested jampack usage information
        from jampack.settings import usage as jampack_usage
        print(jampack_usage)
        sys.exit(0)
    elif c.version(): # User requested jampack version information
        from jampack.settings import app_name, major_version, minor_version, patch_version
        version_display_string = app_name + ' ' + major_version + '.' + minor_version + '.' + patch_version
        print(version_display_string)
        sys.exit(0)
    #------------------------------------------------------------------------------------------
    # [ PRIMARY COMMAND LOGIC ]
    #   Enter your command line parsing logic below
    #------------------------------------------------------------------------------------------

    if c.argc == 0:
        # pack the current working directory
        directory_name = os.path.basename(os.getcwd())
        package(directory_name, ".")
        stdout("[✓] jampack")
        sys.exit(0)
    elif c.argc > 0:
        # pack the explicitly set directory
        pass

    #------------------------------------------------------------------------------------------
    # [ DEFAULT MESSAGE FOR MATCH FAILURE ]
    #  Message to provide to the user when all above conditional logic fails to meet a true condition
    #------------------------------------------------------------------------------------------
    else:
        print("Could not complete the command that you entered.  Please try again.")
        sys.exit(1) #exit


def exclude_files(tarinfo):
    the_basename = os.path.basename(tarinfo.name)
    if the_basename == ".DS_Store":
        return None
    else:
        return tarinfo


def package(archive_name, root_directory):
    try:
        if root_directory is not ".":
            current_dir = os.getcwd()
            os.chdir(root_directory)  # navigate to the root directory to add the files to the archive
        archive_gz_name = archive_name + ".tar.gz"
        tar = tarfile.open(archive_gz_name, mode="w:gz", compresslevel=9)    # file writes to current working directory
        tar.add(".", filter=exclude_files)     # make tar.gz archive
        tar.close()
        if root_directory is not ".":
            os.chdir(current_dir)  # navigate back to user's current working directory

    except Exception as e:
        os.chdir(current_dir)  # if exception was raised, make sure that user is back in their current working directory before raising system exit
        tar.close()
        stderr("[!] jampack: Unable to pack the directory '" + root_dir + "'. Error: " + str(e))

if __name__ == '__main__':
    main()
