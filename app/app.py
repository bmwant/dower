# -*- coding: utf-8 -*-
import smtplib
import os
import time
import shutil
import email.utils
from email.mime.text import MIMEText

from creator import Creator

from flask import Flask, render_template, request, Response

fj = os.path.join


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        project_name = request.form['name']
        project_type = request.form['type']
        creator = Creator(project_name, project_type)
        from colorama import Fore, Back, Style
        #print(Fore.RED + u'Юнікоде текстsome red text')
        return Response(creator.create(), content_type='text/event-stream')


@app.route('/sendmail', methods=['GET', 'POST'])
def sendmail():
    message = request.form['message']
    addr_from = request.form['from']
    addr_to = request.form['to']
    subject = request.form['subject']
    msg = MIMEText(message)
    msg['To'] = email.utils.formataddr(('Recipient', addr_to))
    msg['From'] = email.utils.formataddr(('Author', addr_from))
    msg['Subject'] = subject

    server = smtplib.SMTP('127.0.0.1', 25)
    #server.set_debuglevel(True)  # show communication with the server
    try:
        server.sendmail(addr_from, [addr_to], msg.as_string())
    finally:
        server.quit()
    return 'Message sended'


@app.route('/generate')
def genering():
    def generate():
        for i in range(5):
            yield str(i)
            time.sleep(1)
    return Response(generate())

if __name__ == '__main__':
    app.run(debug=True, port=27027)