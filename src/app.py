from flask import Flask, render_template, request, jsonify
import asyncio
from browser_agent import main as run_browser_agent

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-task', methods=['POST'])
async def run_task():
    task_input = request.json.get('task')
    if not task_input:
        return jsonify({'error': 'No task provided'}), 400

    result = await run_browser_agent(task_input)
    print(result)
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)