class Permissions(object):
    def __init__(self, client):
        self._client = client

    def get_my_permissions(self, params=None):
        """
        Returns a list of permissions indicating which permissions the user has. 
        Details of the user's permissions can be obtained in a global, project, or issue context.

        The user is reported as having a project permission:

        in the global context, if the user has the project permission in any project.

        for a project, where the project permission is determined using issue data, 
        if the user meets the permission's criteria for any issue in the project. 
        Otherwise, if the user has the project permission in the project.

        for an issue, where a project permission is determined using issue data, 
        if the user has the permission in the issue. Otherwise, if the user has 
        the project permission in the project containing the issue.

        This means that users may be shown as having an issue permission (such as EDIT_ISSUE) 
        in the global context or a project context but may not have the permission for any or 
        all issues. For example, if Reporters have the EDIT_ISSUE permission a user would be 
        shown as having this permission in the global context or the context of a project, 
        because any user can be a reporter. However, if they are not the user who reported 
        the issue queried they would not have EDIT_ISSUE permission for that issue.

        Global permissions are unaffected by context.

        This operation can be accessed anonymously.
        """
        return self._client._get(self._client._BASE_URL + 'mypermissions', params=params)
