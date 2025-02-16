document.getElementById('registrationForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const first_name = document.getElementById('first_name').value;
    const last_name = document.getElementById('last_name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirm_password = document.getElementById('confirm_password').value;

    if (password !== confirm_password) {
        document.getElementById('message').textContent = "Passwords do not match!";
        return;
    }

    const response = await fetch('https://sporting-server-pmrvwpqq4-rabiul-hosens-projects.vercel.app/accounts/register/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, first_name, last_name, email, password, confirm_password })
    });

    const data = await response.json();

    if (response.ok) {
        document.getElementById('message').textContent = "Registration successful!";
        document.getElementById('message').classList.remove('text-red-600');
        document.getElementById('message').classList.add('text-green-600');
    } else {
        document.getElementById('message').textContent = data.error || "Registration failed!";
    }
});
