Source Repository: `<https://github.com/chrissimpkins/jampack>`_

What is JamPack?
----------------------------

JamPack includes the executables ``jam`` and ``unjam`` that provide a simple approach to pack and unpack tar.gz, tar.bz2, and zip file archives, respectively.  No more alphabet soup. JamPack works on Linux, OS X, and Windows platforms.


Install
--------------

Install with ``pip`` using the command:

::

    $ pip install jampack


or `download the source repository <https://github.com/chrissimpkins/jampack/tarball/master>`_, unpack it, and navigate to the top level of the repository.  Then enter:


::

    $ python setup.py install



Usage
------------


::

    $ jam [secondary command] [directory path]


::

    $ unjam [archive file path]



Compress and Archive the Current Working Directory (tar.gz default)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


::

    $ jam


Compress and Archive the Current Working Directory (tar.bz2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


::

    $ jam bz2



Compress and Archive the Current Working Directory (zip)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


::

    $ jam zip



Compress and Archive Explicit Directory (tar.gz default)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


::

    $ jam [directory path(s)]



Compress and Archive Explicit Directory (tar.bz2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


::

    $ jam bz2 [directory path(s)]



Compress and Archive Explicit Directory (zip)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


::

    $ jam zip [directory path(s)]



Decompress and Unpack a tar.gz, tar.bz2, or zip Archive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


::

    $ unjam [tar.gz archive path]



::

    $ unjam [tar.bz2 archive path]



::

    $ unjam [zip archive path]



The archive and compression types are detected automatically.



Help
------------


::

    $ jam help



::

    $ unjam help



License
----------------

Licensed under the MIT license.  The full text of the license is available at `<https://github.com/chrissimpkins/jampack/blob/master/LICENSE>`_