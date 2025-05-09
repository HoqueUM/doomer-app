from flask import Flask
import os
import dotenv
from api.supabase_interface import SupabaseInterface

dotenv.load_dotenv()

supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
table = "Current News"


supabase = SupabaseInterface(supabase_url, supabase_key, table)

app = Flask(__name__)



@app.route("/api/get_news")
def hello_world():
    return supabase.get_news()

if __name__ == "__main__":
    app.run(port=5328)