import jwt
from fastapi import HTTPException

from container import Container


class Middleware:
    @staticmethod
    def valid_token(function):
        print("ДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДДД")

        def output(*args):
            try:
                print("ЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖЖ")
                jwt.decode(
                    jwt=args[1],
                    key=Container().auth["secret_key"],
                    algorithms=["HS256"]
                )
                print("МММММММММММММММММММММММММММММММММММММММММММММММММММММММММММММММММММММ")
                return function(*args)
            except:
                raise HTTPException(status_code=406, detail="token invalid")

        return output
