#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------
# jampack
# Copyright 2015 Christopher Simpkins
# MIT license
# ------------------------------------------------------------------------------

import zipfile
import tarfile
from Naked.toolshed.system import stdout, stderr


# Application start
def main():
    import sys
    from Naked.commandline import Command

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
                    zipper = zipfile.ZipFile(archive_name, mode="r")
                    zipper.extractall()
                elif lowercase_archive_name.endswith('.tar.gz') or lowercase_archive_name.endswith('.tgz') or lowercase_archive_name.endswith('.tar.gzip'):
                    tarball = tarfile.open(archive_name, mode="r:gz")
                    tarball.extractall()
                elif lowercase_archive_name.endswith('.tar.bz2') or lowercase_archive_name.endswith('.tar.bzip2'):
                    bzball = tarfile.open(archive_name, mode="r:bz2")
                    bzball.extractall()
                else:
                    stderr("[\033[91m!\033[0m] jampack: Unable to identify the archive type for '" + archive_name + "'. This archive was not unpacked. Please check the file extension and try again.")
        except Exception as e:
            stderr(
                "[\033[91m!\033[0m] jampack: Unable to unpack the archive '" + archive_name + "'. Error: " + str(e))

    # ------------------------------------------------------------------------------------------
    # [ DEFAULT MESSAGE FOR MATCH FAILURE ]
    #  Message to provide to the user when all above conditional logic fails to meet a true condition
    # ------------------------------------------------------------------------------------------
    else:
        print("Could not complete the command that you entered.  Please try again.")
        sys.exit(1)  # exit

if __name__ == '__main__':
    main()
