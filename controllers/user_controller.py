from flask import Blueprint, request, jsonify
from factory import api, db
from sqlalchemy import or_
from spectree import Response
from schemas.user_schema import UserCreate, UserListResponse, SearchUser, UserResponse
from schemas.default_schema import DefaultResponse, DefaultCreateResponse
from models import User


user_controller = Blueprint("user_controller", __name__, url_prefix="/user")


@user_controller.get("/<int:user_id>")
@api.validate(
    resp=Response(HTTP_200=DefaultResponse, HTTP_404=DefaultResponse), tags=["users"]
)
def get_user(user_id: int):
    """
    Get a specified user
    """

    user = User.query.filter_by(id=user_id).first()

    if not user:
        return {"msg": "User not found"}, 404

    return user


@user_controller.post("/")
@api.validate(
    json=UserCreate,
    resp=Response(HTTP_201=DefaultCreateResponse, HTTP_409=DefaultResponse),
    tags=["users"],
)
def create_user():
    """
    Creates a new user
    """

    data = request.json

    user = User.query.filter(
        or_(User.email == data.get("email"), User.username == data.get("username"))
    ).first()

    if user:
        return {"msg": "Email or username in use"}, 409

    user = User(
        username=data.get("username"),
        description=data.get("description"),
        email=data.get("email"),
    )

    db.session.add(user)
    db.session.commit()

    return {
        "msg": "User created",
        "id": user.id,
    }, 201


@user_controller.put("/<int:user_id>")
@api.validate(
    resp=Response(HTTP_200=DefaultResponse, HTTP_404=DefaultResponse),
    tags=["users"],
)
def put_user(user_id):
    """
    Modify a specified user
    """

    user = User.query.filter_by(id=user_id).first()

    if user is None:
        return {"msg": f"There is no user with id {user_id}"}, 404

    data = request.json

    # TODO: validate if username and email already exists if modified

    user.username = data["username"]
    user.email = data["email"]
    user.description = data.get("description")

    db.session.commit()

    return {"msg": "User was updated."}, 200


@user_controller.delete("/<int:user_id>")
@api.validate(
    resp=Response(HTTP_200=DefaultResponse, HTTP_404=DefaultResponse),
    tags=["users"],
)
def delete_user(user_id):
    """
    Delete a specified user
    """

    user = User.query.filter_by(id=user_id).first()

    if user is None:
        return {"msg": f"There is no user with id {user_id}"}, 404

    db.session.delete(user)
    db.session.commit()

    return {"msg": "User deleted from the database."}, 200
