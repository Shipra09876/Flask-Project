# User CRUD System 

This project is a RESTful API built using Flask and MongoDB, providing complete CRUD functionality (Create, Read, Update, Delete) for user management

## Demo


## Installation
```bash
    pip install python  
    pip install bcrypt
    pip install flask
    pip install flask_pymongo
    pip install python-dotenv
    pip install flasgger
```

### Enviornment setup 
```bash
    python3 -m venv venv
```

### Backend project setup 
```bash
    app-> models -> user_models.py
    app-> routes -> user_routes.py
    app-> init.py
    config.py
    Readme.md
    run.py
    .env
```
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

### Database (MongoDB)
```bash
DB_USER=Mongodb
```

### CORS
``` bash
ALLOWED_HOSTS=127.0.0.1:8000
```

## Features

✅ REST API for User CRUD operations

✅ MongoDB integration

✅ Password hashing using werkzeug.security

✅ Swagger UI for API documentation

✅ Environment variable support via .env


## API Reference

#### Add User

```http://127.0.0.1:8000/
  GET api/users
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | **Required**  |
| `email` | `email` | **Required**  |
| `password` | `hashed` | **Required**  |



#### Get all users

```http
  GET /api/users
```

#### Get one user

```http
  GET /api/users/{id}
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | uuid | **Required**. Id of item to fetch |


#### delete user

```http
  DELETE /api/users/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | uuid | **Required**. Id of item to fetch |

#### UPDATE user

```http
  UPDATE /api/users/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`    | `string` | **Required** |
| `email`   | `email` | **Required** |
| `password`| `hashed password` | **Required** |


#### Swagger api 

```http
  http://127.0.0.1:8000/apidocs/
```


## Tech Stack 
- Backend	: Flask, UUID,Flask-PyMongo,Flask-RESTful,Werkzeug python-dotenv
- Database	: MongoDB 
- API Docs	: drf-yasg (Swagger),postman 
- UUIDs	    : For unique Book and Review IDs 



# Hi, I'm Shipra Gupta! 👋


## 🚀 About Me
I'm a full stack developer...


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shipra-guptaa/)


