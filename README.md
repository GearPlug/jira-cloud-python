# jira-cloud-python

jira-cloud-python is an API wrapper for Jira Software Cloud written in Python

## Installing
```
pip install jira-cloud-python
```

## Usage

#### Client instantiation
```
from jiracloud.client import Client

client = Client('CLIENT_ID', 'CLIENT_SECRET') # Host must have trailing slash
```

### OAuth 2.0 (3LO)

For more information: https://developer.atlassian.com/cloud/jira/platform/oauth-2-authorization-code-grants-3lo-for-apps/

#### Direct the user to the authorization URL to get an authorization code

A refresh token can be returned with the access token in your initial authorization flow. 
To do this, add the offline_access scope to the scope parameter of the authorization URL.

```
scope_list = ['read:jira-user', 'read:jira-work', 'write:jira-work', 'offline_access']
url = client.authorization_url('REDIRECT_URI', scope_list, 'STATE')
```

#### Exchange authorization code for access token
```
response = client.exchange_code('REDIRECT_URI', 'CODE')
```

#### Set access token in the library
```
client.set_access_token('ACCESS_TOKEN')
```

#### Get the cloudid for your site
```
response = client.get_resource_list()
```

#### Set cloudid in the library
```
client.set_cloud_id('CLOUD_ID')
```

#### Refresh token
```
response = client.refresh_token('REFRESH_TOKEN')
```

### Issues

#### Get issue
```
response = client.issues.get_issue('ISSUE_ID')
```

#### Create issue
```
data = {
  "update": {},
  "fields": {
    "summary": "something's wrong",
    "issuetype": {
      "id": "10000"
    },
    "components": [
      {
        "id": "10000"
      }
    ],
    "customfield_20000": "06/Jul/19 3:25 PM",
    "customfield_40000": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "text": "this is a text field",
              "type": "text"
            }
          ]
        }
      ]
    },
    "customfield_70000": [
      "jira-administrators",
      "jira-software-users"
    ],
    "project": {
      "id": "10000"
    },
    "description": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "text": "description",
              "type": "text"
            }
          ]
        }
      ]
    },
    "reporter": {
      "id": "99:e2a16dd9-2ffb-4a4b-a9bd-bd1145a020ee"
    },
    "fixVersions": [
      {
        "id": "10001"
      }
    ],
    "customfield_10000": "09/Jun/19",
    "priority": {
      "id": "20000"
    },
    "labels": [
      "bugfix",
      "blitz_test"
    ],
    "timetracking": {
      "remainingEstimate": "5",
      "originalEstimate": "10"
    },
    "customfield_30000": [
      "10000",
      "10002"
    ],
    "customfield_80000": {
      "value": "red"
    },
    "security": {
      "id": "10000"
    },
    "environment": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "text": "environment",
              "type": "text"
            }
          ]
        }
      ]
    },
    "versions": [
      {
        "id": "10000"
      }
    ],
    "duedate": "2019-05-11T00:00:00.000Z",
    "customfield_60000": "jira-software-users",
    "customfield_50000": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "text": "this is a text area. big text.",
              "type": "text"
            }
          ]
        }
      ]
    },
    "assignee": {
      "id": "e5:e1a16c14-1fe0-1c93-a2b1-ac4493ace0f1"
    }
  }
}
response = client.issues.create_issue(data)
```

#### Delete issue
```
response = client.issues.delete_issue('ISSUE_ID')
```

#### Get create issue metadata
```
response = client.issues.get_create_issue_metadata()
```

#### Search for issues using JQL
```
data = {
  "expand": [
    "names",
    "schema",
    "operations"
  ],
  "jql": "project = HSP",
  "maxResults": 15,
  "fieldsByKeys": false,
  "fields": [
    "summary",
    "status",
    "assignee"
  ],
  "startAt": 0
}
response = client.issues.search_for_issues_using_jql(data)
```

### Permissions

#### Get my permissions
```
response = client.permissions.get_my_permissions()
```

#### Projects
```
response = client.projects.get_projects_paginated()
```

#### Users
```
response = client.users.find_users_assignable_to_issues()
```

### Webhooks
Currently, webhooks are not available for OAuth 2.0 apps, for more information: https://ecosystem.atlassian.net/browse/ACJIRA-1632


## Contributing
We are always grateful for any kind of contribution including but not limited to bug reports, code enhancements, bug fixes, and even functionality suggestions.
#### You can report any bug you find or suggest new functionality with a new [issue](https://github.com/ingmferrer/jira-cloud-python/issues).
#### If you want to add yourself some functionality to the wrapper:
1. Fork it ( https://github.com/ingmferrer/jira-cloud-python )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Adds my new feature')
4. Push to the branch (git push origin my-new-feature)
5. Create a new Pull Request
