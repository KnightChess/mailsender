# response code
SUCCESS = 0
ERROR = 1

defaultCodeMsg = {
    SUCCESS: "success",
    ERROR: "error"
}


def basic_response(code, msg=None, data=None):
    if not isinstance(code, int):
        raise ValueError("code must be assigned an integer")
    if msg is None:
        try:
            msg = defaultCodeMsg[code]
        except KeyError:
            msg = None
    return {
        'code': code,
        'msg': msg,
        'data': data
    }
