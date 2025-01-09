from config import settings
import database
import json
from models import Client
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_first_emails():
    db_session = next(database.get_db())
    clients = db_session.query(Client).all()
    for client in clients:
        send_email(client.email, client.name)
        client.sended_emails += 1
        db_session.commit()

def send_email(email_address, client_name):
    try:
        # Set up the email message
        sender_email = settings.EMAIL_SENDER
        sender_password = settings.EMAIL_PASSWORD
        subject = "Opportunità di Collaborazione con TuscanyAI"
        body = f"""
Gentile {client_name},

Mi chiamo Oleksandr Nazarevych e sono il fondatore di TuscanyAI. Vorrei proporvi un’opportunità unica: uno sviluppo gratuito del nostro chatbot AI e un mese di prova senza alcun impegno.

Il nostro chatbot è pensato per aiutare barbershop come il vostro a gestire le prenotazioni e migliorare il servizio clienti. Ecco cosa può fare per voi:

- Prenotazioni su WhatsApp: I vostri clienti possono prenotare, modificare o cancellare appuntamenti in pochi secondi.
- Risposte automatiche 24/7: Gestisce le richieste telefoniche e appuntamenti senza bisogno di personale aggiuntivo.
- Supporto multilingue: Perfetto per attirare clienti locali e internazionali.
- Migliorare l’esperienza clienti: Un sistema veloce e semplice per aumentare la soddisfazione e la fedeltà dei vostri clienti.

Sappiamo che molti barbershop usano sistemi tradizionali, ma il nostro chatbot si integra perfettamente o li supera, rendendo tutto più facile per voi e per i vostri clienti.

Vi piacerebbe vedere come funziona? Posso organizzare una breve demo o una chiamata per spiegarvi tutti i vantaggi.

Resto in attesa di una vostra risposta!

Cordiali saluti,  
Oleksandr Nazarevych  
Fondatore, TuscanyAI  
📞 +39 340 371 4830  
"""


        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email_address
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to Gmail's SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the Gmail account
            server.send_message(msg)  # Send the email

        logger.info(f"Email successfully sent to {email_address}")

    except Exception as e:
        logger.info(f"Failed to send email to {email_address}. Error: {e}")

def fill_database():
    with open('clients.json', 'r') as f:
        clients = json.load(f)

    db_session = next(database.get_db())
    for client in clients:
        if not db_session.query(Client).filter(Client.email == client['email']).first():
            db_session.add(Client(name=client['name'], email=client['email']))
    db_session.commit()

if __name__ == '__main__':
    fill_database()
    send_first_emails()