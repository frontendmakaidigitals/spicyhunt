from flask import Flask, request
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'frontendmakaidigitals@gmail.com'
app.config['MAIL_PASSWORD'] = 'tcat lhbh manu bmkw'  # Use Gmail App Password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/', methods=['POST'])
def reserve():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        date = request.form.get('date')
        time = request.form.get('time')
        person = request.form.get('person')

        # --- Professional Restaurant Email ---
        subject = f"🍽️ New Table Reservation - {name}"
        body = f"""
You have received a new table reservation from your restaurant website.

----------------------------------------
👤 Name: {name}
📧 Email: {email}
📞 Phone: {phone}
📅 Date: {date}
⏰ Time: {time}
👥 Guests: {person}
----------------------------------------

This message was sent automatically via your restaurant's website.
        """

        msg = Message(
            subject=subject,
            sender=("Restaurant Website", app.config['MAIL_USERNAME']),
            recipients=["faheemk793@gmail.com"],  # your inbox
            body=body
        )

        mail.send(msg)
        return "success"

    except Exception as e:
        print("❌ Email send error:", e)
        return "error"

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
