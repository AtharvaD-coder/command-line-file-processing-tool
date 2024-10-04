User Guide
==========

The File Processor is a command-line tool that allows you to perform various operations on text files.

Basic Usage
-----------

.. code-block:: bash

   python src/processor.py -f <path_to_file> [options]

For detailed information on available options, see the :doc:`command_line_tools` section.

Example Usage
-------------

1. Count words and characters in a file:

   .. code-block:: bash

      python src/processor.py -f sample.txt -wc -cc

2. Find a specific word in a file:

   .. code-block:: bash

      python src/processor.py -f sample.txt -find "example"

3. Replace a word in a file:

   .. code-block:: bash

      python src/processor.py -f sample.txt -r "old" "new"

For more examples and detailed explanations, see the :doc:`process_text_file` section.

.. image:: _static/example_output.png
   :alt: Example output of the File Processor
   :width: 600

This image shows an example output of the File Processor when run with various options.