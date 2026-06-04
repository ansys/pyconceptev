.. _ref_user_guide:

User guide
##########

This section explains how to use PyConceptEV.

Create a client (local server — v2 API)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use ``get_local_client`` to connect to a locally running ConceptEV service at
``http://127.0.0.1:8080/api``.  No authentication is required.  The returned
client is a typed generated client that works directly with the v2 API modules.

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
           id=concept_id, part_type="configuration", client=client,
           body=AeroInput(name="Aero", drag_coefficient=0.3, cross_sectional_area=2.0),
       )
       mass = create_concept_part.sync(
           id=concept_id, part_type="configuration", client=client,
           body=MassInput(name="Mass", mass=2000.0),
       )
       wheel = create_concept_part.sync(
           id=concept_id, part_type="configuration", client=client,
           body=WheelInput(name="Wheel", rolling_radius=0.3),
       )

       # Add components
       transmission = create_concept_part.sync(
           id=concept_id, part_type="component", client=client,
           body=TransmissionLossCoefficientsInput(
               name="Transmission", gear_ratios=[5.0], headline_efficiencies=[0.95],
               max_torque=500.0, max_speed=2000.0, static_drags=[0.5], friction_ratios=[60.0],
           ),
       )
       battery = create_concept_part.sync(
           id=concept_id, part_type="component", client=client,
           body=BatteryFixedVoltagesInput(name="Battery", voltage_max=400.0),
       )

       # Add architecture
       arch = create_concept_part.sync(
           id=concept_id, part_type="architecture", client=client,
           body=ArchitectureInput(
               battery_id=battery.id,
               number_of_front_motors=1,
               front_transmission_id=transmission.id,
           ),
       )

       # Add requirement and submit job
       req = create_concept_part.sync(
           id=concept_id, part_type="requirement", client=client,
           body=DynamicRequirementInput(
               name="Req 1", aero_id=aero.id, mass_id=mass.id, wheel_id=wheel.id,
           ),
       )
       job = create_job.sync(
           concept_id=concept_id, client=client,
           body=JobRequest(
               name="My Job", requirement_ids=[req.id], architecture_id=arch.id,
           ),
       )
       print(f"Job submitted: {job.id}, status: {job.status}")


Create a client (cloud service — legacy API)
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
       BodyCreateFileV2ConceptIdFilesPost,
       MotorLabInput,
   )

   with open("e9.lab", "rb") as f:
       file_resp = create_file_item.sync(
           id=concept_id,
           client=client,
           body=BodyCreateFileV2ConceptIdFilesPost(file=f.read().decode("latin-1")),
           name="e9.lab",
           component_file_type="motor_lab_file",
       )

   motor = create_concept_part.sync(
       id=concept_id, part_type="component", client=client,
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
and the settings management will find it.
Most things can be left as default but the ``account_name`` should be changed
to match your company account name.

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


