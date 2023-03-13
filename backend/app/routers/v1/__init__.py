from fastapi import APIRouter
from routers.v1 import user


router = APIRouter(prefix='/v1')
router.include_router(user.router)