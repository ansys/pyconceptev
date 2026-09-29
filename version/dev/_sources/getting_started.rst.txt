.. _ref_getting_started:

Getting started
###############

This section describes how to install PyConceptEV in user mode and
quickly begin using it. If you are interested in contributing to PyConceptEV,
see :ref:`ref_contributing` for information on installing in developer mode.


Installation
^^^^^^^^^^^^

.. note::
   These instructions assume you are familiar
   with ``pip`` and the command line. If they are new to you, you should read
   the `Python Packaging User Guide Tutorial on pip <https://packaging.python.org/en/latest/tutorials/installing-packages/>`
   before proceeding.

Before installing PyConceptEV, make sure that you have the latest version
of `pip <https://pypi.org/project/pip/>`_ by running this command:

.. code:: bash

   python -m pip install -U pip

Then, install PyConceptEV with this command:

.. code:: bash

   python -m pip install ansys-conceptev-core

Optional dependencies
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

Ansys developer ecosystem resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ansys has an extensive developer ecosystem where you can find assistance for a variety of issues.

- `Developer Portal <https://developer.ansys.com/>`_: Blog posts, documentation, and guide
- `Developer Forum <https://discuss.ansys.com/>`_: Scripting and usage support for PyAnsys and other Ansys developer tools
- `Ansys Innovation Space <https://innovationspace.ansys.com/>`_: Product support forum and training materials
- `GitHub <https://github.com/ansys/pyconceptev>`_: Development support, bug reporting, feature requests, and more.
- `Ansys Learning Hub <https://learninghub.ansys.com/>`_: Training, courses and learning plans
