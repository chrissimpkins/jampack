<img src="https://raw.githubusercontent.com/chrissimpkins/jampack/master/img/jampack-header.png" alt="JamPack - simple file archives for everyone" width="728" />

## JamPack

> Simple file archives for everyone

### About

JamPack includes the executables `jam` and `unjam` that provide a simple approach to pack and unpack tar.gz, tar.bz2, and zip file archives, respectively.  No more alphabet soup.


### Contents

- [Install Guide](https://github.com/chrissimpkins/jampack#install)
- [`jam` Usage](https://github.com/chrissimpkins/jampack#jam-usage)
- [`unjam` Usage](https://github.com/chrissimpkins/jampack#unjam-usage)


### Install

JamPack requires Python v2.6+ or v3.2+ and you can install it with pip:

```shell
$ pip install jampack
```

or download the source repository, unpack it locally, navigate to the root directory, and run the command:

```shell
$ python setup.py install
```

You can safely discard the source repository after you use this command.

### Usage

#### `jam` Usage

```
jam [secondary command] [directory path]
```

##### Default Behavior

`jam` defaults to a tar.gz archive of the current working directory.  To create this simply navigate to the directory and enter:

```shell
$ jam
```

The archive file takes the same name as the working directory name and writes to the working directory.

##### Secondary Commands

You can create tar.bz2 or zip archives by including either the `bz2` or `zip` secondary command as an argument to the `jam` executable:

```shell
$ jam bz2
```

```shell
$ jam zip
```

In the above examples, the working directory is compressed into a tar.bz2 archive (top) and a zip archive (bottom).


##### Explicit Directory Archives

Include one or more directory path arguments to create a new archive file for each directory that you specify.

```shell
$ jam mydirectory
```

The above command creates a tar.gz archive of the subdirectory `mydirectory` and the archive write takes place in the current working directory. The top level of the destination directory is always used as the root directory for your new archive irrespective of the depth from the current working directory.

Add a `bz2` or `zip` secondary command followed by the directory path(s) to create tar.bz2 and zip archives.  For example, 

```shell
$ jam bz2 mydirectory
```

```shell
$ jam zip mydirectory
```

##### Compression of Archives

Maximum compression level (compression level 9) is always used for gzip and bzip2 compression.  zip compression is maximized if your system includes a zlib install, otherwise the system default compression level is used.


##### OS X Only

`.DS_Store` files are excluded from all archive types by default.


### `unjam` Usage

```
unjam [archive file path]
```

Simply enter the archive file path as an argument to the `unjam` executable to decompress and unpack the archive file in the current working directory.  The archive and compression types are detected by examination of the file extension in a case-insensitive manner.


### License

[MIT license](https://github.com/chrissimpkins/jampack/LICENSE)




