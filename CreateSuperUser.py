import subprocess

try:
    subprocess.check_call(
        'echo "from django.contrib.auth import get_user_model; '
        'User = get_user_model(); '
        'User.objects.create_superuser(email=\'kismassolomon@gmail.com\', password=\'solo123SOLO\')" | '
        'python manage.py shell',
        shell=True
    )
    print("Superuser created successfully")
except subprocess.CalledProcessError as e:
    print(f"Error creating superuser: {e}")
