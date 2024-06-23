from pymongo import MongoClient

client = MongoClient('mongodb+srv://salhabenabdelkader:salha2024@maincluster.chamw6t.mongodb.net/SmartQuest_db?retryWrites=true&w=majority&appName=mainCluster')
db = client.SmartQuest_db
