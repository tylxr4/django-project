import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

password = os.getenv("MONGO_PASSWORD")
client = MongoClient(f"mongodb+srv://chorduser:{password}@cluster0.5bamdfn.mongodb.net/?appName=Cluster0")

db = client['chordcompanion']