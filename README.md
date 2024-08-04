# CHECK-CREATE-PASSWORD-API

## Description

API for checking and creating a hashed password for various programs (for example, for authorization in a telegram bot)

## Installation

Follow the instructions below to install and run the api.

## Installation steps

1. Clone the repository

    ```bash
    git clone https://github.com/CinnamonPiee/CheckCreatePasswordAPI.git
    ```

2. Create and activate a virtual environment

   - Windows
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

   - Linux and MacOS
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Run the api with the command

    ```bash
    uvicorn main:app --reload
    ```

## Usage example
Password encryption
```
curl -X 'POST' \
  'http://127.0.0.1:8000/encrypt/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "password": "YOUR PASSWORD"
}'
```
Password verification
```
curl -X 'POST' \
  'http://127.0.0.1:8000/check/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "password": "YOUR PASSWORD",
  "hashed_password": "HASHED PASSWORD"
}'
```