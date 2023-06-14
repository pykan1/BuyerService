import jwt
from fastapi import HTTPException

from container import Container


class Middleware:
    @staticmethod
    def valid_token(function):
        def output(*args):
            try:
                jwt.decode(
                    jwt=args[1],
                    key=Container().auth["secret_key"],
                    algorithms=["HS256"]
                )
                return function(args[0], args[1])
            except:
                raise HTTPException(status_code=406, detail="token invalid")

        return output
