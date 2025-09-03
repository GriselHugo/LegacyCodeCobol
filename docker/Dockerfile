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

COPY ./python/requirements.txt /app/python/requirements.txt
RUN if [ -f /app/python/requirements.txt ]; then \
        python3 -m pip install --upgrade pip && \
        python3 -m pip install --no-cache-dir -r /app/python/requirements.txt; \
    fi

CMD ["/bin/bash"]
