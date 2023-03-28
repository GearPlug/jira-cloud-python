import requests

from jiracloud.exceptions import UnknownError, InvalidIDError, NotFoundIDError, NotAuthenticatedError, PermissionError
from jiracloud.issues import Issues
from jiracloud.permissions import Permissions
from jiracloud.projects import Projects
from jiracloud.users import Users
from jiracloud.webhooks import Webhooks
from urllib.parse import urlencode


class Client(object):
    BASE_URL = 'https://api.atlassian.com/ex/jira'
    API_URL = 'rest/api/3/'

    def __init__(self, client_id, client_secret):
        self._client_id = client_id
        self._client_secret = client_secret
        self._BASE_URL = None
        self._access_token = None
        self._cloud_id = None

        self.issues = Issues(self)
        self.permissions = Permissions(self)
        self.projects = Projects(self)
        self.users = Users(self)
        self.webhooks = Webhooks(self)

    def authorization_url(self, redirect_uri, scope, state):
        if not isinstance(scope, list):
            raise Exception('scope must be a list.')

        params = {
            'audience': 'api.atlassian.com',
            'client_id': self._client_id,
            'scope': ' '.join(scope),
            'redirect_uri': redirect_uri,
            'state': state,
            'response_type': 'code',
            'prompt': 'consent'
        }
        return 'https://auth.atlassian.com/authorize?' + urlencode(params)

    def exchange_code(self, redirect_uri, code):
        data = {
            'grant_type': 'authorization_code',
            'client_id': self._client_id,
            'client_secret': self._client_secret,
            'code': code,
            'redirect_uri': redirect_uri
        }
        return self._post('https://auth.atlassian.com/oauth/token', json=data)

    def refresh_token(self, refresh_token):
        data = {
            'grant_type': 'refresh_token',
            'client_id': self._client_id,
            'client_secret': self._client_secret,
            'refresh_token': refresh_token
        }
        return self._post('https://auth.atlassian.com/oauth/token', json=data)

    def set_access_token(self, access_token):
        if isinstance(access_token, dict):
            if 'access_token' not in access_token:
                raise Exception('token must have access_token')

            self._access_token = access_token['access_token']
        else:
            self._access_token = access_token

    def get_resource_list(self):
        return self._get('https://api.atlassian.com/oauth/token/accessible-resources')

    def set_cloud_id(self, cloud_id):
        self.cloud_id = cloud_id

        self._BASE_URL = '{}/{}/{}'.format(self.BASE_URL, cloud_id, self.API_URL)

    def _get(self, endpoint, **kwargs):
        return self._request('GET', endpoint, **kwargs)

    def _post(self, endpoint, **kwargs):
        return self._request('POST', endpoint, **kwargs)

    def _put(self, endpoint, **kwargs):
        return self._request('PUT', endpoint, **kwargs)

    def _delete(self, endpoint, **kwargs):
        return self._request('DELETE', endpoint, **kwargs)

    def _request(self, method, endpoint, headers=None, **kwargs):
        _headers = {'Authorization': 'Bearer {}'.format(self._access_token)}
        if headers:
            _headers.update(headers)
        return self._parse(requests.request(method, endpoint, headers=_headers, **kwargs))

    def _parse(self, response):
        status_code = response.status_code
        if 'Content-Type' in response.headers and 'application/json' in response.headers['Content-Type']:
            r = response.json()
        else:
            return response.text
        
        if not response.ok:
            message = None
            if 'message' in r:
                message = r['message']
            if 'errorMessages' in r:
                message = '. '.join(r['errorMessages'])
            if 'error_description' in r:
                message = r['error_description']
            
            if status_code == 400:
                raise InvalidIDError(message, response)
            if status_code == 401:
                raise NotAuthenticatedError(message, response)
            if status_code == 403:
                raise PermissionError(message, response)
            if status_code == 404:
                raise NotFoundIDError(message, response)
                
            raise UnknownError(message, response)

        return r
