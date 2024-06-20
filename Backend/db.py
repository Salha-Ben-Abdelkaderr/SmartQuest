from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("mongodb+srv://salhabenabdelkader:salha2024@maincluster.chamw6t.mongodb.net/SmartQuest_db?retryWrites=true&w=majority&appName=mainCluster")
client = AsyncIOMotorClient(MONGODB_URL)

def get_database():
    return client.get_database("SmartQuest_db")
