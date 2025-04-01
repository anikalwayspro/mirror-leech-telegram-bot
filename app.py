from flask import Flask
import os

app = Flask(__name__)

# Main route
@app.route('/')
def hello_world():
    return 'Hello from Anik!'

# Health check route
@app.route('/health')
def health_check():
    return "Health Check OK", 200

if __name__ == "__main__":
    # Get the port from environment variable (default to 8080)
    port = int(os.getenv("PORT", 8080))
    # Run the app, bind to all network interfaces
    print(f"Starting Flask app on port {port}...")
    app.run(host="0.0.0.0", port=port, debug=True)
