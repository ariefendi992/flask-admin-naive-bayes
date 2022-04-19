import os
from dotenv import load_dotenv

load_dotenv()


class Config():
    SECRECT_KEY = str(os.getenv('secret_key'))
