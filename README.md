# ELMO -- Brownie version

ELMO: **E**xchange **L**ayer2 **M**oney **O**ptimistically

ELMO is Venmo but on Ethereum Layer 2. The dev goal of this project was to get experience building a dapp, so the use case was kept simple. The dapp goal is to onboard people to crypto in a cheap, seamless way.  

This repo runs a docker container with brownie and react. Currently, it installs a specific PR of brownie (`feat-hardhat`) for operability with the [Optimism Virtual Machine](https://github.com/ethereum-optimism/optimism-tutorial) to build dapps on Layer 2. Ensure you have `docker` installed before going further.

## Getting Started

Clone the repo and complete the configuration steps below
```
git clone https://github.com/vintrocode/elmo-brownie.git
```

Now create a `.env` file and paste the code chunk below, substituting in your values.  **NOTE: MAKE SURE THE `.env` FILE IS IN YOUR `.gitignore`, DON'T PUSH YOUR KEYS TO GITHUB AND GET REKT**

```
METAMASK_PUBLIC_ADDRESS={your address here}
METAMASK_SECRET_KEY={your secret here}
PROVIDER_MAINNET={your mainnet url here}
PROVIDER_KOVAN={your kovan url here}
WEB3_INFURA_PROJECT_ID={your infura project id here}
ETHERSCAN_TOKEN={your etherscan API token here}
```

Now you're ready to build and run the container! This may take a few minutes but it's a one time cost.
```
docker-compose up -d --build
```


Port 3000 will be exposed to run the react example. Now you can attach VSCode or `docker exec` into the container and get to work!
```
# Access a shell within the container
$ docker exec -it elmo-brownie_eth-brownie_1 /bin/bash
```

## Running the Frontend (WIP)

If the contracts have already been deployed, you can spin up the frontend.
```
cd client
yarn start
```

## Next Steps

To continue with the example, click on the `elmo/` folder and follow the readme there.
