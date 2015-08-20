<img src="https://raw.githubusercontent.com/chrissimpkins/jampack/master/img/jampack-header.png" alt="JamPack - simple file archives for everyone" width="728" />

## JamPack

> Simple file archives for everyone

### About

JamPack includes the executables `jam` and `unjam` that provide a simple approach to pack and unpack tar.gz, tar.bz2, and zip file archives, respectively.  No more alphabet soup.

### Install

JamPack requires Python v2.6+ or v3.2+ and you can install it with pip:

```shell
$ pip install jampack
```

or download the source repository, unpack it locally, navigate to the root directory, and run the command:

```shell
# python setup.py install
```

You can safely discard the source repository after you use this command.

### Usage

#### `jam` Usage

```
jam [secondary command] [directory path]
```

`jam` defaults to a tar.gz archive of the current working directory.  To create this simply navigate to the directory and enter:

```shell
$ jam
```






