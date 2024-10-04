Usage Guide
===========

The File Processor is a command-line tool that allows you to perform various operations on text files.

Basic Usage
-----------

.. code-block:: bash

   python processor.py -f <path_to_file> [options]

Command-line Options
--------------------

- ``-f`` or ``--file``: The path to the input text file (required).
- ``-wc`` or ``--word-count``: Display the total word count.
- ``-cc`` or ``--char-count``: Display the total character count.
- ``-find``: A specific word to search in the text file.
- ``-r`` or ``--replace``: Replace a word in the text file with another word. Usage: ``-r old_word new_word``

Example
-------

.. code-block:: bash

   python processor.py -f sample.txt -wc -cc -find "example" -r "old" "new"