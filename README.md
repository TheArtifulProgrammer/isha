# Therapy Bot using Flask and GPT-3.5-Turbo

This is a therapy bot built using Flask and GPT-3.5-Turbo. The bot is designed to provide therapy assistance to users by answering their questions in a friendly and engaging manner.

## Usage

1. **Installation**:
   - Clone this repository.
   - Install the required dependencies using `pip install -r requirements.txt`.
   - Create a `.env` file and add your OpenAI API key.

2. **Setting Up**:
   - Make sure you have your OpenAI API key. If not, you can get it from [OpenAI](https://openai.com/).
   - Update the `.env` file with your OpenAI API key.

3. **Run the Application**:
   - Run the Flask application using `python app.py`.
   - Visit `http://localhost:5000` in your web browser.

4. **Interacting with the Bot**:
   - Send POST requests to `http://localhost:5000/hi/isha` with JSON payload containing the user's question.
   - The bot will respond with therapy assistance based on the question.

## Code Structure

The code is structured as follows:

- `app.py`: Contains the Flask application setup and routes for handling user requests.
- `isha.py`: Defines the `Isha` class responsible for interacting with the OpenAI GPT-3.5-Turbo model and providing therapy assistance.
- `index.html`: Provides a simple interface for interacting with the bot (optional).

## Dependencies

- Flask
- Flask-CORS
- python-dotenv
- openai

## API Endpoints

- `POST /hi/isha`: Accepts a JSON payload with a user's question and returns the bot's response.

## Configuration

Make sure to set up your environment variables properly:

```dotenv
OPENAI_API_KEY=your_openai_api_key

```

## Disclaimer

This bot is intended for educational and demonstrative purposes only. It is not a substitute for professional therapy or medical advice. Use it at your own discretion.
