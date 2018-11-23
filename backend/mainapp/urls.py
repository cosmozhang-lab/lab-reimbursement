from .views.auth import apis as login_apis

urls = []

for item in login_apis:
    urls.append(("api/auth/" + item[0], item[1]))
