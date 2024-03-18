import os
from dotenv import load_dotenv

load_dotenv("../.env")

def env(name): return os.environ.get(name)
