require("@nomiclabs/hardhat-waffle");
require('@eth-optimism/hardhat-ovm');

module.exports = {
  solidity: "0.7.6",

  networks: {
    optimism: {
      chainId: 69,
      url: 'https://kovan.optimism.io',
      // This sets the gas price to 0 for all transactions on L2. We do this
      // because account balances are not automatically initiated with an ETH
      // balance (yet, sorry!).
      gasPrice: 0,
      ovm: true // This sets the network as using the ovm and ensure contract will be compiled against that.
    }
  }
};