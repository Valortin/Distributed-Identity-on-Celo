// script.js

const registrationForm = document.getElementById('registrationForm');
const authenticationForm = document.getElementById('authenticationForm');

registrationForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const username = document.getElementById('usernameInput').value;
    const password = document.getElementById('passwordInput').value;

    // Make a POST request to the backend for user registration
    const response = await fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username,
            password
        })
    });

    const data = await response.json();
    console.log(data);
});

authenticationForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const username = document.getElementById('authUsernameInput').value;
    const password = document.getElementById('authPasswordInput').value;

    // Make a POST request to the backend for user authentication
    const response = await fetch('/authenticate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username,
            password
        })
    });

    const data = await response.json();
    console.log(data);
});
