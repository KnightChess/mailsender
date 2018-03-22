# Mail Sender

## Guide

Copy `accounts.json.example` to `accounts.json`, and edit it with your own email account

Running by `python app.py`

and `POST localhost:5000/send`

| Field Name | Description                  | Reqired/Optional | Default Value |
| ---------- | ---------------------------- | ---------------- | ------------- |
| to         | Receiver's email address     | required         |               |
| subject    | Email's subject              | required         |               |
| content    | Email's content              | required         |               |
| alias      | Senders' email account alias | optional         | 'defalt'      |
| html       | use html or not              | optional         | False         |

> Using [httpie](https://github.com/jakubroztocil/httpie): `http -fv POST "locahost:5000/send" to=foo@bar.com subject=foo content=bar`

## Contribution Guide

1.  Install [virtualenv](https://virtualenv.pypa.io/en/stable/) and activate an venv
2.  Install dependencies by runnig `pip install -r requirements.txt`
3.  Copy `accounts.json.example` to `accounts.json`, and edit it with your own email account
4.  Run unittest: `python test.py`
5.  Unittest file should ends with `_test.py`
