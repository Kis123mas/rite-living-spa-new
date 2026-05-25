import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spabusmgt.settings')
django.setup()
from django.db import connection
c = connection.cursor()

tables = [
    'firstApp_customuser', 'firstApp_expense', 'firstApp_product',
    'firstApp_order', 'firstApp_message', 'firstApp_review',
    'firstApp_spasessionbooking', 'firstApp_contactmessage',
    'firstApp_servicerendered', 'firstApp_uniform', 'firstApp_userprofile',
    'auth_user', 'auth_permission', 'auth_group',
    'django_content_type', 'django_session', 'account_emailaddress',
    'socialaccount_socialaccount',
]

for t in tables:
    try:
        c.execute(f'SELECT COUNT(*) FROM "{t}"')
        print(f"{t}: {c.fetchone()[0]}")
    except Exception as e:
        print(f"{t}: ERROR - {e}")
