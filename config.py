import os
from dotenv import load_dotenv
load_dotenv()



class Config:
    
    # SECRET_KEY = 'mongodb+srv://mongo_xema:Iv7m9uQdjlg3yoTn@jsearchdb.m9rzgkr.mongodb.net/jsearchweb'
    SECRET_KEY = os.getenv('SECRET_KEY')
    MONGO_URI = os.getenv('MONGO_URI')