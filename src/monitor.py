from web3 import Web3
import pickle
import pandas as pd

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

if not web3.is_connected():
    print("Failed to connect to Ganache")
    exit()

# Load the AI model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Function to analyze transactions
def analyze_transaction(transaction):
    df = pd.DataFrame([transaction])
    features = df[['amount']]
    prediction = model.predict(features)
    return prediction[0]

# Monitor transactions
def monitor_transactions():
    print("Monitoring transactions...")
    block_number = web3.eth.block_number
    while True:
        new_block_number = web3.eth.block_number
        if new_block_number > block_number:
            block = web3.eth.get_block(new_block_number, full_transactions=True)
            for tx in block.transactions:
                tx_data = {
                    'amount': tx['value'],
                    'is_fraudulent': 0  # Placeholder, since we are predicting this
                }
                result = analyze_transaction(tx_data)
                print(f"Transaction {tx['hash'].hex()} is {'fraudulent' if result else 'legitimate'}")
            block_number = new_block_number

monitor_transactions()
