document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const username = document.getElementById('username').value;
    const fullname = document.getElementById('fullname').value;
    const message = document.getElementById('message');
    
    message.innerHTML = `<p class="success">Дякуємо за реєстрацію, ${fullname}!<br>Ваш логін: ${username}</p>`;
    
    // Можна додати додаткову логіку, наприклад, очищення форми
    // this.reset();
});
