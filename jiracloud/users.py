class Users(object):
    def __init__(self, client):
        self._client = client

    def find_users_assignable_to_issues(self, params=None):
        """
        Returns a list of users that can be assigned to an issue. Use this operation 
        to find the list of users who can be assigned to:

        a new issue, by providing the projectKeyOrId.

        an updated issue, by providing the issueKey.

        to an issue during a transition (workflow action), by providing the issueKey 
        and the transition id in actionDescriptorId. You can obtain the IDs of an issue's
        valid transitions using the transitions option in the expand parameter of Get issue.

        In all these cases, you can pass an accountId to determine if a user can be assigned 
        to an issue. The user is returned in the response if they can be assigned to the issue 
        or issue transition.
        """
        return self._client._get(self._client._BASE_URL + 'user/assignable/search', params=params)
