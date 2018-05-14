FROM nginx:latest
ADD nginx.conf /etc/nginx/nginx.conf


# installs the `ps` command in the nginx image
RUN apt-get update && apt-get install -y procps

RUN apt-get install -y git

ADD start.sh /start.sh
ADD nginx-secure.conf /etc/nginx/nginx-secure.conf
ADD dhparams.pem /etc/ssl/private/dhparams.pem

RUN git clone https://github.com/Refugees-Say/questionnaire.git frontend
COPY frontend/public /app

CMD /start.sh

