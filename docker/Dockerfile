FROM ubuntu:latest

ENV TZ America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
	python3-venv python3-pip libpython3-dev python3-wheel python3-setuptools \
            libblas-dev liblapack-dev gfortran libgmp3-dev libxml2-dev libpng-dev libsodium-dev \
            libssl-dev libcurl4-openssl-dev libpq-dev zlib1g-dev pkg-config \
	bash vim-tiny build-essential git locales \
    nodejs npm

RUN add-apt-repository ppa:ethereum/ethereum -y 

COPY ./requirements.txt /home/
RUN python3 -m pip install -r /home/requirements.txt
RUN python3 -m pip install pipx
RUN python3 -m pipx ensurepath
RUN pipx install git+https://github.com/eth-brownie/brownie.git@feat-hardhat


RUN npm install -g ganache-cli
RUN npm install -g yarn


WORKDIR "/home/project/client"
RUN yarn install


WORKDIR "/home/project"
# command below runs, but trying anything in the container with HH results in this:
# root@43dbe2bb6c96:/home/project# npx hardhat compile
# sh: 1: node-gyp-build: Permission denied
# sh: 1: node-gyp-build: Permission denied
# Error HH12: Trying to use a non-local installation of Hardhat, which is not supported.
# Please install Hardhat locally using npm or Yarn, and try again.
RUN npm install --save-dev hardhat@dtt
# so we might have to just do this inside



