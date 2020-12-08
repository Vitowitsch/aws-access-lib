import attr
import os
import tempfile
import boto3
import botocore
import unittest
import attr
from moto import mock_s3
from framework.s3 import access as s3access
MY_BUCKET = "bucket"
MY_PREFIX = "mock_folder"
REGION = "us-east-1"


@mock_s3
class TestDownloadJsonFiles(unittest.TestCase):
    client = None
    s3 = None

    def setUp(self):
        self.client = boto3.client(
            "s3",
            region_name=REGION,
            aws_access_key_id="fake_access_key",
            aws_secret_access_key="fake_secret_key",
        )
        self.s3 = boto3.resource(
            "s3",
            region_name=REGION,
            aws_access_key_id="fake_access_key",
            aws_secret_access_key="fake_secret_key",
        )
        self.client.create_bucket(Bucket=MY_BUCKET)
        current_dir = os.path.dirname(__file__)
        fixtures_dir = os.path.join(current_dir, "fixtures")
        _upload_fixtures(self.client, MY_BUCKET, fixtures_dir)

    def tearDown(self):
        bucket = self.s3.Bucket(MY_BUCKET)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()

    def test_download(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            s3access.get(MY_BUCKET, MY_PREFIX, tmpdir)
            mock_folder_local_path = os.path.join(tmpdir, MY_PREFIX)
            self.assertTrue(os.path.isdir(tmpdir),
                            '{}'.format(mock_folder_local_path))
            result = os.listdir(mock_folder_local_path)
            desired_result = ["bar.json", "foo.json"]
            self.assertCountEqual(result, desired_result)


def _upload_fixtures(client, bucket: str, fixtures_dir: str) -> None:
    fixtures_paths = [os.path.join(path,  filename) for path, _, files in os.walk(
        fixtures_dir) for filename in files]
    for path in fixtures_paths:
        key = os.path.relpath(path, fixtures_dir)
        print("{}".format(key))
        client.upload_file(Filename=path, Bucket=bucket, Key=key)
