# upload file onto Google Drive

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import SignedJwtAssertionCredentials
import base64, httplib2, pprint, subprocess, datetime
from string import capwords
from pytz import timezone

# from google API console - convert private key to base64 or load from file
id = "716534029983-2nijn8944oa2vukthtsv3ethg2m5kjgi.apps.googleusercontent.com"
key = base64.b64decode('MIIGwAIBAzCCBnoGCSqGSIb3DQEHAaCCBmsEggZnMIIGYzCCAygGCSqGSIb3DQEHAaCCAxkEggMVMIIDETCCAw0GCyqGSIb3DQEMCgECoIICsjCCAq4wKAYKKoZIhvcNAQwBAzAaBBQMh2cKlUsSomvjNNjeezDuqvLlEwICBAAEggKA0qj37oU++8Txshy8WIKR4s8qFVDlxrRWqRsCdmVL9KDwE7oMfiUi3xiafaaEOkntV0oEh5UeML0u6VckYYP2g5F94v32KAB/AbihLdw7W1HPs2DjHbKTaiHAAAq4K/FvlMLDiOxx3OIsaCW6R8oMfhvoFCfvL2ODC+J2VCxApvPizK5S+pS8w1wniDmMq3X6b1lzSx5U65cVPLvhrRbvH7lJo2k/1fxs60pNeoBdD6CCr+8550yc1FcZmBS+yQ/ynDl/c0AGd6gTemjLUMumCS0xLeA9YFr0vLoz4iZ65fEeXZQ0RnFBDN28hbyboHoUWfUAyn5b78PI+a57wWvUNsu0qrOtlTo3FvkKpxMCyazmnGoQwQjNHt/BEeEc/QqwhreufZugF9ldtqLw7WCDisWixj3fc4CeLjcGjDRmg/7UYmC53oSXA3Vw2l57NMfalPTCidO9i2Ro8DmfAWiyxfKM3ywL9B6miDGwbsXomcLZUyyw7ZD/B3e//HY5cjFNCmpCY85XYKIy9eBg0USyVqATZtrQK4bZPALfFMHTxqlvsYMRWLYkzFetCAu7WQmIhSCh7HlyqLSro6xX+to5phS24wcl3FYqO5kwyz7b6uY2H3Oiu7bUmkSEPOuWAnaPmSskvgIA0Ladd11MlfM54RfILkivEJCXxdrgqewFT0tBY8UmoZO/XqVPbyMzBwmU0BlOz92oYUMzszrzhceauz3eqPmGU6wWBdgUdc0gb1fcnh3EzsCVPOsbz7pkYbPkyMkvcV6pqUC8bTy2zhySZt9BEMmarKcgNQvsjMPUklDIoBlmY+GQkYfRTDKiDyPA2wthBxnSIc0umfSanHNXhDFIMCMGCSqGSIb3DQEJFDEWHhQAcAByAGkAdgBhAHQAZQBrAGUAeTAhBgkqhkiG9w0BCRUxFAQSVGltZSAxNDE5OTA5MTA1NDA0MIIDMwYJKoZIhvcNAQcGoIIDJDCCAyACAQAwggMZBgkqhkiG9w0BBwEwKAYKKoZIhvcNAQwBBjAaBBTlB0+jrdQbV2f0s/Mkz1uOhmXPkwICBACAggLg+DG5075D+ywocMy1vWAXV1OackSo8EYxWiFY4Wsd8xQjg4kVs5KFuM6a2MH1SlDqvpXfb4YeBd+xPKUkcGLofm3gvGN1J4edPJJ9gcGf8KfjWH7ZYAHsY+Y5itRjfuCrXiHIDkTR3oTfUlgiuV356fORWDGZXY/xssCOpbz9oM+bKLV56ouyl8kddl17Kyps5wWrG9DtxGcpn5nqLxEhcc0PNWqS/mwWqjezlT2lud94gfBsFC+VtoEQ/NI/oQ8af791ZO4ZSzA2ONjKhc7+urchln/AhljAWdn2oOV/X0r4uFaAMqTVt4aKSH3g9UC3Wok8Z3hk2cZp7ThWW5Qmy9quoUUttgi8I7wDpTO1udY2obUU+tUoLf5Hn8rByK6ePYlMmFtyByWNBTIUJg50t6TKBpLhQSwypEkUTYnk3XFNjneLXsAg524TLzkTWdlZDKw6q9I8CaXyX+8FltQ5STatc0hbPCro1KxesfezFvjhjrfmSnB3gfe927KsMQplgDdSs8Zx7Qff6q0Za0qtk0RW5xoVrFhLSJo0yNfu5jDsG5PC4SKNjua/CJWlNWQAYCmA5+Y8exwKQb0M7NBashkXl/Y+jPqxUjjgRepQM1PPFeUHgXd7g0tdT0TBI7IKCwhm9uKWbbK1wYzmEsWM7cBi1uR43C5coXZgGkDUTMwkWrvz36/v76fq7g3D4gidJGb6rHoF+w73kRFUhWL8fY8bU3fcvEViDbthnz04fDCwztXdj/bvI/iz3rbciCBtRg2ESjOkEf6KW+R+VJ1i83nfx1kW0X7qrHfx6E6OJXgOEpjA7nZt69FaG8UgIqQctlJ8Nt9DpvL0PPBA3lLyy9DUQdXGWjV1Ynzq+sthpRhfKkvIttfhXPX05JqYHPQE6Qo7GpVp/MXStMcYSyNdoKAIUlGRLMN9O3GOV+42YiA42AcXpz2rRwpqRtGG2TqdvrUOtIUffTZ8jJOzsIUb8zA9MCEwCQYFKw4DAhoFAAQUUbPA2qiFLIYjBn8dPv0ZNFQ+QkwEFHVGuCmn6/HiTew+7aZK2UqromR1AgIEAA==')

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
