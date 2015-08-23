#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------
# Application Name
# ------------------------------------------------------------------------------
app_name = 'jampack'

# ------------------------------------------------------------------------------
# Version Number
# ------------------------------------------------------------------------------
major_version = "0"
minor_version = "9"
patch_version = "3"

# ------------------------------------------------------------------------------
# Debug Flag (switch to False for production release code)
# ------------------------------------------------------------------------------
debug = False

# ------------------------------------------------------------------------------
# Usage String
# ------------------------------------------------------------------------------
usage = """
jam [command] [directory path]
unjam [archive path]

Use 'jam help' or 'unjam help' for additional information
"""

# ------------------------------------------------------------------------------
# Help String
# ------------------------------------------------------------------------------
help = """
-------------------------------------------------
 JamPack
 Simple file archives for everyone
 Copyright 2015 Christopher Simpkins
 MIT license
 Source: http://github.com/chrissimpkins/jampack
-------------------------------------------------

 Archive and Compress Directory
 ==============================

   jam [zip|bz2] [directory path]

 The default archive type is a tar.gz compressed archive if you do not include a secondary command.  The default path is the current working directory if you do not include a directory path.

 Decompress and Unpack Archive
 =============================

   unjam <archive path>

 Include the archive path as the argument for this command.  The archive type is interpreted from the file extension.
"""
