# Email 2 X

Several scripts to read mail input (from postfix, for example) and send it to various destinations. Some are coded very specifically to emails from DVR163 security camera software. 

**Email to PushBullet (email2bushbullet.py)**

Redirects email input to a PushBullet notification. Supports multipart emails with plaintext, html, and jpg parts. 

Note: This requires [pushbullet.py](https://github.com/rbrcsk/pushbullet.py).

**Email to Email (email2email.py)**

Forward email input to a new email address via SMTP. 

**Email to Dropbox (email2dropbox.py)**

Parses the image out of DVR163 emails and uploads it to Dropbox

**Email to File (email2file.py)**

Parses the image out of DVR163 emails and saves it as a file. 

## Example usage

Let's imagine that we want to redirect all emails sent to push@example.com as a PushBullet notification. Keep in mind that instructions below were tested on Raspbian with Python 2.7. 

### Step 0: Setup and configure postfix for domain example.com and other prerequisites

[This tutorial](https://www.stewright.me/2012/09/tutorial-install-postfix-to-allow-outgoing-email-on-raspberry-pi/) is super short but a good place to get your feet wet if you are coming from nothing. 

[This tutorial](https://samhobbs.co.uk/2013/12/raspberry-pi-email-server-part-1-postfix) goes more in-depth. 

### Step 1: Create shell script

First, create shell script which will contain the python call (email2pushbullet.py) with all the configurable arguments such as the API key. 

Let's name it `/var/spool/postfix/email2x/handle_email`.

Why there? Tested in Debian and Raspbian, and postfix's home dir is /var/spool/postfix.
Rememer, postfix should be able to acces your script.

The script will be something like this:

```
#!/bin/sh
/usr/bin/python /var/spool/postfix/email2x/email2pushbullet.py --key YOUR_PUSHBULLET_API_KEY 
```
Feel free to change/remove `log_level` or `log_file` as needed.

Make the script executable:

```
chmod +x /var/spool/postfix/email2x/email2pushbullet
```

Make the log file writeable:

```
chmod +w /var/spool/postfix/email2x/email2pushbullet.log
```

**Note:** For a more complex script example that forwards a copy of all emails to an address and only "pushes" certain messages based on the content, see  `handle_email.example`.


### Step 2: Add mail alias

Open /etc/aliases file and append a line there:

```
push: |/var/spool/postfix/email2x/handle_email
```
Save the file and execute `newaliases` command.


### Step 3: Test it

Send email to push@example.com and, if it didn't work, check /var/log/mail.log. If it did work you should receieve the push. 

That's it.
