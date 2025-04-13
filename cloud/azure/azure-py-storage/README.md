# Azure Storage and Python Example

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![uv](https://img.shields.io/badge/built%20with-uv-blueviolet)](https://astral.sh/blog/uv)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)

This project demonstrates the setup of Azure Storage alongside a simple Python application that interacts with it. It shows basic Azure CLI commands, libraries, and best practices.

## 1. Azure Configuration

Configure your Azure resources using the following commands, replacing placeholders with your values:

```bash
GNAME="..."      # Resource group name
SANAME="..."     # Storage account name
CNAME="..."      # Blob container name
TNAME="..."      # Table name

az login

# Create a resource group in the desired region:
az group create --name $GNAME --location westeurope

# OPT: List storage accounts in the resource group:
az storage account list --resource-group $GNAME

# Create a storage account with Standard_LRS:
az storage account create --name $SANAME --resource-group $GNAME --location westeurope --sku Standard_LRS

# OPT: Update the storage account to use the Cool access tier:
az storage account update --name $SANAME --resource-group $GNAME --access-tier Cool

# OPT: Show details of the storage account:
az storage account show --name $SANAME

# Create a blob container with no public access:
az storage container create --account-name $SANAME --name $CNAME --public-access off

# Create a table for key-value storage:
az storage table create --name $TNAME --account-name $SANAME

# Retrieve the storage account connection string:
az storage account show-connection-string --name $SANAME --resource-group $GNAME # or
CONN_STRING=$(az storage account show-connection-string --name $SANAME --resource-group $GNAME --query connectionString -o tsv)
cp .env.example .env
echo "AZURE_STORAGE_CONNECTION_STRING=\"$CONN_STRING\"" >> .env
echo "AZURE_CONTAINER_NAME=\"$CNAME\"" >> .env
echo "AZURE_TABLE_NAME=\"$TNAME\"" >> .env

# OPT: Delete the resource group and all resources within it:
az group delete --name $GNAME --yes --no-wait
```

This setup provides a simple yet effective approach to working with Azure Storage services and a Python application. Modify the instructions as needed for your specific use case.


## 2. Setup the app

```bash
uv sync              # Synchronize and set up your virtual environment
uv run pytest
# Make sure your .env contains the correct values, example: .env.example
```

## 3. Run

```bash
uv run main.py
```
