import logging

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
    try:
        to = request.form['to']
        subject = request.form['subject']
        content = request.form['content']
    except KeyError:
        return jsonify(basic_response(ERROR, 'not enough arguments'))

    # TODO: send(to, subject, content)
    mail.send(to, subject, content)
    logging.debug('Sending mail to %s, subject %s, content %s' % (to, subject, content[:10]))

    return jsonify(basic_response(SUCCESS))


if __name__ == '__main__':
    app.run()
