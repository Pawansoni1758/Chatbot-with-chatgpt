from bardapi import Bard
from dotenv import load_dotenv

load_dotenv()
token = "bAj5iBGJM__kfSmxIBcg0Vng_2RiMX-54AE_K2nQlyUGkalrUWlnI25uLN8IBJFpojvlVg.."
bard = Bard(token=token)
result = bard.get_answer("who is the pm of india")
print(result)
