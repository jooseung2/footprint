import boto3
from constants import BUCKET_NAME, REGION
import os


def upload_to_s3(username, file_obj):
    """
    return url to the image file stored in aws s3
    """
    filename = str(file_obj) + ".jpg"

    s3_client = boto3.client(
        service_name="s3",
        aws_access_key_id=os.environ["ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["SECRET_ACCESS_KEY"],
        region_name=REGION,
    )

    key = str(username) + "/" + filename
    s3_client.upload_file(filename, BUCKET_NAME, key)

    url = "https://{bucketname}.s3.{region}.amazonaws.com/{key}".format(
        BUCKET_NAME, REGION, key
    )
    return url
