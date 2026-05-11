document.addEventListener('DOMContentLoaded', () => {
    const rows = document.querySelectorAll('#truth-table tbody tr');
    const checkBtn = document.getElementById('check-btn');
    const resetBtn = document.getElementById('reset-btn');
    const resultDiv = document.getElementById('result');

    rows.forEach(row => {
        const buttons = row.querySelectorAll('.ans-btn');
        buttons.forEach(btn => {
            btn.addEventListener('click', () => {
                buttons.forEach(b => b.classList.remove('selected'));
                btn.classList.add('selected');
                row.classList.remove('row-correct', 'row-incorrect');
            });
        });
    });

    checkBtn.addEventListener('mouseover', () => {
        let allCorrect = true;
        let allAnswered = true;

        rows.forEach(row => {
            const selectedBtn = row.querySelector('.ans-btn.selected');
            const correctAnswer = row.getAttribute('data-answer');

            if (!selectedBtn) {
                allAnswered = false;
                row.classList.remove('row-correct', 'row-incorrect');
                return;
            }

            if (selectedBtn.getAttribute('data-val') === correctAnswer) {
                row.classList.add('row-correct');
                row.classList.remove('row-incorrect');
            } else {
                row.classList.add('row-incorrect');
                row.classList.remove('row-correct');
                allCorrect = false;
            }
        });

        if (!allAnswered) {
            resultDiv.textContent = 'Будь ласка, дайте відповіді на всі питання!';
            resultDiv.className = 'incorrect';
        } else if (allCorrect) {
            resultDiv.textContent = 'Вітаємо! Всі відповіді правильні.';
            resultDiv.className = 'correct';
        } else {
            resultDiv.textContent = 'Є помилки. Спробуйте ще раз.';
            resultDiv.className = 'incorrect';
        }
    });

    resetBtn.addEventListener('click', () => {
        rows.forEach(row => {
            const buttons = row.querySelectorAll('.ans-btn');
            buttons.forEach(b => b.classList.remove('selected'));
            row.classList.remove('row-correct', 'row-incorrect');
        });
        resultDiv.textContent = '';
        resultDiv.className = '';
    });
});
