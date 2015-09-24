import httplib2
from apiclient.discovery import build
from oauth2client import client, file, tools
from oauth2client.client import SignedJwtAssertionCredentials

class GoogleAPI:
    def authenticate(api_name, api_version, scope, key_file_location, service_account_email):
        f = open(key_file_location, 'rb')
        key = f.read()
        f.close()
        credentials = SignedJwtAssertionCredentials(service_account_email, key, scope=scope)
        service = build(api_name, api_version, http=credentials.authorize(httplib2.Http()))
        return service
    
    def get_active_users(account_email, key_file, analytics_view_id):
        scope = ['https://www.googleapis.com/auth/analytics.readonly']
        service = GoogleAPI.authenticate('analytics', 'v3', scope, key_file, account_email)
        results = service.data().realtime().get(ids=analytics_view_id, metrics='rt:activeUsers', dimensions='rt:medium').execute()
        totals = results.get('totalsForAllResults')
        return int(totals.get("rt:activeUsers"))
    
