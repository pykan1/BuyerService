from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT

from repository import Repository
from service import Service

buyer_service =APIRouter