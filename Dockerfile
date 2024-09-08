#* Usando uma imagem base oficial do Python
FROM python:3.9-slim

#* Define o diretório de trabalho no contêiner
WORKDIR /app

#* Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt requirements.txt 

#* Instala as dependências do Python
RUN pip install -r requirements.txt

#* Copia todo o conteúdo da aplicação
COPY . .

#* Expõe a porta que o Flask usa
EXPOSE 8080

#* Comando para rodar a aplicação
CMD ["python3", "app.py"]
