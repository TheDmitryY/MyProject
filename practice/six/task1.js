document.addEventListener('DOMContentLoaded', () => {
    const colorSelect = document.getElementById('colorSelect');

    colorSelect.addEventListener('change', (event) => {
        const selectedColor = event.target.value;
        if (selectedColor) {
            document.body.style.backgroundColor = selectedColor;
        } else {
            document.body.style.backgroundColor = ''; // Скидання до стандартного
        }
    });
});
