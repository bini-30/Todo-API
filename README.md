# Todo API

A **simple Todo API** built with **Django REST Framework (DRF)**, supporting **JWT authentication, CRUD operations, pagination, filtering, and search**.

---

## Features

- **User Management**
  - Signup with username, email, password, first & last name
  - JWT authentication (Access & Refresh tokens)
- **Todo Management**
  - Create, list, update, retrieve, and delete todos
  - Each user can only manage their own todos
  - Fields: `title`, `description`, `completed`, `owner`, `created_at`, `updated_at`
- **Filtering & Searching**
  - Filter todos by `completed` status
  - Search todos by `title` or `description`
  - Order by `created_at` or `updated_at`
- **Pagination**
  - Default page size: 5 todos per page
  - Adjustable with query parameter `page_size`

---

## Tech Stack

- Python 3.13.5  
- Django 5.2.5  
- Django REST Framework  
- Django REST Framework Simple JWT  
- django-filter  

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/bini-30/Todo-API.git
cd Todo-API
```
# API Endpoints
- User

| Endpoint          | Method | Description                        | Body                                                                       |
| ----------------- | ------ | ---------------------------------- | -------------------------------------------------------------------------- |
| `/signup/`        | POST   | Register a new user                | `json {"username":"bini","email":"bini@example.com","password":"123456"} ` |
| `/login/`         | POST   | Obtain JWT access & refresh tokens | `json {"username":"bini","password":"123456"} `                            |
| `/token/refresh/` | POST   | Refresh access token               | `json {"refresh":"<refresh_token>"} `                                      |

- Todo

| Endpoint       | Method | Description                  | Body                                                                                           |
| -------------- | ------ | ---------------------------- | ---------------------------------------------------------------------------------------------- |
| `/todos/`      | GET    | List todos of logged-in user | Optional query params: `?page=1&page_size=5&completed=true&search=django&ordering=-created_at` |
| `/todos/`      | POST   | Create a new todo            | `json {"title":"Learn Django","description":"DRF CRUD operations","completed":false} `         |
| `/todos/<id>/` | GET    | Retrieve a todo by ID        | N/A                                                                                            |
| `/todos/<id>/` | PUT    | Update a todo fully          | Include all fields in body                                                                     |
| `/todos/<id>/` | PATCH  | Update a todo partially      | Include only fields you want to update                                                         |
| `/todos/<id>/` | DELETE | Delete a todo                | N/A                                                                                            |


## Project Structure

- Todo-API/
  - backend/
    - api/        # API app (views, serializers, permissions)
    - todo/       # Todo app (models)
    - user/       # User app (models)
    - backend/    # Django project settings
    - manage.py

## Notes

- Only authenticated users can access Todo endpoints
- Users can only manage their own todos (IsOwner permission)
- Passwords are hashed automatically via UserCreateSerializer
- Access tokens expire in 5 minutes (configurable in settings.py)
- Refresh tokens can be used to get new access tokens
