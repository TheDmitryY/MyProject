document.addEventListener('DOMContentLoaded', () => {
    const checkBtn = document.getElementById('check-btn');
    const resultDiv = document.getElementById('result');

    checkBtn.addEventListener('click', () => {
        const selectedOption = document.querySelector('input[name="flyer"]:checked');

        if (!selectedOption) {
            resultDiv.textContent = 'Будь ласка, обери варіант!';
            resultDiv.className = 'error';
            return;
        }

        if (selectedOption.value === 'correct') {
            resultDiv.textContent = 'Вірно! Ти молодець! 🌟';
            resultDiv.className = 'success';
        } else {
            resultDiv.textContent = 'Невірно. Спробуй ще раз! 😊';
            resultDiv.className = 'error';
        }
    });
});
