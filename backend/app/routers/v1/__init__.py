from fastapi import APIRouter
from routers.v1 import user
from routers.v1 import auth


router = APIRouter(prefix='/v1')
router.include_router(auth.router)
router.include_router(user.router)
