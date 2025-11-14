.. _ref_user_guide:

User guide
##########

This section explains how to use PyConceptEV.

Create a client
^^^^^^^^^^^^^^^

Create a client that can access and talk to the Ansys ConceptEV API. You can use
the health check endpoint to check your connection.
The token is cached within a file called `token_cache.bin` you can configure the cache location with
an argument to the `get_http_client` function `cache_filepath`.

.. code-block:: python

   import ansys.conceptev.core.main as pyconceptev

   with pyconceptev.get_http_client(
       concept_id, cache_filepath="token_cache.bin"
   ) as client:
       health = get(client, "/health")
       print(health)


Update configuration
^^^^^^^^^^^^^^^^^^^^

Update the configuration of the client by using the `config.toml` the defaults are located in `src/ansys/conceptev/core/resources/config.toml`.
Create a new config.toml file in your working directory with the `account_name` set or create an environment variable called `ACCOUNT_NAME` and the settings management should find it.
Most things can be left as default but the `account_name` should be changed to match your `company account name`.

Configure SSL certificate for company networks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you're working behind a corporate firewall or need to use custom SSL certificates, you can configure PyConceptEV to use a custom PEM certificate file instead of the default certificate bundle.

**Option 1: Using environment variable (recommended)**

Set the `SSL_CERT_FILE` environment variable to point to your custom certificate file:

.. code-block:: bash

   # Windows Command Prompt
   set SSL_CERT_FILE=C:\path\to\your\certificate.pem

   # Windows PowerShell
   $env:SSL_CERT_FILE="C:\path\to\your\certificate.pem"

   # Linux/macOS
   export SSL_CERT_FILE=/path/to/your/certificate.pem

**Option 2: Using config.toml file**

Add the `ssl_cert_file` setting to your `config.toml`:

.. code-block:: toml

   ssl_cert_file = "/path/to/your/certificate.pem"
   account_name = "your_company_account"

**Creating a custom certificate bundle**

If your company provides a custom CA certificate, you may need to combine it with the default certificates:

.. code-block:: bash

   # On Windows (using PowerShell)
   Get-Content "C:\path\to\company-ca.pem", "C:\path\to\certifi\cacert.pem" | Out-File -Encoding ascii "custom-bundle.pem"

   # On Linux/macOS
   cat /path/to/company-ca.pem /path/to/default/cacert.pem > custom-bundle.pem

Then set the `SSL_CERT_FILE` environment variable or `ssl_cert_file` config option to point to your `custom-bundle.pem` file.

**Note**: If no custom SSL certificate is configured, PyConceptEV will use the default certificate bundle provided by the `certifi` package.


