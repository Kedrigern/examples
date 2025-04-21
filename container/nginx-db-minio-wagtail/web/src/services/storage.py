import os
from minio import Minio
from minio.error import S3Error


def human_readable_size(size_bytes: int) -> str:
    """
    Convert a size in bytes to a human-readable string (e.g., '1.23 MB').
    """
    for unit in ["B", "KB", "MB", "GB", "TB", "PB"]:
        if size_bytes < 1024 or unit == "PB":
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024


def get_minio_client() -> Minio:
    """
    Create and return a Minio client using environment variables.
    """
    endpoint = os.getenv(
        "MINIO_ENDPOINT",
        f"{os.getenv('MINIO_HOST', 'minio')}:{os.getenv('MINIO_PORT', '9000')}",
    )
    access_key = os.getenv("MINIO_ROOT_USER")
    secret_key = os.getenv("MINIO_ROOT_PASSWORD")
    secure = os.getenv("MINIO_SECURE", "false").lower() in ("1", "true", "yes")
    return Minio(endpoint, access_key=access_key, secret_key=secret_key, secure=secure)


def get_minio_info() -> dict:
    """
    Retrieve information about all buckets: names, object counts, and total sizes.
    """
    client = get_minio_client()
    info = {"buckets": []}
    try:
        buckets = client.list_buckets()
        for bucket in buckets:
            count = 0
            total_size = 0
            for obj in client.list_objects(bucket.name, recursive=True):
                count += 1
                total_size += obj.size
            info["buckets"].append(
                {
                    "name": bucket.name,
                    "object_count": count,
                    "total_size": human_readable_size(total_size),
                }
            )
    except S3Error as e:
        info["error"] = f"MinIO error: {e}"
    except Exception as e:
        info["error"] = f"Unexpected error: {e}"
    return info


def ensure_logo(bucket_name: str, local_path: str = "static/logo.png") -> str:
    """
    Ensure that 'logo.png' exists in the specified bucket. Uploads the file if missing,
    then returns a presigned URL valid for one hour.
    """
    client = get_minio_client()
    # Create bucket if it does not exist
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
    try:
        # Check if 'logo.png' exists in the bucket
        exists = any(
            obj.object_name == "logo.png"
            for obj in client.list_objects(
                bucket_name, prefix="logo.png", recursive=False
            )
        )
        if not exists:
            client.fput_object(
                bucket_name,
                'logo.png',
                local_path,
                content_type='image/png'
            )
        return f"/static/{bucket_name}/logo.png"
    except S3Error:
        return ""
    except Exception:
        return ""
