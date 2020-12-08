from framework.model.feature import Feature
from framework.athena import repository


class FeatureAccess:

    def __init__(self, data_access=None):
        self._data_access = data_access or repository

    def get(self):
        return self._data_access.get("${SELECT_STATEMENT_HERE}")
