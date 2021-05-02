# Brownie React Mix

This mix comes with everything you need to start using [React](https://reactjs.org/) with a Brownie project.

## Usage

1. Add Optimism to the networks list in `brownie`.

    ```
    $ brownie networks add Ethereum optimism-kovan host=https://kovan.optimism.io chainid=69
    Brownie v1.14.4 - Python development framework for Ethereum

    SUCCESS: A new network 'optimism-kovan' has been added
    └─optimism-kovan
        ├─id: optimism-kovan
        ├─chainid: 69
        └─host: https://kovan.optimism.io
    ```

    *The contracts have been compiled and the L1 ERC token is deployed on Kovan at `0x620696fb88Afcc8B467636756cD6F232bC8c0f57`*

2. Open the Brownie console. Starting the console connects to Optimism's Kovan testnet.

    ```bash
    $ brownie console --network optimism-kovan
    Brownie v1.14.4 - Python development framework for Ethereum

    Project is the active project.
    Brownie environment is ready.
    ```

3. Run the [brownie deployment script](scripts/deploy_brownie.py) (WIP) to deploy the project's smart contracts to Optimistic Kovan.

    ```python
    >>> run('deploy_brownie')
    Running 'scripts/deploy_brownie.py::main'...
    optimism-kovan
    File "<console>", line 1, in <module>
    File "brownie/project/scripts.py", line 69, in run
        return func(*args, **kwargs)
    File "./scripts/deploy_brownie.py", line 11, in main
        ERC20.deploy(1337, 'ELMO', {'from': accounts.default})
    File "brownie/network/contract.py", line 593, in __call__
        return tx["from"].deploy(
    File "brownie/network/account.py", line 463, in deploy
        exc = VirtualMachineError(e)
    File "brownie/exceptions.py", line 85, in __init__
        raise ValueError(exc["message"]) from None
    ValueError: Cannot submit unprotected transaction
    ```

<!-- 5. While Brownie is still running, start the React app in a different terminal.

    ```bash
    # make sure to use a different terminal, not the brownie console
    cd client
    yarn start
    ```

4. Connect Metamask to the Kovan test network. In the upper right corner, click the network dropdown menu. Select `Kovan Test Network`.

5. Interact with the smart contracts using the web interface or via the Brownie console.

    ```python
    # get the newest vyper storage contract
    >>> vyper_storage = VyperStorage[-1]

    # the default sender of the transaction is the contract creator
    >>> vyper_storage.set(1337)
    ```

    Any changes to the contracts from the console should show on the website after a refresh, and vice versa.

## Ending a Session

When you close the Brownie console, the Ganache instance also terminates and the deployment artifacts are deleted.

To retain your deployment artifacts (and their functionality) you can launch Ganache yourself prior to launching Brownie. Brownie automatically attaches to the ganache instance where you can deploy the contracts. After closing Brownie, the chain and deployment artifacts will persist.

## Further Possibilities

### Testing

To run the test suite:

```bash
brownie test
```

### Deploying to a Live Network

To deploy your contracts to the mainnet or one of the test nets, first modify [`scripts/deploy.py`](`scripts/deploy.py`) to [use a funded account](https://eth-brownie.readthedocs.io/en/stable/account-management.html).

Then:

```bash
brownie run deploy --network kovan
```

Replace `kovan` with the name of the network you wish you use. You may also wish to adjust Brownie's [network settings](https://eth-brownie.readthedocs.io/en/stable/network-management.html).

For contracts deployed on a live network, the deployment information is stored permanently unless you:

* Delete or rename the contract file or
* Manually remove the `client/src/artifacts/` directory

## Resources

This mix provides a bare-bones implementation of [Create React App](https://create-react-app.dev/), configured to work with Brownie.

To get started with React and building a front-end for your dApps:

* [Rimble](https://rimble.consensys.design/) is an open-source library of React components and guides to help you make dApps. Along with components they provide guides and tutorials to help you get started.
* For more in-depth information, read the [Create React App documentation](https://create-react-app.dev/docs/getting-started)


To get started with Brownie:

* Check out the other [Brownie mixes](https://github.com/brownie-mix/) that can be used as a starting point for your own contracts. They also provide example code to help you get started.
* ["Getting Started with Brownie"](https://medium.com/@iamdefinitelyahuman/getting-started-with-brownie-part-1-9b2181f4cb99) is a good tutorial to help you familiarize yourself with Brownie
* For more in-depth information, read the [Brownie documentation](https://eth-brownie.readthedocs.io/en/stable/)


Any questions? Join our [Gitter](https://gitter.im/eth-brownie/community) channel to chat and share with others in the community. -->
