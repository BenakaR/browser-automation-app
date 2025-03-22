# browser-automation-app

This project is a simple frontend application that automates browsing tasks using a generative AI model. It allows users to input their browsing automation tasks, executes the provided Python code, and displays the results.

## Project Structure

```
browser-automation-app
├── src
│   ├── backend
│   │   ├── __init__.py
│   │   ├── browser_agent.py
│   │   └── browser_use.py
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── main.js
│   └── templates
│   │   └── index.html
│   ├── app.py
│   └── config.py
├── requirements.txt
├── .env
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd browser-automation-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables in the `.env` file. Make sure to include your API keys and any other necessary configurations.

## Usage

1. Run the application:
   ```
   python src/app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000` (or the appropriate port specified in your app).

3. Enter your browsing automation task in the input field and submit the form.

4. View the results displayed on the web page after the task is completed.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.
