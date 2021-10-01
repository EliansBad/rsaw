class RsawError(Exception):
    pass

class InvalidKeyError(RsawError):
    pass

class ParamError(RsawError):
    pass