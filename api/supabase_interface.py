import os
from supabase import create_client


def has_only_ascii(text):
    try:
        text.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False

class SupabaseInterface:
    def __init__(self, url, key, table):
        self.supabase = create_client(url, key)
        self.table = table

    def insert_news(self, article):
        """Insert article into the table."""
        try:
            self.supabase.table(self.table).insert(article).execute()
        except Exception as e:
            if "duplicate key value violates unique constraint" in str(e):
                pass
            else:
                raise
    
    def upsert_news(self, article):
        """Upsert article into the table."""
        self.supabase.table(self.table).upsert(article, on_conflict=["title"]).execute()    
    def get_news(self):
        """Get all news currently in the table."""
        response = self.supabase.table(self.table).select("*").order("created_at", desc=True).execute()

        data = response.data
        response = [data for data in data if has_only_ascii(data["title"])]
        return response
    
    def delete_news(self, title):
        """Delete news with the specified title."""
        self.supabase.table(self.table).delete().eq("title", title).execute()