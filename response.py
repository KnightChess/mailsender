# response code

SUCCESS = 0
ERROR = 1


def basic_response(code, msg=None, data=None):
    if not isinstance(code, int):
        raise ValueError("code must be assigned an integer")
    if msg is None:
        msg = {
            SUCCESS: "success",
            ERROR: "error"
        }[code]
    return {
        'code': code,
        'msg': msg,
        'data': data
    }
