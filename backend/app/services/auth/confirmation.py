import aiofiles
from jinja2 import Template

import smtplib
from email.mime.text import MIMEText

import schemas
from settings import settings, path


async def _get_template(endpoint_key: str, user: schemas.UserWithID) -> Template:

    async with aiofiles.open(path('templates', 'confirmation', 'index.html'), mode='r', encoding='utf-8') as file:
        template_message = Template(await file.read())

    data = {
        'login': user.login,
        'confirmation_url': settings.client_origin + endpoint_key,
        'site': settings.client_origin,
    }

    return template_message.render(data)


async def send_email(to: str, endpoint_key: str, user: schemas.UserWithID) -> None:
    
    rendered_template = await _get_template(endpoint_key, user)

    message = MIMEText(rendered_template, 'html')
    message['Subject'] = 'Email Confirmation'
    message['From'] = settings.email_sender
    message['To'] = to

    with smtplib.SMTP('smtp.gmail.com', 587) as server:

        server.starttls()
        server.login(user=settings.email_sender, password=settings.email_password)
        server.sendmail(from_addr=settings.email_sender, to_addrs=to, msg=message.as_string())
