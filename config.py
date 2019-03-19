import os


class Config:

    DATABASE_CONFIG = {
        'host': os.environ.get('MONGO_HOST', 'localhost'),
        'port': os.environ.get('MONGO_PORT', 27017)
    }

   