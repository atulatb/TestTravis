# upload file onto Google Drive

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import SignedJwtAssertionCredentials
import base64, httplib2, pprint, subprocess, datetime
from string import capwords
from pytz import timezone

# from google API console - convert private key to base64 or load from file
id = "716534029983-2nijn8944oa2vukthtsv3ethg2m5kjgi.apps.googleusercontent.com"
key = base64.b64decode('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')

# get credentials
credentials = SignedJwtAssertionCredentials(id, key, scope='https://www.googleapis.com/auth/drive')
http = httplib2.Http()
http = credentials.authorize(http)

# initi drive_service
drive_service = build('drive', 'v2', http=http)

COMMAND_GIT_LOG = 'git log -1 --pretty=%B'
process = subprocess.Popen(COMMAND_GIT_LOG, stdout=subprocess.PIPE, shell=True)
(output, err) = process.communicate()
pprint.pprint(capwords(output.rstrip('\n')).replace(" ", ""))

GIT_MESSAGE = capwords(output.rstrip('\n')).replace(" ", "")
DATETIME = datetime.datetime.now(timezone('Asia/Tokyo')).strftime("%Y%m%d%H%M")


# name of file what will upload onto Google Drive
FILENAME = 'TestTravis-debug.apk'
# title of file what will show on [APKs] folder
TITLE = 'TestTravis-' + DATETIME + '-' + GIT_MESSAGE + '.apk'
# discription of file what will show when user mouse_hover on file item
DESCRIPTION = 'TestTravis-' + DATETIME + '-' + GIT_MESSAGE
# mime type of file
MIMETYPE = 'application/apk'
media_body = MediaFileUpload(FILENAME, mimetype=MIMETYPE, resumable=True)
body = {
  'title': TITLE,
  'description': DESCRIPTION,
  'mimeType': MIMETYPE
}
# folder Id of [APKs]
#https://drive.google.com/drive/#folders/0B9rB79o-kLR5NDRaTnc1a0Z6MTA
body['parents'] = [{'id': '0B9rB79o-kLR5NDRaTnc1a0Z6MTA'}]

# upload APK file onto [APKs] folder on Google Drive
file = drive_service.files().insert(body=body, media_body=media_body).execute()

# print log about file what just uploaded
pprint.pprint(file)
