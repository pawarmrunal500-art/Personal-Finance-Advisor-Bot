import time
from pyngrok import ngrok

try:
    ngrok.set_auth_token("3JxlfbMUPcIluv8sf2cCbaPOAQ9_5GprB1nGspUHemge1S11t")
    public_url = ngrok.connect(5000)
    print(f"Ngrok Tunnel is active at: {public_url}")
    print("Keep this script running to keep the tunnel open.")
    while True:
        time.sleep(1)
except Exception as e:
    print(f"Failed to start ngrok: {e}")
