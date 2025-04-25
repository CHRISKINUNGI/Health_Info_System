import os
from dotenv import load_dotenv
from supabase import create_client, Client


load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


def get_supabase_client() -> Client:
    """
    Establishes and returns a Supabase client.

    Returns:
        Client: A Supabase client instance.
    Raises:
        ValueError: If SUPABASE_URL or SUPABASE_KEY are not set.
    """
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("Supabase URL and Key must be set in .env file")
    return create_client(SUPABASE_URL, SUPABASE_KEY)


supabase: Client = get_supabase_client()