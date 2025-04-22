from storages.backends.s3boto3 import S3Boto3Storage

class MinioMediaStorage(S3Boto3Storage):
    """
    Custom storage for media files on MinIO:
    - Uses S3 API for upload (credentials from settings)
    - Overrides url() to return a local path under /media/
    """
    custom_domain = False  # disable domain-based URLs
    default_acl = 'private'
    location = ''          # no extra prefix

    def url(self, name):
        # always return a relative URL served by our nginx proxy
        return f"/storage/media/{name}"
