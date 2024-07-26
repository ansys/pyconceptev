.. _ref_user_guide:

User guide
##########

This section explains how to use PyConceptEV.

Get a token using AnsysID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get a token by creating a MSAL (Microsoft Authentication Library) app to communicate with the AnsysID system.
Use this app to create a token.
The token is cached within a file called `token_cache.bin`.

.. code-block:: python

    from ansys.pyconcceptev.core import auth

    app = auth.create_msal_app()
    token = auth.get_ansyId_token(app)

Create a client
^^^^^^^^^^^^^^^

Create a client that can access and talk to the Ansys ConceptEV API. You can use
the health check endpoint to check your connection.

.. code-block:: python

   import ansys.conceptev.core.main as pyconceptev

   with pyconceptev.get_http_client(token, concept_id) as client:
       health = get(client, "/health")
       print(health)


Configure a session using OnScale Cognito (deprecated)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create an ``ENV`` file to keep your username and password.
The file should look like this:

.. code-block:: bash

   CONCEPTEV_USERNAME = joe.blogs@my_work.com
   CONCEPTEV_PASSWORD = sup3r_s3cr3t_passw0rd


Get a token using OnScale Cognito (deprecated)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Import the PyConceptEV core module and use the :code:`get_token()` method to get a
a random access string from the server.

.. code-block:: python

   import ansys.conceptev.core.main as pyconceptev

   token = pyconceptev.get_token()



