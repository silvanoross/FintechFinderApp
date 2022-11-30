# This funciton will generate a mnemonic key string and save it to a local .env file if not in existance

# import and load the env variables
from dotenv import load_dotenv
import os
from mnemonic import Mnemonic

# load environment variables
load_dotenv()

def create_mnemonic():
    # Load the value of the MNEMONIC variable from the .env file
    mnemonic = os.getenv("MNEMONIC")

    # Evaluate the contents of the mnemonic variable
    # Create a new mnemonic seed phrase if the value of mnemonic equals None
    if mnemonic is None:
        mnemo = Mnemonic("english")
        mnemonic = mnemo.generate(strength=128)
        with open(".env", 'w') as e:
            e.write(f"MNEMONIC={mnemonic}")