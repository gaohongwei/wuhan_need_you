
FROM ubuntu:18.04

RUN mkdir /root/.pip

COPY sources.list /etc/apt/
COPY pip.conf /root/.pip/

RUN apt-get update && \
		apt install -y openssh-server sudo

RUN systemctl enable ssh

EXPOSE 22
EXPOSE 80
EXPOSE 5000

CMD [ "/sbin/init" ]

