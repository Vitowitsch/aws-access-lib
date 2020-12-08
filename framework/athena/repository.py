import contextlib
import os
from pyathenajdbc import connect
from pyathenajdbc.util import as_pandas
import pandas as pd


def get(query):
    print("running query..")
    with contextlib.closing(
            connect(s3_staging_dir=os.getenv('ATHENA_BUCKET', 'UNSET'),
                    region_name=os.getenv('AWS_REGION', 'UNSET'))) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            df = as_pandas(cursor)

    return df.values.tolist
