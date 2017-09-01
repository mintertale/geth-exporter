# geth-exporter
go-Ethereum exporter for Prometheus

## General
A go-Ethereum exporter, written in Python3, for Prometheus.

## Installation
Details will follow. For now, you can look at the

## Configuration
### `node_exporter` Configuration
`geth-exporter` doesn't open a port, rather it uses the `textfile` collector in `node_exporter`. You need to start
node_exporter with the option `-collectors.enabled textfile` and you need to specify the folder where the metrics are
located with `-collector.textfile.directory /your/path`

### `geth` Configuration
`geth-exporter` uses the HTTP-RPC server in geth. To enable it, you need to start geth with the following options:
*   `--rpc`
*   `--rpcapi=db,eth,net,web3,personal`

> *WARNING* Never allow access from the Internet to the `geth` HTTP-RPC server.

### Environment Variables
The following environment variables are used by `geth-exporter`:
*   `LOGLEVEL` one of `DEBUG`, `INFO`, `WARNING`, `ERROR`

### Configuration file
The configuration file is located in `/etc/geth-exporter/geth-exporter.yaml`. The following values are accepted:
```
geth_exporter:
  prom_folder: '/var/lib/node_exporter' # node_exporter textfile folder
  interval: 60 # polling interval in seconds
  geth_host: 'localhost' # server with the geth HTTP-RPC server
  geth_port: '8545' # the port of the geth HTTP-RPC
  additional_accounts: []
```

You can specify additional accounts, that are not located in your geth wallet:
```
geth_exporter:
  prom_folder: '/var/lib/node_exporter'
  interval: 60
  geth_host: 'localhost'
  geth_port: '8545'
  additional_accounts:
    - 0xaaaa...
    - 0xbbbb...
    - 0xcccc...
```

## Example Metric
```
# HELP geth_block_number The number of the most recent block
# TYPE geth_block_number gauge
geth_block_number 4227955.0
# HELP geth_syncing Boolean syncing status
# TYPE geth_syncing gauge
geth_syncing 0.0
# HELP geth_hash_rate The current number of hashes per second the node is mining with
# TYPE geth_hash_rate gauge
geth_hash_rate 0.0
# HELP geth_gas_price_wei The current gas price in Wei
# TYPE geth_gas_price_wei gauge
geth_gas_price_wei 28987298387.0
# HELP account_balance Account Balance
# TYPE account_balance gauge
account_balance{account="0xaaaa...",currency="ETH",type="geth"} 1.225055210216375
# HELP geth_mining Boolean mining status
# TYPE geth_mining gauge
geth_mining 0.0
```

## Donations
If you want to support this work, donations in ETH are welcomed.
*   `0x90833394db1b53f08b9d97dab8beff69fcf3ba49`
