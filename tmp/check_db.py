import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spabusmgt.settings')
django.setup()
from django.db import connection
c = connection.cursor()
c.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
print("Tables:", [r[0] for r in c.fetchall()])
c.execute("SELECT COUNT(*) FROM django_migrations")
print("Migrations:", c.fetchone()[0])
