# Task_2_API_Key_Generation_and_Sharing
RootSoftware Text-Processing API

## 🎥 Demo Video
**[Watch Demo Video](https://drive.google.com/file/d/1UueYUAOGbtRdPnO7UE3V8ouIH7i-6gg_/view?usp=drive_link)**

## How to Run
pip install -r requirements.txt
python app.py

## Test
Valid Key:
curl -X POST http://127.0.0.1:5000/process -H "X-API-Key: YOUR_KEY" -H "Content-Type: application/json" -d '{"text": "hello"}'

Invalid Key: 403 Error
Missing Key: 401 Error


