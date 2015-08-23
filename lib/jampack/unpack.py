#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------
# jampack
# Copyright 2015 Christopher Simpkins
# MIT license
# ------------------------------------------------------------------------------

import zipfile
import tarfile
import platform
from Naked.toolshed.system import stdout, stderr

# start colorama for colored CLI std output
from colorama import init
init()


# Application start
def main():
    import sys
    from Naked.commandline import Command

    user_platform = platform.system()

    # ------------------------------------------------------------------------------------------
    # [ Instantiate Naked framework command line object ]
    #   used for all subsequent conditional logic in the CLI application
    # ------------------------------------------------------------------------------------------
    c = Command(sys.argv[0], sys.argv[1:])

    if not c.command_suite_validates():
        from jampack.settings import usage as jampack_usage
        print(jampack_usage)
        sys.exit(1)

    if c.help():      # User requested jampack help information
        from jampack.settings import help as jampack_help
        print(jampack_help)
        sys.exit(0)
    elif c.usage():   # User requested jampack usage information
        from jampack.settings import usage as jampack_usage
        print(jampack_usage)
        sys.exit(0)
    elif c.version():  # User requested jampack version information
        from jampack.settings import app_name, major_version, minor_version, patch_version
        version_display_string = app_name + ' ' + major_version + '.' + minor_version + '.' + patch_version
        print(version_display_string)
        sys.exit(0)

    if c.argc > 0:  # if there is an argument to the executable
        try:
            for archive_name in c.argv:
                lowercase_archive_name = archive_name.lower()
                if lowercase_archive_name.endswith('.zip'):
                    if zipfile.is_zipfile(archive_name):
                        zipper = zipfile.ZipFile(archive_name, mode="r")
                        zipper.extractall()
                        if user_platform == "Windows":
                            stdout("'" + archive_name + "' was unpacked.")
                        else:
                            stdout("[\033[32m✓\033[0m] '" + archive_name + "' was unpacked.")
                    else:
                        if user_platform == "Windows":
                            stderr("'" + archive_name + "' does not appear to be a zip file")
                        else:
                            stderr("[\033[31m!\033[0m] '" + archive_name + "' does not appear to be a zip file")
                elif lowercase_archive_name.endswith('.tar.gz') or lowercase_archive_name.endswith('.tgz') or lowercase_archive_name.endswith('.tar.gzip'):
                    if tarfile.is_tarfile(archive_name):
                        tarball = tarfile.open(archive_name, mode="r:gz")
                        tarball.extractall()
                        if user_platform == "Windows":
                            stdout("'" + archive_name + "' was unpacked.")
                        else:
                            stdout("[\033[32m✓\033[0m] '" + archive_name + "' was unpacked.")
                    else:
                        if user_platform == "Windows":
                            stderr("'" + archive_name + "' does not appear to be a tar archive")
                        else:
                            stderr("[\033[31m!\033[0m] '" + archive_name + "' does not appear to be a tar archive")
                elif lowercase_archive_name.endswith('.tar.bz2') or lowercase_archive_name.endswith('.tar.bzip2'):
                    if tarfile.is_tarfile(archive_name):
                        bzball = tarfile.open(archive_name, mode="r:bz2")
                        bzball.extractall()
                        if user_platform == "Windows":
                            stdout("'" + archive_name + "' was unpacked.")
                        else:
                            stdout("[\033[32m✓\033[0m] '" + archive_name + "' was unpacked.")
                    else:
                        if user_platform == "Windows":
                            stderr("'" + archive_name + "' does not appear to be a tar archive")
                        else:
                            stderr("[\033[31m!\033[0m] '" + archive_name + "' does not appear to be a tar archive")
                else:
                    if user_platform == "Windows":
                        stderr("Unable to identify the archive type for '" + archive_name + "'. This archive was not unpacked. Please check the file extension and try again.")
                    else:
                        stderr("[\033[31m!\033[0m] Unable to identify the archive type for '" + archive_name + "'. This archive was not unpacked. Please check the file extension and try again.")
        except Exception as e:
            if user_platform == "Windows":
                stderr("Unable to unpack the archive '" + archive_name + "'. Error: " + str(e))
            else:
                stderr(
                    "[\033[31m!\033[0m] Unable to unpack the archive '" + archive_name + "'. Error: " + str(e))

    # ------------------------------------------------------------------------------------------
    # [ DEFAULT MESSAGE FOR MATCH FAILURE ]
    #  Message to provide to the user when all above conditional logic fails to meet a true condition
    # ------------------------------------------------------------------------------------------
    else:
        if user_platform == "Windows":
            print("Could not complete the command that you entered.  Please try again.")
        else:
            print("[\033[31mX\033[0m] Could not complete the command that you entered.  Please try again.")
        sys.exit(1)  # exit

if __name__ == '__main__':
    main()
