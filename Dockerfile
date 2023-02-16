FROM --platform=arm64 continuumio/miniconda3

WORKDIR /usr/src/app

COPY app/ .

RUN conda update --name base conda && \
    conda env create --file environments.yaml

SHELL ["conda", "run", "--name", "house-pricing", "/bin/bash", "-c"]

ENTRYPOINT ["conda", "run", "--name", "house-pricing", "python", "main.py", "250"]