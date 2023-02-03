# Interview Setup

1. Make Migrations
```
python manage.py makemigrations authentication music_library
```
2. Migrate
```
python manage.py migrate
```
3. Create Superuser
```
python manage.py createsuperuser
```
```
Username: admin
Email address: admin@tourus.io
Password: admin
Password (again): admin
Bypass password validation and create user anyway? [y/N]: y
```

4. Test Run the server
- Login to admin
- Test api view

5. Import data
```
 python manage.py import_data
 ```

6. Confirm import & Logout
On the admin confirm import and logout

7. Break the app
In music_library/admin.py remove the Track import
