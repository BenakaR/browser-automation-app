document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('automation-form');
    const resultDiv = document.getElementById('result-output');

    form.addEventListener('submit', async function(event) {
        event.preventDefault();
        const input = document.getElementById('task-input').value;

        const response = await fetch('/run-task', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ task: input }),
        });

        if (response.ok) {
            const result = await response.json();
            console.log(result);
            resultDiv.textContent = result.result;
        } else {
            resultDiv.textContent = 'Error executing task.';
        }
    });
});