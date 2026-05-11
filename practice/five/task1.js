const name = prompt("Введіть ваше ім'я:", "Павло Бондар");
const profession = prompt("Введіть вашу професію:", "computer engineering");
const phone = prompt("Введіть ваш телефон:", "067-888-88-88");

if (name && profession && phone) {
    const container = document.getElementById('container');
    const table = document.createElement('table');

    for (let i = 0; i < 12; i++) {
        const tr = document.createElement('tr');
        for (let j = 0; j < 3; j++) {
            const td = document.createElement('td');
            td.innerHTML = `
                <div class="card">
                    <div class="icon">
                        <div class="square2"></div>
                        <div class="square1"></div>
                    </div>
                    <div class="info">
                        <div class="name">${name}</div>
                        <div class="profession">${profession}</div>
                        <div class="phone">${phone}</div>
                    </div>
                </div>
            `;
            tr.appendChild(td);
        }
        table.appendChild(tr);
    }
    container.appendChild(table);
} else {
    document.body.innerHTML = "<h1>Дані не введено. Будь ласка, оновіть сторінку та заповніть поля.</h1>";
}
