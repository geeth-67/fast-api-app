from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Optional
from models import UserResponse, UserPatch, UserCreate


class UserRepository(ABC):

    @abstractmethod
    def create_user(self, user: UserCreate) -> UserResponse:
        pass

    @abstractmethod
    def update_user(self, user: UserCreate, user_id: int) -> UserResponse:
        pass

    @abstractmethod
    def patch_user(self, user: UserPatch, user_id: int) -> UserResponse:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[UserResponse]:
        pass

    @abstractmethod
    def get_by_username(self, name: str) -> Optional[UserResponse]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[UserResponse]:
        pass

    @abstractmethod
    def delete(self, id: int) -> bool:
        pass


class UserServiceException(Exception):
    pass


class InMemoryUserRepository(UserRepository):

    def __init__(self):
        self.users: Dict[int, UserResponse] = {}
        self.count: int = 0

    def patch_user(self, user: UserPatch, user_id: int) -> UserResponse:

        if user_id not in self.users.keys():
            raise UserServiceException("User ID not found for patching")

        existing_user = self.users[user_id]
        updated_data = user.model_dump(exclude_unset=True)
        updated_user = existing_user.model_copy(update=updated_data)
        # object by updating necessary fields
        self.users[user_id] = updated_user

        return self.users[user_id]

    def create_user(self, user:UserCreate) -> UserResponse:

        user_obj =  UserResponse(
            id=self.count,
            name=user.name,
            age=user.age,
            role=user.role,
            email=user.email,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        self.users[self.count] = user_obj
        self.count += 1
        return user_obj

    def update_user(self, user: UserCreate, user_id: int) -> UserResponse:

        if user_id not in self.users.keys():
            raise UserServiceException("Invalid user id")

        existing_user = self.users[user_id]

        self.users[user_id] = UserResponse(
            id=user_id,
            name=user.name,
            email=user.email,
            age=user.age,
            role=user.role,
            created_at=existing_user.created_at,
            updated_at=datetime.now()
        )

        return self.users[user_id]

    def get_by_id(self, id: int) -> Optional[UserResponse]:
        return self.users.get(id)

    def get_by_username(self, name: str) -> Optional[UserResponse]:
        pass

    def get_by_email(self, email: str) -> Optional[UserResponse]:
        for user in self.users.values():
            if user.email == email:
                return user

        return None

    def delete(self, id: int) -> bool:
        pass
