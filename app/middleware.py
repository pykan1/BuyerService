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
                function()
            except:
                raise HTTPException(status_code=406, detail={"message": "token invalid"})

        return output
