# Riddle Game (Socket.IO + Python)

This project is based on a template from the course [Stepik: Writing WebSockets in Python](https://stepik.org/course/195202/info). It is a simple riddle game built with Python and Socket.IO. In this project I learned how to work with WebSockets, handle real-time communication, and manage game logic.
## Features

- Real-time interaction with players via WebSockets
- Players can request new riddles and submit answers
- The system evaluates answers and keeps track of scores

## Installation and Setup

1. **Clone the repository:**
    
    ```sh
    git clone https://github.com/kateutkate23/socketio_riddle_game.git
    cd socketio_riddle_game
    ```
    
2. **Create a virtual environment and activate it:**
    
    ```sh
    python -m venv venv
    # On Linux
    source venv/bin/activate
    # On Windows
    venv\Scripts\activate
    ```
    
3. **Install dependencies:**
    
    ```sh
    pip install -r requirements.txt
    ```
    
4. **Run the application:**
    
    ```sh
    python main.py
    ```
    
5. **Open in your browser:**
    
    - Visit `http://127.0.0.1:8000/` to start playing.

## Technologies Used

- Python
- Socket.IO
- Eventlet

---

### License

This project is for learning purposes and is open for modification and improvement.
