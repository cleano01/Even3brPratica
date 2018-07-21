from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from gerador.models import Certificado
from gerador.forms import CertificadoForm

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 


import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from email.MIMEBase i

from email.mime.base import MIMEBase
from email import encoders



# Create your views here.

def index(request):
    if(request.method == 'POST'):
        
        form= CertificadoForm(request.POST, request.FILES)

        print(form)
        if (form.is_valid()):
            
            form.save()
            context={'form':form}
            
            texto1 = "Certifico que {nome} participou do I Congresso Norte".format(nome="Cleano Ferreira")
            texto2 = "Americano de Letras na cidade de Recife, no perído de 10/04/2018 a"
            texto3 = "12/04/2018 totalizando uma carga horária de 20 horas"
            

            img = Image.open("media/certificado_base.jpeg") 
            draw = ImageDraw.Draw(img)
            # font = ImageFont.truetype(<font-file>, <font-size>)
            font = ImageFont.truetype("fonts/Oswald-Light.ttf", 40)
            # draw.text((x, y),"Sample Text",(r,g,b))
            draw.text((150, 350),texto1,(0,0,0),font=font)
            draw.text((150, 410),texto2,(0,0,0),font=font)
            draw.text((150, 470),texto3,(0,0,0),font=font)
            img.save('sample-out.pdf')

            return render(request, 'gerador/index.html',context)

    form= CertificadoForm()
    context={'form':form} 
    return render(request, 'gerador/index.html',context)    


def email(request):
    if(request.method == 'POST'):

             
        email= request.POST['email']
        print(email)
        print("FOI POST ")

        print("Enviar Email")

        fromaddr = 'cleano.ferreira@dce.ufpb.br'
        toaddr = email

#############################################

        msg = MIMEMultipart()

        msg['From']= fromaddr
        msg['To']= toaddr
        msg['Subject']= 'Certificado Gerado'


        body= 'Mensagem Enviada Python, body'
        msg.attach(MIMEText(body))

        filename='sample-out.pdf' #aqui bota o nome do arquivo
        attachment=open(filename, 'rb')

        mimetypes.guess_type(filename)
        mimetype_anexp= mimetypes.guess_type(filename)[0].split('/')
        part= MIMEBase(mimetype_anexp[0], mimetype_anexp[1])


        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" %filename)

        msg.attach(part)

#############################################
        server= smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, open('senha.txt').read().strip())
        #server.login(fromaddr, "PODE INFORMAR SUA SENHA AQUI NA STRING!!")
        text= msg.as_string()
        #print(text)
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        
       

        return render(request, 'gerador/index.html')
    print('NÃO FOI POST NO EMAIL')
    return render(request, 'gerador/index.html')