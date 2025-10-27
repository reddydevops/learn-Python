import os
import sys
from typing import Optional

from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import Sku, StorageAccountCreateParameters
from azure.core.exceptions import AzureError

# Example: Deploy an Azure Storage Account (replace with your resource and parameters)
resource_group = os.environ.get("AZURE_RESOURCE_GROUP", "myResourceGroup")
storage_account = os.environ.get("AZURE_STORAGE_ACCOUNT", "mystorageacct123")
location = os.environ.get("AZURE_LOCATION", "eastus")


def get_subscription_id() -> str:
    """Return the subscription id from environment or raise a helpful error."""
    sub = os.environ.get("AZURE_SUBSCRIPTION_ID")
    if not sub:
        raise RuntimeError(
            "AZURE_SUBSCRIPTION_ID environment variable is not set. "
            "Set it to the target subscription ID before running this script."
        )
    return sub


def deploy_storage_account(
    account_name: str = storage_account,
    resource_group_name: str = resource_group,
    location_name: str = location,
    subscription_id: Optional[str] = None,
):
    """Create an Azure Storage Account using the Azure SDK and DefaultAzureCredential.

    This function uses DefaultAzureCredential which supports multiple auth flows
    (managed identity, environment, Visual Studio, Azure CLI token, etc.). In CI
    environments (GitHub Actions) you typically configure a service principal and
    set environment variables or use the `azure/login` action.
    """

    if subscription_id is None:
        subscription_id = get_subscription_id()

    credential = DefaultAzureCredential()

    client = StorageManagementClient(credential, subscription_id)

    params = StorageAccountCreateParameters(
        sku=Sku(name="Standard_LRS"),
        kind="StorageV2",
        location=location_name,
    )

    try:
        poller = client.storage_accounts.begin_create(
            resource_group_name, account_name, params
        )
        result = poller.result()  # wait for completion
        return result
    except AzureError as exc:
        # Re-raise with a clearer message for callers
        raise RuntimeError(f"Azure SDK error during storage account creation: {exc}") from exc


python -m ppython -m ppython -m ppython -m pip install -r requirements.txt
    try:
        res = deploy_storage_account()
        print("Storage account deployment successful.")
        # Optionally print a small summary
        try:
            print(f"Name: {res.name} | Location: {res.location} | SKU: {res.sku.name}")
        except Exception:
            pass
    except Exception as e:
        print(f"Deployment failed: {e}")
        sys.exit(1)