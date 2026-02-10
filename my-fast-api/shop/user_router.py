from typing import List
from fastapi import APIRouter ,status , HTTPException
from models import UserResponse, UserCreate, UserPatch
from service import UserService , ProductException , UserException
from repository import UserRepository

router = APIRouter(prefix= "/users", tags=["users"])
user_service = UserService(user_repository= UserRepository())

@router.post("/" , response_model= UserResponse , status_code= status.HTTP_201_CREATED)

def create_user(user:UserCreate) -> UserResponse:

    try:
        return user_service.create_user(user)
    except ProductException as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail=str(e))

@router.get("/{user_id}")
def get_user(user_id : int) -> UserResponse:
    try:
        return user_service.get_by_id(user_id)
    except ProductException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=str(e))

@router.get("/")

def all_users(offset : int = 0 , limit : int = 10)->List[UserResponse]:
    return user_service.list_all_use(offset,limit)

@router.delete("/{user_id}")

def delete_user(user_id : int):
    try:
        return user_service.delete_user(user_id)
    except UserException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail= str(e))

@router.put("/{user_id}")

def update_user(user_id : int , user :UserCreate):
    try:
        return user_service.update_user(user_id , user)
    except UserException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@router.patch("/{user_id}")

def patch_user(user_id : int , user : UserPatch):
    try:
        patch_users = user_service.patch_user(user_id , user)
        return {"message" : "user updated successfully", "patched_user" : patch_users}

    except UserException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=str(e))
