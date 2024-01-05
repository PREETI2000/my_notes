from notes.settings import RESPONSE_MESSAGE, INTERNAL_RESPONSE_CODES


def generate_response(status, message, data=None):
    response_data = {
            "status": RESPONSE_MESSAGE[status],
            "message": message,
            "data": data,
            "status_code": INTERNAL_RESPONSE_CODES[status]
    }
    return response_data