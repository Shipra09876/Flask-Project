from flask import Blueprint, request, jsonify
from app import mongo
from app.models.user_model import User
from bson import ObjectId
from werkzeug.security import generate_password_hash,check_password_hash
user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/users', methods=['POST'])
def create_user():
    """
    Add a new user
    ---
    tags:
      - Users
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: User
          required:
            - name
            - email
            - pwd
          properties:
            name:
              type: string
              example: Shipra
            email:
              type: string
              example: shipra@example.com
            pwd:
              type: string
              example: password123
    responses:
      200:
        description: User added successfully
      400:
        description: Invalid input
    """

    data = request.get_json()

    if not data or not all(k in data for k in ('name', 'email', 'pwd')):
        return jsonify({"error": "Missing fields"}), 400

    hashed_password=generate_password_hash(data['pwd'])
    user = User(data['name'], data['email'], hashed_password)
    inserted_id= mongo.db.users.insert_one(user.to_dict()).inserted_id

    return jsonify({'message': 'User created successfully', 'id': str(inserted_id)}), 201



@user_bp.route('/users', methods=['GET'])
def get_all_users():
    """
    Get all users
    ---
    tags:
      - Users
    responses:
      200:
        description: A list of users
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  _id:
                    type: string
                    example: 64f8d23d5aa1e45e76892abc
                  name:
                    type: string
                    example: Shipra
                  email:
                    type: string
                    example: shipra@example.com
    """
    users = list(mongo.db.users.find())
    for user in users:
        user['_id'] = str(user['_id'])
    return jsonify(users), 200


@user_bp.route('/users/<id>', methods=['GET'])
def get_user(id):
    """
    Get a user by ID
    ---
    tags:
      - Users
    parameters:
      - name: id
        in: path
        type: string
        required: true
        description: The user ID
    responses:
      200:
        description: User found
        content:
          application/json:
            schema:
              type: object
              properties:
                _id:
                  type: string
                  example: 64f8d23d5aa1e45e76892abc
                name:
                  type: string
                  example: Shipra
                email:
                  type: string
                  example: shipra@example.com
      404:
        description: User not found
    """
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404


@user_bp.route('/users/<id>', methods=['PUT'])
def update_user(id):
    """
    Update a user by ID
    ---
    tags:
      - Users
    parameters:
      - name: id
        in: path
        type: string
        required: true
        description: The user ID
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - name
              - email
              - pwd
            properties:
              name:
                type: string
                example: Updated Name
              email:
                type: string
                example: new@example.com
              pwd:
                type: string
                example: newpassword123
    responses:
      200:
        description: User updated successfully
      400:
        description: Invalid input
      404:
        description: User not found
    """
    data = request.get_json()

    if not data or not all(k in data for k in ('name', 'email', 'pwd')):
        return jsonify({'error': 'Missing required fields'}), 400
    
    hashed_password=generate_password_hash(data['pwd'])

    update_result = mongo.db.users.update_one({'_id': ObjectId(id)},   {'$set': {'name': data['name'],
              'email': data['email'],
              'password': hashed_password
            }})
    
    if update_result.matched_count:
        return jsonify({'message': 'User updated successfully'}), 200
    
    return jsonify({'error': 'User not found'}), 404


@user_bp.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    """
    Delete a user by ID
    ---
    tags:
      - Users
    parameters:
      - name: id
        in: path
        type: string
        required: true
        description: The user ID
    responses:
      200:
        description: User deleted successfully
      404:
        description: User not found
    """
    try:
        delete_result = mongo.db.users.delete_one({'_id': ObjectId(id)})
    except:
        return jsonify({'error': 'Invalid ID format'}), 400


    if delete_result.deleted_count:
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'error': 'User not found'}), 404