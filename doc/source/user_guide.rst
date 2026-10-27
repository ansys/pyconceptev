.. _ref_user_guide:

User guide
##########

This section explains how to use PyConceptEV.

Create a client (local server, v2 API)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use ``get_local_client`` to connect to the local ConceptEV service. If the
service is unavailable, ``ConceptEV.exe`` is started automatically and the
client waits for its health endpoint. No authentication is required. The
returned client is a typed generated client that works directly with the v2
API modules.

The ``LOCAL_SERVER_MODE`` setting selects ``gui`` (the default) or ``headless``.
By default, the executable is searched for in
``%ProgramFiles%/ANSYS Inc/{RELEASE}/motorcad`` for GUI mode and
``%ProgramFiles%/ANSYS Inc/{RELEASE}/motorcad/resources/desktop-api`` for
headless mode.  Override ``local_server_path``,
``local_server_headless_path``, or ``local_server_timeout`` in the settings for
custom installations.

.. code-block:: python

   from ansys.conceptev.core.app import get_local_client
   from ansys.conceptev.core.generated.api.concept_v2 import (
       create_concept,
       create_concept_part,
       create_job,
       get_job,
   )
   from ansys.conceptev.core.generated.models import (
       AeroInput,
       ArchitectureInput,
       BatteryFixedVoltagesInput,
       ConceptInput,
       DynamicRequirementInput,
       MassInput,
       TransmissionLossCoefficientsInput,
       WheelInput,
   )
   from ansys.conceptev.core.generated.models.job_request import JobRequest

   with get_local_client() as client:
       # Create a study
       concept = create_concept.sync(
           client=client,
           body=ConceptInput(name="My Study"),
       )
       concept_id = concept.id

       # Add configurations
       aero = create_concept_part.sync(
           id=concept_id,
           part_type="configuration",
           client=client,
           body=AeroInput(name="Aero", drag_coefficient=0.3, cross_sectional_area=2.0),
       )
       mass = create_concept_part.sync(
           id=concept_id,
           part_type="configuration",
           client=client,
           body=MassInput(name="Mass", mass=2000.0),
       )
       wheel = create_concept_part.sync(
           id=concept_id,
           part_type="configuration",
           client=client,
           body=WheelInput(name="Wheel", rolling_radius=0.3),
       )

       # Add components
       transmission = create_concept_part.sync(
           id=concept_id,
           part_type="component",
           client=client,
           body=TransmissionLossCoefficientsInput(
               name="Transmission",
               gear_ratios=[5.0],
               headline_efficiencies=[0.95],
               max_torque=500.0,
               max_speed=2000.0,
               static_drags=[0.5],
               friction_ratios=[60.0],
           ),
       )
       battery = create_concept_part.sync(
           id=concept_id,
           part_type="component",
           client=client,
           body=BatteryFixedVoltagesInput(name="Battery", voltage_max=400.0),
       )

       # Add architecture
       arch = create_concept_part.sync(
           id=concept_id,
           part_type="architecture",
           client=client,
           body=ArchitectureInput(
               battery_id=battery.id,
               number_of_front_motors=1,
               front_transmission_id=transmission.id,
           ),
       )

       # Add requirement and submit job
       req = create_concept_part.sync(
           id=concept_id,
           part_type="requirement",
           client=client,
           body=DynamicRequirementInput(
               name="Req 1",
               aero_id=aero.id,
               mass_id=mass.id,
               wheel_id=wheel.id,
           ),
       )
       job = create_job.sync(
           concept_id=concept_id,
           client=client,
           body=JobRequest(
               name="My Job",
               requirement_ids=[req.id],
               architecture_id=arch.id,
           ),
       )
       print(f"Job submitted: {job.id}, status: {job.status}")


Create a client (cloud service, legacy API)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the hosted Ansys ConceptEV cloud service, use ``get_http_client`` (legacy
raw ``httpx`` client with MSAL authentication) or ``get_conceptev_client``
(typed generated client with MSAL authentication).

The token is cached in a file called ``token_cache.bin``.  You can configure
the cache location with the ``cache_filepath`` argument.

.. code-block:: python

   from ansys.conceptev.core.app import get_conceptev_client

   with get_conceptev_client() as client:
       # Use with generated API modules (same as local client above)
       ...


Upload a file component
^^^^^^^^^^^^^^^^^^^^^^^

To use file-based components (motor lab files, battery lookup tables, etc.)
upload the file first, then reference the returned file ID when creating the
component:

.. code-block:: python

   from ansys.conceptev.core.generated.api.concept_v2 import (
       create_file_item,
       create_concept_part,
   )
   from ansys.conceptev.core.generated.models import (
       BodyCreateFileItem,
       MotorLabInput,
   )

   with open("e9.lab", "rb") as f:
       file_resp = create_file_item.sync(
           id=concept_id,
           client=client,
           body=BodyCreateFileItem(file=f.read().decode("latin-1")),
           name="e9.lab",
           component_file_type="motor_lab_file",
       )

   motor = create_concept_part.sync(
       id=concept_id,
       part_type="component",
       client=client,
       body=MotorLabInput(
           name="e9 Motor",
           lab_data_id=file_resp.id,
           max_speed=file_resp.calculated_values["max_speed"],
       ),
   )


Update configuration
^^^^^^^^^^^^^^^^^^^^

Update the configuration of the client by using the ``config.toml``. The
defaults are located in ``src/ansys/conceptev/core/resources/config.toml``.
Create a new ``config.toml`` file in your working directory with the
``account_name`` set or create an environment variable called ``ACCOUNT_NAME``
and the settings management uses it.
Most things can be left as default but the ``account_name`` should be changed
to match your company account name.

Authenticate without an interactive sign-in (PAT)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, ``get_http_client``/``get_conceptev_client`` sign in interactively
(a browser window) or via a cached token. For automation that can't complete
an interactive sign-in—CI pipelines, scheduled scripts, accounts protected by
SSO/MFA—use an Ansys **Personal Access Token (PAT)** instead. PyConceptEV
exchanges the PAT for a normal access token automatically (it is not used
directly as a bearer token); see the `PAT authentication guide
<https://developer.synopsys.com/docs/ansys-id-sso/pat-authentication-guide>`_
for background on how Ansys ID SSO handles this.

**Generate a PAT**

1. Go to `<https://id.ansys.com/>`_ and sign in with your Ansys ID.
2. Select the appropriate account if you belong to more than one.
3. Open your profile icon and select **Personal access token**.
4. Select **Create Token**, give it a name and expiration date, and set
   **Scope** to **Full Access**.
5. Copy the generated token—it's shown only once.

**Configure PyConceptEV to use it**

Set the ``ANSYS_UAT_PAT`` environment variable, or add ``ansys_uat_pat`` to
your ``config.toml``:

.. code-block:: toml

   ansys_uat_pat = "your_pat_value"

When set, it's tried before any interactive prompt. It's declared as a
Pydantic ``SecretStr`` setting, so it's masked (``**********``) if settings
are ever printed or logged, and never appears in tracebacks.

**Treat a PAT like a password**

- Never paste it directly into a terminal command (it ends up in your shell
  history); use a prompt that doesn't echo it, or a secrets manager.
- Never commit it to source control or share it with others.
- Give it the shortest expiration that's practical, and delete unused tokens.
- Rotate/revoke it immediately at `<https://id.ansys.com/>`_ if it's ever
  exposed.

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

**Note**: If no custom SSL certificate is configured, PyConceptEV uses the default certificate bundle provided by the `certifi` package.


