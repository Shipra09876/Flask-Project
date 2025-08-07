from dotenv import load_dotenv
load_dotenv()
import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/user_db")
    SWAGGER = {
        'title':  os.getenv('SWAGGER_TITLE'),
        'uiversion': int(os.getenv('SWAGGER_VERSION'))
    }