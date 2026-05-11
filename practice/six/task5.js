document.getElementById('calcBtn').addEventListener('click', function() {
    const n1 = parseFloat(document.getElementById('num1').value);
    const n2 = parseFloat(document.getElementById('num2').value);
    
    if (isNaN(n1) || isNaN(n2)) {
        alert('Будь ласка, введіть обидва числа!');
        return;
    }
    
    const sum = n1 + n2;
    
    // Вивід у поле форми
    document.getElementById('resultField').value = sum;
    
    // Вивід у діалогове вікно
    alert('Результат обчислення: ' + sum);
});
