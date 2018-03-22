import logging
from http import HTTPStatus

from flask import Flask
from flask import jsonify
from flask import request

import mail
from response import basic_response, SUCCESS, ERROR

app = Flask(__name__)
# TODO: this should be put in config file
logging.basicConfig(filename='app.log', level=logging.DEBUG)


@app.route('/send', methods=['POST'])
def post_send():
    # to, subject, content are required fields
    try:
        to = request.form['to']
        subject = request.form['subject']
        content = request.form['content']
    except KeyError:
        return jsonify(basic_response(ERROR, 'not enough arguments'))

    # alias and html are optional fields
    try:
        alias = request.form['alias']
    except KeyError:
        alias = 'default'

    try:
        html = request.form['html']
        if html == 1 or str(html).lower() == 'true':
            html = True
        else:
            html = False
    except KeyError:
        html = False

    try:
        mail.send(to, subject, content, alias, html)
    except Exception as e:
        # sending failed
        logging.error('Sending mail to %s, subject %s, content %s, error %s' % (to, subject, content[:10], repr(e)))
        return jsonify(basic_response(ERROR, repr(e))), HTTPStatus.INTERNAL_SERVER_ERROR

    # sending succeeded
    logging.debug('Sending mail to %s, subject %s, content %s' % (to, subject, content[:10]))
    return jsonify(basic_response(SUCCESS)), HTTPStatus.CREATED


if __name__ == '__main__':
    app.run()
