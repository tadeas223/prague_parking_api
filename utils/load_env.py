from dotenv import load_dotenv
import os

load_dotenv()

def load_env(name):
    return os.getenv(name)