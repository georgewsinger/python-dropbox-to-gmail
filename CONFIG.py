gmail_user = 'your_user_name@gmail.com'
gmail_pwd = 'your_password'

dropbox_path_to_gmail = '/path/to/your/file' # note that the root of this path designateѕ your Dropbox directory

# Get your Dropbox ACCESS_TOKEN via https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'

# Gmail Headers
FROM = 'First Last <your_user_name@gmail.com>'
TO = 'First Last <your_recipient_email@gmail.com>' # this may need to be different from the actual recipient of the gmail
SUBJECT = "SUBJECT"
# CC = 'First Last <user@gmail.com>'

# This is who actually receives the gmail
RECIPIENTS = ['your_recipient@gmail.com']
