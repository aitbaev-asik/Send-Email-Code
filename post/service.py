from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Вы подписались на наш сервис уведомлений',
        'aslanbek2004.2019@gamil.com',
        [user_email],
        fail_silently=False
    )
