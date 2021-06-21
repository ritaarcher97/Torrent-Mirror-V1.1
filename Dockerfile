FROM junedkh/torrentmirror:latest

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

RUN curl https://github.com/P3TERX/aria2.conf/raw/master/dht.dat -o /usr/src/app/dht.dat && \
    curl https://github.com/P3TERX/aria2.conf/raw/master/dht6.dat -o /usr/src/app/dht6.dat

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY extract /usr/local/bin
COPY pextract /usr/local/bin
RUN chmod +x /usr/local/bin/extract && chmod +x /usr/local/bin/pextract
COPY . .
COPY netrc /root/.netrc
COPY netrc .netrc
RUN chmod 600 /usr/src/app/.netrc
RUN chmod +x aria.sh

CMD ["bash","start.sh"]
