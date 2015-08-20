#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------
# jampack
# Copyright 2015 Christopher Simpkins
# MIT license
# ------------------------------------------------------------------------------

# Application start
def main():
    import sys
    from Naked.commandline import Command
    from Naked.toolshed.state import StateObject

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
    elif c.version(): # User requested jampack version information
        from jampack.settings import app_name, major_version, minor_version, patch_version
        version_display_string = app_name + ' ' + major_version + '.' + minor_version + '.' + patch_version
        print(version_display_string)
        sys.exit(0)
    else:
        # just display usage information with this executable.  Users need to use jam or unjam
        from jampack.settings import usage as jampack_usage
        print(jampack_usage)
        sys.exit(0)

if __name__ == '__main__':
    main()
