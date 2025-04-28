# Simple HTTP Web Server

A lightweight HTTP web server implemented in Python, designed to handle HTTP GET requests. This project includes two versions of the server: a single-threaded implementation (Task 1) and a multi-threaded implementation with a client script (Task 2). The server serves static HTML files, such as `index.html`, and handles 404 errors when requested files are not found.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Task 1: Single-Threaded Server](#task-1-single-threaded-server)
  - [Task 2: Multi-Threaded Server with Client](#task-2-multi-threaded-server-with-client)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Single-Threaded Server (Task 1)**: A basic HTTP server that handles one client request at a time, serving static HTML files.
- **Multi-Threaded Server (Task 2)**: An enhanced server that handles multiple client requests concurrently using threading.
- **Client Script (Task 2)**: A Python client that sends HTTP GET requests to the server and displays the response.
- **Error Handling**: Returns a 404 Not Found response if the requested file is not available.
- **Simple and Lightweight**: Designed for educational purposes to demonstrate HTTP server-client communication.

## Project Structure
```
Simple-HTTP-Web-Server/
├── server.py           # Single-threaded server (Task 1)
├── server_threaded.py  # Multi-threaded server (Task 2)
├── client.py           # Client script for Task 2
├── index.html          # Sample HTML file served by the server
└── README.md           # Project documentation
```

## Requirements
- Python 3.x
- No external libraries are required (uses standard Python libraries: `socket`, `sys`, `threading`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/nnichaelangello/Simple-HTTP-Web-Server.git
   cd SimpleHTTPServer
   ```
2. Ensure Python 3.x is installed on your system:
   ```bash
   python3 --version
   ```
3. Place an `index.html` file (or other HTML files) in the project directory to be served by the server.

## Usage

### Task 1: Single-Threaded Server
The single-threaded server handles one client request at a time.

1. Run the server:
   ```bash
   python3 server.py
   ```
2. Open a web browser or use a tool like `curl` to access the server:
   ```bash
   curl http://127.0.0.1:6789/index.html
   ```
3. The server will serve `index.html` or return a 404 error if the file is not found.
4. To stop the server, press `Ctrl+C`.

### Task 2: Multi-Threaded Server with Client
The multi-threaded server handles multiple client requests concurrently, and the client script sends HTTP GET requests.

1. Run the multi-threaded server:
   ```bash
   python3 server_threaded.py
   ```
2. In a separate terminal, run the client script to request a file:
   ```bash
   python3 client.py 127.0.0.1 6789 index.html
   ```
3. The client will display the server's response, including the HTTP headers and the content of `index.html`.
4. To stop the server, press `Ctrl+C`.

### Notes
- The server listens on `127.0.0.1:6789` by default.
- Ensure the requested file (e.g., `index.html`) exists in the project directory.
- The client script requires three command-line arguments: `server_host`, `server_port`, and `filename`.

## Example Output

### Task 1: Single-Threaded Server
Running `server.py`:
```
Siap menerima permintaan...
```
Accessing `http://127.0.0.1:6789/index.html` via browser or `curl`:
```html
<html>
<body>
<h1>Hello, World!</h1>
</body>
</html>
```

### Task 2: Multi-Threaded Server and Client
Running `server_threaded.py`:
```
Server siap menerima permintaan...
Koneksi dari ('127.0.0.1', 54321)
```
Running `client.py 127.0.0.1 6789 index.html`:
```
Respons dari server:
HTTP/1.1 200 OK
Content-Type: text/html

<html>
<body>
<h1>Hello, World!</h1>
</body>
</html>
```

If the file is not found:
```
Respons dari server:
HTTP/1.1 404 Not Found
Content-Type: text/html

<html><body><h1>404 Not Found</h1></body></html>
```
