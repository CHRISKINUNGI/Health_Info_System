from supabase import create_client, Client
import os
from dotenv import load_dotenv
import logging

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_ANON_KEY = os.environ.get("SUPABASE_ANON_KEY")

if not SUPABASE_URL:
    raise ValueError("SUPABASE_URL environment variable must be set.")
if not SUPABASE_ANON_KEY:
    raise ValueError("SUPABASE_ANON_KEY environment variable must be set.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

def get_supabase_client():
    return supabase

def check_database_connection():
    try:
        # Simple query to check the connection (it could also be any simple query)
        response = supabase.from_("programs").select("id").limit(1).execute()
        
        if response.error:
            logging.error(f"Database connection failed: {response.error}")
            return False
        else:
            logging.info("Database connection successful.")
            return True
    except Exception as e:
        logging.error(f"Database connection error: {e}")
        return False
