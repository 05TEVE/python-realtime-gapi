from gapi import GoogleAPI

account_email = 'yourserviceaccount@developer.gserviceaccount.com'
keyfile = '<KEYNAME>.p12'
analytics_view_id = 'ga:<VIEW_ID>'
count = GoogleAPI.get_active_users(account_email, keyfile, analytics_view_id)

if count == 1:
    print('There is currently ' + str(count) + ' active user.')
else:
    print('There are currently ' + str(count) + ' active users.')