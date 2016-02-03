import dropbox
import smtplib
import CONFIG

from email.mime.text import MIMEText

smtpserver = smtplib.SMTP("smtp.gmail.com",587)

def log_into_gmail():
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(CONFIG.gmail_user, CONFIG.gmail_pwd)

def get_gmail_text_from_dropbox_file():

    client = dropbox.client.DropboxClient(CONFIG.ACCESS_TOKEN)

    f, metadata = client.get_file_and_metadata(CONFIG.dropbox_path_to_gmail)
    cont = f.read().decode('UTF-8', 'ignore')
    f.close()
    return cont

def prep_text_for_gmail(original_text):

    # Here, we use Courier font, convert all \n to <br />,  and wrap everything in <pre></pre> to preserve spacing
    prepped_text = '<pre><font face="Courier New, Courier, monospace" style="font-size:12px">' + original_text + '</font></pre>'
    prepped_text = "<br />".join(prepped_text.split("\n"))
    return prepped_text

def send_gmail():
    gmail_text = prep_text_for_gmail(get_gmail_text_from_dropbox_file())

    MIME_object = MIMEText(gmail_text, 'html')
    MIME_object['From'] = CONFIG.FROM
    MIME_object['To'] = CONFIG.TO
  # MIME_object['Cc'] = CONFIG.CC
    MIME_object['Subject'] = CONFIG.SUBJECT
    MIME_string = MIME_object.as_string()

    smtpserver.sendmail(CONFIG.gmail_user, CONFIG.RECIPIENTS, MIME_string)

    print('Message sent.')

log_into_gmail()
send_gmail()
smtpserver.close()
