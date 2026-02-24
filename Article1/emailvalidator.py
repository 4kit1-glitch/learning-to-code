# this code is a simple email validator

email = "user@example.com"

if('@' in email and '.' in email):
    user_name = email.split('@')[0]
    domain_name = email.split('@')[1]

    print(f"username = {user_name}")
    print(f"domain = {domain_name}")

    #beautiful is better than ugly