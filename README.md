# Reproduction of jazzband/django-auditlog/issues/685

1. Clone this repo (database included)
2. `pipenv install` (or use `requirements.txt` as desired)
3. Run django server: `pipenv run python manange.py runserver`
4. Navigate to http://127.0.0.1:8001/admin/
5. Log in with credentials `admin`/`admin`
6. Navigate to http://127.0.0.1:8001/admin/things/food/add/
7. Add a food with a name and tag
8. Navigate to http://127.0.0.1:8001/admin/auditlog/logentry/
9. Note the `update` audit log assoictaed with the added Food is duplicated.

<img width="1076" alt="image" src="https://github.com/user-attachments/assets/4fdfef31-9d8e-45d9-a2c6-71b795a89b60">
