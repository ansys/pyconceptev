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


Update configuration
^^^^^^^^^^^^^^^^^^^^

Update the configuration of the client by using the `config.toml` the defaults are located in `src/ansys/conceptev/core/resources/config.toml`.
Create a new config.toml file in your working directory with the `account_name` set or create an environment variable called `ACCOUNT_NAME` and the settings management should find it.
Most things can be left as default but the `account_name` should be changed to match your `company account name`.
