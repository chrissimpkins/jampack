Source Repository: https://github.com/chrissimpkins/jampack

What is JamPack?
------------------

JamPack includes the executables ``jam`` and ``unjam`` that provide a simple approach to pack and unpack tar.gz, tar.bz2, and zip file archives, respectively.  No more alphabet soup.

Install
---------

Install with ``pip`` using the command:

.. code-block:: bash

	$ pip install jampack

or `download the source repository <https://github.com/chrissimpkins/jampack/tarball/master>`_, unpack it, and navigate to the top level of the repository.  Then enter:

.. code-block:: bash

	$ python setup.py install

Usage
---------

.. code-block:: bash

	$ jam [secondary command] [directory path]

.. code-block:: bash

	$ unjam <archive file path>


Compress and Archive the Current Working Directory (tar.gz default)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

	$ jam

Compress and Archive the Current Working Directory (tar.bz2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

	$ jam bz2


Compress and Archive the Current Working Directory (zip)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

	$ jam zip


Compress and Archive Explicit Directory (tar.gz default)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

	$ jam [directory path(s)]

Compress and Archive Explicit Directory (tar.bz2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

	$ jam bz2 [directory path(s)]


Compress and Archive Explicit Directory (zip)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

	$ jam zip [directory path(s)]


Decompress and Unpack a tar.gz, tar.bz2, or zip Archive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

	$ unjam [tar.gz archive path]


.. code-block:: bash

	$ unjam [tar.bz2 archive path]


.. code-block:: bash

	$ unjam [zip archive path]


The archive and compression types are detected automatically.


Help
------------

.. code-block:: bash

	$ jam help


.. code-block:: bash

	$ unjam help


License
----------------

Licensed under the MIT license.  The full text of the license is available at `https://github.com/chrissimpkins/jampack/blob/master/LICENSE`_
