from django.core.management.base import BaseCommand
from forms_app.models import Formularze, Szablony

class Command(BaseCommand):
    help = 'Populate initial data into the database'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Formularze.objects.all().delete()
        Szablony.objects.all().delete()

        # Insert Formularze data
        formularze_data = [
            ('form1', 'imie', 'Jan', 0),
            ('form1', 'nazwisko', 'Kowalski', 1),
            ('form1', 'email', 'jan.kowalski@example.com', 2),
            ('form2', 'email', 'maria.nowak@example.com', 0),
            ('form2', 'telefon', '987654321', 1),
            ('form2', 'miasto', 'Gdańsk', 2),
            ('form3', 'imie', 'Tomasz', 0),
            ('form3', 'wiek', '35', 1),
            ('form3', 'adres', 'ul. Zielona 8, Poznań', 2),
        ]
        for form_name, attr_name, attr_value, position in formularze_data:
            Formularze.objects.create(
                form_name=form_name,
                attr_name=attr_name,
                attr_value=attr_value,
                position=position
            )

        # Insert Szablony data
        szablony_data = [
            ('template1', 'Cześć {imie} {nazwisko}, twój email to {email}.'),
            ('template2', 'Witaj! Twój numer telefonu to {telefon}, a miasto: {miasto}.'),
            ('template3', 'Szanowny Panie/Pani {imie}, zapraszamy na spotkanie pod adresem: {adres}.'),
        ]
        for template_name, template_text in szablony_data:
            Szablony.objects.create(
                template_name=template_name,
                template_text=template_text
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated data'))