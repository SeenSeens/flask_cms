from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env.example file.

from app import app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)