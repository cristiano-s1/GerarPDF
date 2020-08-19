import io
from django.http import FileResponse
from django.views.generic import View
from reportlab.pdfgen import canvas


class IndexView(View):

    def get(self, request, *args, **kwargs):

        # Cria um arquivo para receber os dados e gerar o PDF
        buffer = io.BytesIO()

        # Criar o arquivo pdf
        pdf = canvas.Canvas(buffer)

        # Insere 'coisas' no PDF
        pdf.drawString(50, 500, "PROGRAMAÇÃO WEB COM PYTHON E FRAMEWORK DJANGO")

        # Quando acabamos de inserir coisas no PDF
        pdf.showPage()
        pdf.save()

        # Por fim, retornamos o buffer para o início do arquivo
        buffer.seek(0)

        # Faz o download do arquivo em PDF gerado
        # return FileResponse(buffer, as_attachment=True, filename='relatorio1.pdf')

        # Abre o PDF direto no navegador
        return FileResponse(buffer, filename='relatorio1.pdf')

