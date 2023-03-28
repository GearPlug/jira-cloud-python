class Webhooks(object):
    def __init__(self, client):
        self._client = client

    def get_webhook(self, webhook_id, params=None):
        return self._client._get(self._client._BASE_URL + 'webhook/{}'.format(webhook_id), params=params)

    def get_all_webhooks(self, params=None):
        return self._client._get(self._client._BASE_URL + 'webhook', params=params)

    def create_webhook(self, data):
        return self._client._post(self._client._BASE_URL + 'webhook', json=data)

    def delete_webhook(self, webhook_id, params=None):
        return self._client._delete(self._client._BASE_URL + 'webhook/{}'.format(webhook_id), params=params)
