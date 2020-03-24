
FROM readthedocs/build:latest
# https://hub.docker.com/r/readthedocs/build/dockerfile
# texlive, python2, python3, miniconda2, miniconda3

ARG uid=1000
ARG user="app"
ARG home="/home/${user}"

USER root
RUN useradd ${user} -d ${home} -s /usr/bin/bash -u ${uid} -m
RUN apt-get install -y hevea && rm -rf /var/lib/apt/lists/*

USER ${uid}
VOLUME ${home}
CMD ["/bin/bash"]
