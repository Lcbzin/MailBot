import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# Configuração do servidor de e-mail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = "lorenzobarcellos@gmail.com"
PASSWORD = "qzex tifl lpqc tnmk"

# Função para enviar e-mail
def enviar_email(destinatario, assunto, mensagem, anexo):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Adicionar o corpo do e-mail
    msg.attach(MIMEText(mensagem, 'plain'))

    # Anexar o arquivo
    with open(anexo, "rb") as file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={anexo}')
        msg.attach(part)

    # Conectar e enviar o e-mail
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

# Caminho do arquivo Excel
arquivo_excel = "base_dados.xlsx"

# Destinatários
destinatarios = {
    "minergamingbr@gmail.com": "Relatório diário.",
}

# Enviar e-mails
for destinatario, assunto in destinatarios.items():
    mensagem = f"Bom dia, segue o relatório atualizado.\n\nAtenciosamente,\nLorenzo Barcellos"
    enviar_email(destinatario, assunto, mensagem, arquivo_excel)

print("E-mails enviados com sucesso!")
