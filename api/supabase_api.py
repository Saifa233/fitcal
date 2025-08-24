import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

supabase = create_client(
  os.getenv('SUPABASE_PROJECTURL'),
  os.getenv('SUPABASE_APIKEY')
)

print(os.getenv('SUPABASE_PROJECTURL'))
print(os.getenv('SUPABASE_APIKEY'))