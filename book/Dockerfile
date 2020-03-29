
FROM readthedocs/build:latest
# https://hub.docker.com/r/readthedocs/build/dockerfile
# texlive, python2, python3, miniconda2, miniconda3

ARG uid=1000
ARG user="app"
ARG home="/home/${user}"

USER root
RUN useradd ${user} -d ${home} -s /usr/bin/bash -u ${uid} -m
RUN apt-get install -y hevea && rm -rf /var/lib/apt/lists/*

ARG heveaversion=""
# ARG heveaversion="master"
# ARG heveaversion="v2.34"

#  sed -i 's/^# deb-src/deb-src/g' /etc/apt/sources.list
#  apt-get update; apt-get build-dep -y hevea

# apt-get install -y wget make ocaml-nox ocamlbuild
RUN if test -n "$heveaversion"; then \
    apt-get update && \
    apt-get install -y wget make ocaml-nox ocamlbuild && \
    rm -rf /var/lib/apt/lists/* && \
    \
    mkdir -p /usr/local/src/hevea && \
    cd /usr/local/src && \
    wget "https://github.com/maranget/hevea/archive/$heveaversion.tar.gz" && \
    tar xzvf "${heveaversion}.tar.gz" && \
    cd "/usr/local/src/hevea-${heveaversion}" && \
    make all install \
    ; \
    fi


USER ${uid}
VOLUME ${home}
CMD ["/bin/bash"]
