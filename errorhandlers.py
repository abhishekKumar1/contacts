def error404():
    return {"RestException": {"Status": 404, "Message": "Resource Not Found"}}

def error401():
    return {"RestException": {"Status": 401, "Message": "Not Authenticated"}}

def error400():
    return {"RestException": {"Status": 400, "Message": "Invalid Request"}}

def error500():
    return {"RestException": {"Status": 500, "Message": "Internal Server Error"}}