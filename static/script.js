// static/script.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predictionForm');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        predictPrice();
    });
});

function predictPrice() {
    const form = document.getElementById('predictionForm');
    const formData = new FormData(form);
    const data = {};
    formData.forEach((value, key) => data[key] = value);

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams(data).toString()
    })
    .then(response => response.json())
    .then(data => {
        if (data.predicted_price) {
            document.getElementById('result').innerText = `Predicted Price: $${data.predicted_price.toFixed(2)}`;
            document.getElementById('error').innerText = '';
        } else if (data.error) {
            document.getElementById('result').innerText = '';
            document.getElementById('error').innerText = `Error: ${data.error}`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = '';
        document.getElementById('error').innerText = 'An unexpected error occurred.';
    });
}
