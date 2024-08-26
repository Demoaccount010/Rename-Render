# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("27829715", "")

API_HASH = os.environ.get("72e38250de2b0ae7dd9eb467ffa35c17", "")

BOT_TOKEN = os.environ.get("7495132028:AAHMrEA4l3BGSLpiMSqoC4UDxp9UsSmeNsI", "") 

FORCE_SUB = os.environ.get("Hindi_Animes_Series", "VJ_Botz") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("yoursmileyt01", "renamevjbot")     

DB_URL = os.environ.get("mongodb+srv://yoursmileyt01:fARox9L4aKD4b9d0@surya.9vtxs.mongodb.net/?retryWrites=true&w=majority&appName=Surya", "")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('1906280172', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
