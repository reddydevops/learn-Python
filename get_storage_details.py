import os
import sys
import argparse
from typing import Any, Dict, Optional

from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from azure.core.exceptions import AzureError


def get_subscription_id() -> str:
    sub = os.environ.get("AZURE_SUBSCRIPTION_ID")
    if not sub:
        raise RuntimeError(
            "AZURE_SUBSCRIPTION_ID environment variable is not set. "
            "Set it to the target subscription ID before running this script."
        )
    return sub


def get_storage_account_details(
    account_name: str, resource_group_name: Optional[str] = None, subscription_id: Optional[str] = None
) -> Dict[str, Any]:
    if subscription_id is None:
        subscription_id = get_subscription_id()

    credential = DefaultAzureCredential()
    client = StorageManagementClient(credential, subscription_id)

    try:
        if resource_group_name:
            acc = client.storage_accounts.get_properties(resource_group_name, account_name)
        else:
            # If resource group is not provided, try to locate the account by listing
            # accounts in the subscription (may be slower for large subscriptions).
            for rg in client.resource_groups.list():
                try:
                    acc = client.storage_accounts.get_properties(rg.name, account_name)
                    break
                except AzureError:
                    acc = None
            if acc is None:
                raise RuntimeError(f"Storage account '{account_name}' not found in subscription.")

        # Convert object to dict-like structure for simple access
        details = {
            "name": acc.name,
            "location": acc.location,
            "sku": getattr(acc.sku, "name", None),
            "kind": getattr(acc, "kind", None),
            "primary_endpoints": getattr(acc, "primary_endpoints", None),
            "id": getattr(acc, "id", None),
            "tags": getattr(acc, "tags", None),
        }
        return details
    except AzureError as exc:
        raise RuntimeError(f"Azure SDK error while fetching storage account details: {exc}") from exc


def format_summary(details: Dict[str, Any]) -> str:
    name = details.get("name", "<unknown>")
    sku = details.get("sku", "<unknown>")
    kind = details.get("kind", "<unknown>")
    location = details.get("location", "<unknown>")
    endpoints = details.get("primary_endpoints") or {}
    blob = endpoints.get("blob") if isinstance(endpoints, dict) else endpoints

    return (
        f"Name: {name}\n"
        f"Location: {location}\n"
        f"SKU: {sku}\n"
        f"Kind: {kind}\n"
        f"Blob endpoint: {blob or '<none>'}\n"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get Azure Storage Account details using Azure SDK and DefaultAzureCredential.")
    parser.add_argument("-n", "--name", help="Storage account name", required=True)
    parser.add_argument("-g", "--resource-group", help="Resource group name (optional)")
    parser.add_argument("-s", "--subscription", help="Subscription ID (optional)")

    args = parser.parse_args()

    try:
        details = get_storage_account_details(args.name, args.resource_group, args.subscription)
        print(format_summary(details))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
