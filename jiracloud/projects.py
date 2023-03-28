class Projects(object):
    def __init__(self, client):
        self._client = client

    def get_projects_paginated(self, params=None):
        """
        Returns projects visible to the user.

        This operation can be accessed anonymously.
        """
        return self._client._get(self._client._BASE_URL + 'project/search', params=params)
