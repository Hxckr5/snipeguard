from solana.rpc.api import Client as SolanaClient
from solana.account import Account
from solana.transaction import Transaction
from spl.token.constants import TOKEN_PROGRAM_ID
from spl.token.instructions import transfer as spl_transfer

solana_client = SolanaClient(SOLANA_RPC_URL)

def transfer_tokens_solana(token_address, amount, recipient_address, private_key_hex):
    account = Account.from_secret_key(bytes.fromhex(private_key_hex))
    transaction = Transaction()

    transaction.add(
        spl_transfer(
            TransferParams(
                program_id=TOKEN_PROGRAM_ID,
                source=account.public_key(),
                dest=recipient_address,
                owner=account.public_key(),
                amount=amount
            )
        )
    )

    response = solana_client.send_transaction(transaction, account)
    return response['result']
