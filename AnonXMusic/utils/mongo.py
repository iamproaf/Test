                                
"""
✩░▒▓▆▅▃▂▁𝐍𝐚𝐢𝐧𝐚▁▂▃▅▆▓▒░✩
"""






from typing import Dict, Union

from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

from config import MONGO_DB_URI

mongo = MongoCli(MONGO_DB_URI)
db = mongo.AnonXMusic

afkdb = db.afk

notesdb = db.notes

filtersdb = db.filters
