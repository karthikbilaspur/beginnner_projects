A simple and secure web server implemented using Python's built-in http.server module. The server supports HTTPS and basic authentication.
Features
HTTPS Support: The server uses SSL/TLS encryption to ensure secure communication.
Basic Authentication: The server supports basic authentication using username and password.
Multi-Threading: The server uses multi-threading to handle multiple requests concurrently.
Error Handling: The server includes error handling to handle and log exceptions.
Installation
Install Python 3.9 or later.
Run pip install -r requirements.txt to install dependencies.
Usage
Run python webserver.py to start the server.
Open a web browser and navigate to https://localhost:8000 to access the server.
Configuration
Update server.crt and server.key files to use custom SSL/TLS certificates.
Update SimpleHTTPRequestHandler class to customize server behavior.
Logging
The server logs requests and errors to server.log file.
Update logging.basicConfig function to customize logging configuration.

