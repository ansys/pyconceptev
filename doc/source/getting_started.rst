.. _ref_getting_started:

Getting started
###############

This section describes how to install PyConceptEV in user mode and
quickly begin using it. If you are interested in contributing to PyConceptEV,
see :ref:`ref_contributing` for information on installing in developer mode.


Installation
^^^^^^^^^^^^

Before installing PyConceptEV, make sure that you have the latest version
of `pip <https://pypi.org/project/pip/>`_ by running this command:

.. code:: bash

   python -m pip install -U pip

Then, install PyConceptEV with this command:

.. code:: bash

   python -m pip install ansys-conceptev-core

Optional Dependencies
^^^^^^^^^^^^^^^^^^^^^

To install the optional dependencies to run the examples script:

.. code:: bash

   python -m pip install ansys-conceptev-core[examples]

If you are using Linux and want to use the encryption features, you need to install
the optional dependencies for Linux encryption. For example on Debian Linux you need:

.. code:: bash

    sudo apt install libgirepository1.0-dev libcairo2-dev python3-dev gir1.2-secret-1
   python -m pip install ansys-conceptev-core[linux-encryption]

Other dependency groups are specified in the `pyproject.toml` file.
