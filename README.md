### py-aws-access

##### Setup

##### Prerequisisties

- python >=3.7
- poetry

##### Setup

1. Install poetry (as detailed on https://python-poetry.org/docs)
2. ```$ poetry install```

##### Tests
AWS-S3 and AWS-Athena resources are monkeypatched using *unittest*.

Yet the test-runner is *pytest* which support unitest-based tests out-of-the-box.

```$ poetry run pytest```
