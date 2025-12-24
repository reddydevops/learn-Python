# Python Project

## Project Name and Description
This repository contains a collection of Python scripts and modules for various automation, data, and utility tasks. The project is designed to be modular and extensible, allowing users to add new scripts and functionality as needed.

## Technology Stack
- Python 3.x
- Standard Python libraries (subprocess, sys, etc.)
- Azure SDK (azure-identity, azure-mgmt-storage, azure-core)
- Snowflake Connector (snowflake-connector-python)

## Project Architecture
The project is organized as a flat structure with individual Python scripts for different functionalities. Each script is self-contained and can be run independently. There is currently no centralized application architecture or framework in use.

## Getting Started
1. Clone the repository:
   ```sh
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```sh
   cd python
   ```
3. Run any script using Python:
   ```sh
   python scriptname.py
   ```

### Azure scripts (setup)

The repository contains scripts that interact with Azure (for example `importsql.py` and `get_storage_details.py`). To use these scripts you should:

1. Install the Python dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
2. Set these environment variables (or export them in your CI environment):
   - `AZURE_SUBSCRIPTION_ID` — target subscription id (required)
   - `AZURE_RESOURCE_GROUP` — resource group name (optional; default in scripts)
   - `AZURE_STORAGE_ACCOUNT` — storage account name (optional; default in scripts)
   - `AZURE_LOCATION` — Azure region (optional; default `eastus`)

3. Authenticate: In local development you can use `az login`. In CI (GitHub Actions) use the `azure/login` action and set `AZURE_CREDENTIALS` secret. The scripts use `DefaultAzureCredential` so multiple auth flows are supported.

4. Example (deploy storage account):
   ```powershell
   python importsql.py
   ```

### Snowflake scripts (setup)

The repository contains scripts that interact with Snowflake (for example `deploy_snowflake_sql.py`). To use these scripts you should:

1. Install the Python dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
2. Set these environment variables (or export them in your CI environment):
   - `SNOWFLAKE_ACCOUNT` — Snowflake account identifier (required)
   - `SNOWFLAKE_USER` — Snowflake user (required)
   - `SNOWFLAKE_PASSWORD` — Snowflake password (required)
   - `SNOWFLAKE_WAREHOUSE` — Snowflake warehouse (optional)
   - `SNOWFLAKE_DATABASE` — Snowflake database (optional)
   - `SNOWFLAKE_SCHEMA` — Snowflake schema (optional)
   - `SNOWFLAKE_ROLE` — Snowflake role (optional)

3. Example (deploy SQL file):
   ```powershell
   python deploy_snowflake_sql.py --sql-file my_script.sql
   ```


## Project Structure
- `main.py` - Example script with a simple add function
- `importsql.py` - Script for deploying Azure Storage Account
- `deploy_snowflake_sql.py` - Script for deploying SQL to Snowflake
- `get_storage_details.py` - Script for querying Azure Storage Account details
- `learn.py` - Various Python function examples
- `classes.py`, `files.py`, `info.py`, etc. - Additional scripts
- `.github/` - GitHub configuration and prompts

## Key Features
- Modular Python scripts for different tasks
- Example code for Azure resource deployment
- Demonstrations of Python functions and programming concepts

## Development Workflow
- Scripts can be developed and tested independently
- No specific branching strategy or CI/CD workflow is currently documented

## Coding Standards
- Follow PEP 8 for Python code style
- Use clear function and variable names
- Include docstrings and comments where appropriate

## Testing
- No automated tests are currently included
- Scripts can be tested manually by running them with sample inputs

## Contributing
- Fork the repository and create a new branch for your feature or bugfix
- Submit a pull request with a clear description of your changes
- Follow the coding standards outlined above

## License
No license information provided yet.
