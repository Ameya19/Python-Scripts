import imaplib
import email
import os

# Email credentials
EMAIL = "" #Give your email address here
PASSWORD = "" #Give your email app password here

# Yahoo IMAP server
IMAP_SERVER = "imap.mail.yahoo.com"

# Directory to save attachments
SAVE_DIR = "attachments"

# You can filter emails by sender or by keyword in the email body. Uncomment the one you want to use and provide the necessary information.

# Sender filter
SENDER_EMAIL = "" #Give the email address of the sender you want to filter here

# Keyword filter
KEYWORD = "" #Give a keyword to filter emails here


def download_attachments():
    # Create directory if it doesn't exist
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    # Connect to Yahoo IMAP server
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, 993)

    # Login
    mail.login(EMAIL, PASSWORD)

    # Select inbox
    mail.select("inbox")

    # Search emails from specific sender
    #status, messages = mail.search(None, f'(FROM "{SENDER_EMAIL}")')
    status, messages = mail.search(None, f'(TEXT "{KEYWORD}")') #Give a keyword to filter emails here

    if status != "OK":
        print("No messages found!")
        return

    # Loop through email IDs
    for num in messages[0].split():

        # Fetch email
        status, data = mail.fetch(num, "(RFC822)")

        if status != "OK":
            print(f"Failed to fetch email {num}")
            continue

        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        # Walk through email parts
        for part in msg.walk():

            # Skip multipart containers
            if part.get_content_maintype() == "multipart":
                continue

            # Skip if no attachment
            if part.get("Content-Disposition") is None:
                continue

            # Get attachment filename
            filename = part.get_filename()

            if filename:
                filepath = os.path.join(SAVE_DIR, filename)

                # Save attachment
                with open(filepath, "wb") as f:
                    f.write(part.get_payload(decode=True))

                print(f"Downloaded: {filename}")

    # Logout
    mail.logout()


if __name__ == "__main__":
    download_attachments()