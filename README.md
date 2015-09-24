# Google Realtime API - Python Example
This code will make a call to the google analytics realtime api to get current number of active users.

## Instructions

1. Create a service account in the google developer console. (https://console.developers.google.com/)

2. Generate a key (preferably in '.p12' format)

3. Go to the Google Analytics console and add the newly created service account (With Read and Analyse Permissions) on the 'Admin -> User Management' page.

4. Copy the key to the same directory as the python files.

5. In main.py set the following fields.

account_email = 'yourserviceaccount@developer.gserviceaccount.com'
keyfile = 'KEYNAME.p12'
analytics_view_id = 'ga:VIEW_ID'