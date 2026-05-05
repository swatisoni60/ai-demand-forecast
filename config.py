import os
from dotenv import load_dotenv
load_dotenv('../.env')

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY', 'secret123')
DATABASE = 'database.db'
UPLOAD_FOLDER = 'uploads'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
