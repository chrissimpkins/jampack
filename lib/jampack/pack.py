#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------
# jampack
# Copyright 2015 Christopher Simpkins
# MIT license
# ------------------------------------------------------------------------------

import os
import shutil
import tarfile
import zipfile
from Naked.toolshed.system import stdout, stderr

# start colorama for colored CLI std output
from colorama import init
init()


# Application start
def main():
    import sys
    from Naked.commandline import Command

    # ------------------------------------------------------------------------------------------
    # [ Instantiate Naked framework command line object ]
    #   used for all subsequent conditional logic in the CLI application
    # ------------------------------------------------------------------------------------------
    c = Command(sys.argv[0], sys.argv[1:])

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
    # ------------------------------------------------------------------------------------------
    # [ PRIMARY COMMAND LOGIC ]
    # ------------------------------------------------------------------------------------------
    if c.argc == 0:
        # tar.gz pack the current working directory
        directory_name = os.path.basename(os.getcwd())
        directory_size = get_directory_size(".")
        package_targz(directory_name, ".")
        archive_name = directory_name + ".tar.gz"
        percent_filesize = (100 * (get_file_size(archive_name) / float(directory_size)))
        display_percent = str(int(percent_filesize))
        stdout("[\033[32m✓\033[0m] " + archive_name + " created " + "[~" + display_percent + "% original]")
        sys.exit(0)
    elif c.argc > 0:
        if c.arg0 == "zip":
            if c.argc == 1:
                # zip pack the current working directory
                directory_name = os.path.basename(os.getcwd())
                directory_size = get_directory_size(".")
                package_zip(directory_name, ".")
                archive_name = directory_name + ".zip"
                percent_filesize = (100 * (get_file_size(archive_name) / float(directory_size)))
                display_percent = str(int(percent_filesize))
                stdout("[\033[32m✓\033[0m] " + archive_name + " created " + "[~" + display_percent + "% original]")
                sys.exit(0)
            else:
                directory_list = c.argv[1:]
                for a_directory in directory_list:
                    if os.path.isdir(a_directory):
                        directory_name = os.path.basename(a_directory)
                        directory_size = get_directory_size(a_directory)
                        package_zip(directory_name, a_directory)
                        archive_name = directory_name + ".zip"
                        percent_filesize = (100 * (get_file_size(archive_name) / float(directory_size)))
                        display_percent = str(int(percent_filesize))
                        stdout(
                            "[\033[32m✓\033[0m] " + archive_name + " created " + "[~" + display_percent + "% original]")
                    else:
                        stderr("[\033[31mX\033[0m] " + a_directory + " is not a directory path")
                sys.exit(0)
        elif c.arg0 == "bz2":
            if c.argc == 1:
                # bz2 pack the current working directory
                directory_name = os.path.basename(os.getcwd())
                directory_size = get_directory_size(".")
                package_bzip2(directory_name, ".")
                archive_name = directory_name + ".tar.bz2"
                percent_filesize = (100 * (get_file_size(archive_name) / float(directory_size)))
                display_percent = str(int(percent_filesize))
                stdout("[\033[32m✓\033[0m] " + archive_name + " created " + "[~" + display_percent + "% original]")
                sys.exit(0)
            else:
                # bz2 pack one or more explicitly set directory
                directory_list = c.argv[1:]
                for a_directory in directory_list:
                    if os.path.isdir(a_directory):
                        directory_name = os.path.basename(a_directory)
                        directory_size = get_directory_size(a_directory)
                        package_bzip2(directory_name, a_directory)
                        archive_name = directory_name + ".tar.bz2"
                        percent_filesize = (100 * (get_file_size(archive_name) / float(directory_size)))
                        display_percent = str(int(percent_filesize))
                        stdout(
                            "[\033[32m✓\033[0m] " + archive_name + " created " + "[~" + display_percent + "% original]")
                    else:
                        stderr("[\033[31mX\033[0m] " + a_directory + " is not a directory path")

                sys.exit(0)
        else:
            # tar.gz one or more explicitly defined directories
            for a_directory in c.argv:
                if os.path.isdir(a_directory):
                    directory_name = os.path.basename(a_directory)
                    directory_size = get_directory_size(a_directory)
                    package_targz(directory_name, a_directory)
                    archive_name = directory_name + ".tar.gz"
                    percent_filesize = (100 * (get_file_size(archive_name) / float(directory_size)))
                    display_percent = str(int(percent_filesize))
                    stdout("[\033[32m✓\033[0m] " + archive_name + " created " + "[~" + display_percent + "% original]")
                else:
                    stderr("[\033[31mX\033[0m] " + a_directory + " is not a directory path")

            sys.exit(0)

    # ------------------------------------------------------------------------------------------
    # [ DEFAULT MESSAGE FOR MATCH FAILURE ]
    #  Message to provide to the user when all above conditional logic fails to meet a true condition
    # ------------------------------------------------------------------------------------------
    else:
        print("[\033[31mX\033[0m] Could not complete the command that you entered.  Please try again.")
        sys.exit(1)  # exit


def exclude_files(tarinfo):
    the_basename = os.path.basename(tarinfo.name)
    if the_basename == ".DS_Store":
        return None
    else:
        return tarinfo


def get_directory_size(the_directory):
    total_size = os.path.getsize(the_directory)
    for item in os.listdir(the_directory):
        itempath = os.path.join(the_directory, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += get_directory_size(itempath)
    return total_size


def get_file_size(the_file):
    return os.path.getsize(the_file)


def package_targz(archive_name, root_directory):
    try:
        if root_directory is not ".":
            current_dir = os.getcwd()
            os.chdir(root_directory)  # navigate to the root directory to add the files to the archive
        archive_gz_name = archive_name + ".tar.gz"
        tar = tarfile.open(archive_gz_name, mode="w:gz", compresslevel=9)    # file writes to current working directory
        tar.add(".", filter=exclude_files)     # make tar.gz archive
        tar.close()
        if root_directory is not ".":
            shutil.move(archive_gz_name, os.path.join(current_dir, archive_gz_name))  # move file to working directory
            os.chdir(current_dir)  # navigate back to user's current working directory
    except Exception as e:
        os.chdir(current_dir)
        tar.close()
        stderr("[\033[31m!\033[0m] jampack: Unable to pack the directory '" + root_directory + "'. Error: " + str(e))


def package_bzip2(archive_name, root_directory):
    try:
        if root_directory is not ".":
            current_dir = os.getcwd()
            os.chdir(root_directory)  # navigate to the root directory to add the files to the archive
        archive_gz_name = archive_name + ".tar.bz2"
        tar = tarfile.open(archive_gz_name, mode="w:bz2", compresslevel=9)  # file writes to current working directory
        tar.add(".", filter=exclude_files)  # make tar.gz archive
        tar.close()
        if root_directory is not ".":
            shutil.move(archive_gz_name, os.path.join(current_dir, archive_gz_name))  # move file to working directory
            os.chdir(current_dir)  # navigate back to user's current working directory
    except Exception as e:
        os.chdir(current_dir)
        tar.close()
        stderr("[\033[31m!\033[0m] jampack: Unable to pack the directory '" + root_directory + "'. Error: " + str(e))


def package_zip(archive_name, root_directory):
    try:
        # attempt to import zlib for compression, fall back to default if not installed
        try:
            import zlib
            compression = zipfile.ZIP_DEFLATED
        except ImportError:
            compression = zipfile.ZIP_STORED

        archive_zip_name = archive_name + '.zip'
        archive_file_list = []
        current_dir = os.getcwd()

        # change to the target directory if explicitly requested
        if root_directory is not ".":
            os.chdir(root_directory)

        for root, dirs, files in os.walk(os.getcwd()):
            for the_file in files:
                archive_file_list.append((os.path.relpath(os.path.join(root, the_file))))
        zipper = zipfile.ZipFile(archive_zip_name, 'w')
        for zip_file in archive_file_list:
            # do not include OS X .DS_Store files in archives
            if os.path.basename(zip_file) == ".DS_Store":
                pass
            else:
                zipper.write(zip_file, compress_type=compression)
        zipper.close()

        # change to the original working directory if the directory was changed
        if root_directory is not ".":
            shutil.move(archive_zip_name, os.path.join(current_dir, archive_zip_name))
            os.chdir(current_dir)
    except Exception as e:
        os.chdir(current_dir)
        zipper.close()
        stderr("[\033[31m!\033[0m] jampack: Unable to pack the directory '" + root_directory + "'. Error: " + str(e))

if __name__ == '__main__':
    main()
