class Issues(object):
    def __init__(self, client):
        self._client = client

    def get_issue(self, issue_id, params=None):
        """
        Returns the details for an issue.

        The issue is identified by its ID or key, however, if the identifier doesn't 
        match an issue, a case-insensitive search and check for moved issues is 
        performed. If a matching issue is found its details are returned, a 302 or 
        other redirect is not returned. The issue key returned in the response is the 
        key of the issue found.

        This operation can be accessed anonymously.
        """
        return self._client._get(self._client._BASE_URL + 'issue/{}'.format(issue_id), params=params)

    def create_issue(self, data, params=None):
        """
        Creates an issue or, where the option to create subtasks is enabled in Jira, 
        a subtask. A transition may be applied, to move the issue or subtask to a 
        workflow step other than the default start step, and issue properties set.

        The content of the issue or subtask is defined using update and fields. 
        The fields that can be set in the issue or subtask are determined using the 
        Get create issue metadata. These are the same fields that appear on the 
        issue's create screen. Note that the description, environment, and any 
        textarea type custom fields (multi-line text fields) take Atlassian Document 
        Format content. Single line custom fields (textfield) accept a string and 
        don't handle Atlassian Document Format content.

        Creating a subtask differs from creating an issue as follows:

        issueType must be set to a subtask issue type (use Get create issue metadata 
        to find subtask issue types).

        parent MUST contain the ID or key of the parent issue.

        A parent MAY be supplied for any issue provided both parent and child are members 
        of the same next-gen project. In a classic project the parent field is only valid 
        for subtasks.
        """
        return self._client._post(self._client._BASE_URL + 'issue', data=data, params=params)

    def delete_issue(self, issue_id, params=None):
        """
        Deletes an issue.

        An issue cannot be deleted if it has one or more subtasks. To delete an issue with 
        subtasks, set deleteSubtasks. This causes the issue's subtasks to be deleted with 
        the issue.

        This operation can be accessed anonymously.
        """
        return self._client._delete(self._client._BASE_URL + 'issue/{}'.format(issue_id), params=params)

    def get_create_issue_metadata(self, params=None):
        """
        Returns details of projects, issue types within projects, and, when requested, 
        the create screen fields for each issue type for the user. Use the information 
        to populate the requests in Create issue and Create issues.

        The request can be restricted to specific projects or issue types using the query 
        parameters. The response will contain information for the valid projects, issue types, 
        or project and issue type combinations requested. Note that invalid project, issue type, 
        or project and issue type combinations do not generate errors.

        This operation can be accessed anonymously.
        """
        return self._client._get(self._client._BASE_URL + 'issue/createmeta', params=params)

    def search_for_issues_using_jql(self, data):
        """
        Searches for issues using JQL.

        There is a GET version of this resource that can be used for smaller JQL query expressions.

        This operation can be accessed anonymously.
        """
        return self._client._post(self._client._BASE_URL + 'search', json=data)
