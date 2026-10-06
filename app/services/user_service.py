users = []


def create_user(user):
    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email,
    }

    users.append(new_user)

    return new_user


def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    return None