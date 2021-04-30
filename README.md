# Brownie Docker Template

This repo allows anyone to get up and running developing dapps in a docker container. Spin up the docker container, clone your favorite brownie mix, and get going

### Getting Started

TODO: create .env
```
METAMASK_PUBLIC_ADDRESS={your address here}
METAMASK_SECRET_KEY={your secret here}
PROVIDER_MAINNET={your mainnet url here}
PROVIDER_KOVAN={your kovan url here}
```

TODO: brownie bake something

TODO: edit docker-compose.yaml with brownie folder
```
    volumes:
      - ./{your folder here}:/home/project
```


Ensure you have docker installed locally and run the following commands:
```
git clone https://github.com/vintrocode/eth-brownie-docker-template.git
cd eth-brownie-docker-template
docker-compose up -d --build
```

Once that's finished you should have a docker container running in the background. Either docker exec into it or use vscode to connect.