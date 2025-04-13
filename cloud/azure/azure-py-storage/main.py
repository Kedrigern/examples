import os
import sys
import argparse
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient, ContainerClient
# from azure.storage.blob.aio import BlobServiceClient # async support
from azure.data.tables import TableServiceClient, TableClient

PARTITION: str = "kv"


def get_blob_container_client() -> ContainerClient:
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = os.getenv("AZURE_CONTAINER_NAME", "pytrysundaycontainer")
    if not connection_string:
        raise Exception("Connection string not defined in .env")
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    container_client.get_container_properties()
    return container_client


def get_table_client() -> TableClient:
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    table_name = os.getenv("AZURE_TABLE_NAME", "pytrysundaytable")
    if not connection_string:
        raise Exception("Connection string not defined in .env")
    table_service_client = TableServiceClient.from_connection_string(
        conn_str=connection_string
    )
    table_client = table_service_client.create_table_if_not_exists(
        table_name=table_name
    )
    return table_client


def blob_list(container_client) -> None:
    for blob in container_client.list_blobs():
        print(blob.name)


def blob_upload(container_client, file_path) -> None:
    file_name = os.path.basename(file_path)
    with open(file_path, "rb") as data:
        container_client.upload_blob(name=file_name, data=data, overwrite=True)
    print(f"Uploaded file '{file_name}'.")


def table_set(
    table_client: TableClient, key: str, value: str, partition: str = PARTITION
) -> None:
    entity = {"PartitionKey": partition, "RowKey": key, "Value": value}
    table_client.upsert_entity(entity=entity)
    print(f"Set key '{key}' -> '{value}'.")


def table_get(table_client: TableClient, key: str, partition: str = PARTITION) -> None:
    try:
        entity = table_client.get_entity(partition_key=partition, row_key=key)
        print(f"{entity['RowKey']}: {entity.get('Value')}")
    except Exception as e:
        print(f"Error getting key '{key}': {e}")


def table_list(table_client: TableClient, partition: str = PARTITION) -> None:
    for ent in table_client.list_entities(filter=f"PartitionKey eq '{partition}'"):
        print(f"{ent['RowKey']}: {ent.get('Value')}")


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser(description="Azure Storage CLI")
    subparsers = parser.add_subparsers(dest="command", title="Commands")

    file_parser = subparsers.add_parser("file", help="Blob storage commands")
    file_subparsers = file_parser.add_subparsers(
        dest="file_command", title="File Commands"
    )
    file_subparsers.add_parser("list", help="List files in blob storage")
    upload_parser = file_subparsers.add_parser(
        "upload", help="Upload a file to blob storage"
    )
    upload_parser.add_argument("filepath", nargs="?", help="Path to file to upload")

    val_parser = subparsers.add_parser("val", help="Table storage key-value commands")
    val_subparsers = val_parser.add_subparsers(dest="val_command", title="Val Commands")
    val_subparsers.add_parser("list", help="List key-value pairs")
    get_parser = val_subparsers.add_parser("get", help="Get value for a key")
    get_parser.add_argument("key", help="Key to retrieve")
    set_parser = val_subparsers.add_parser("set", help="Set a value for a key")
    set_parser.add_argument("key", help="Key to set")

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        return

    if args.command == "file":
        try:
            container_client = get_blob_container_client()
        except Exception as e:
            print(f"Error initializing blob container: {e}", file=sys.stderr)
            sys.exit(1)

        if args.file_command == "list":
            blob_list(container_client)
        elif args.file_command == "upload":
            filepath = args.filepath if args.filepath else input("Enter file path: ")
            if not os.path.isfile(filepath):
                print(
                    f"File '{filepath}' not found or not accessible.", file=sys.stderr
                )
                sys.exit(1)
            blob_upload(container_client, filepath)
        else:
            file_parser.print_help()

    elif args.command == "val":
        try:
            table_client = get_table_client()
        except Exception as e:
            print(f"Error initializing table storage: {e}", file=sys.stderr)
            sys.exit(1)

        if args.val_command == "list":
            table_list(table_client)
        elif args.val_command == "get":
            table_get(table_client, args.key)
        elif args.val_command == "set":
            value = input("Enter value: ")
            table_set(table_client, args.key, value)
        else:
            val_parser.print_help()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
