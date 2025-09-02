FROM fedora:latest

RUN dnf -y update && \
    dnf -y install \
        git \
        make \
        gcc \
        gnucobol \
        python3 \
        python3-pip \
        python3-devel \
        vim \
        less \
        && dnf clean all

WORKDIR /app

CMD ["/bin/bash"]
