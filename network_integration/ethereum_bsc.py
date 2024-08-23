from web3 import Web3
import json

# Initialize Web3 connection
web3_eth = Web3(Web3.HTTPProvider(WEB3_INFURA_URL))
web3_bsc = Web3(Web3.HTTPProvider(WEB3_BSC_URL))

def swap_tokens_eth_bsc(token_in, token_out, amount_in, private_key, network):
    if network == 'ETH':
        web3 = web3_eth
    elif network == 'BSC':
        web3 = web3_bsc
    else:
        raise ValueError("Unsupported network")

    # Load wallet and contract
    account = web3.eth.account.privateKeyToAccount(private_key)
    router_address = Web3.toChecksumAddress('<ROUTER_CONTRACT_ADDRESS>')
    router_abi = json.loads('[... ABI JSON ...]')  # Replace with actual ABI
    router_contract = web3.eth.contract(address=router_address, abi=router_abi)

    # Build transaction
    tx = router_contract.functions.swapExactTokensForTokens(
        amount_in,
        0,  # Slippage tolerance
        [token_in, token_out],
        account.address,
        int(time.time()) + 60 * 10  # Deadline (10 minutes from now)
    ).buildTransaction({
        'chainId': 1 if network == 'ETH' else 56,  # Chain ID for ETH or BSC
        'gas': 200000,
        'gasPrice': web3.toWei('5', 'gwei'),
        'nonce': web3.eth.getTransactionCount(account.address)
    })

    signed_tx = web3.eth.account.sign_transaction(tx, private_key=private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_hash
