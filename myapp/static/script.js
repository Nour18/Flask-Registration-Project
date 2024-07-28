document.getElementById('registration-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const data = {
        first_name: formData.get('first_name'),
        last_name: formData.get('last_name'),
        email: formData.get('email'),
        phone_number: formData.get('phone_number'),
        password: formData.get('password')
    };

    try {
        const response = await fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        const responseMessage = document.getElementById('response-message');

        if (response.ok) {
            responseMessage.textContent = 'User registered successfully!';
            responseMessage.style.color = 'green';
        } else {
            responseMessage.textContent = result.message || 'Registration failed.';
            responseMessage.style.color = 'red';
        }
    } catch (error) {
        document.getElementById('response-message').textContent = 'An error occurred.';
    }
});
