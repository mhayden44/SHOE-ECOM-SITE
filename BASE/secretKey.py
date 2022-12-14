# Generates a Django SECRET_KEY
# The output should be copy and pasted into a file within SHOE ECOM SITE/BASE called .env
import secrets

length = 50
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

secret_key = ''.join(secrets.choice(chars) for i in range(length))

print('SECRET_KEY =','"'+secret_key+'"')