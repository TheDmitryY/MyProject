<?php
/**
 * Завдання 2: Математичні обчислення через GET
 */

$a = isset($_GET['a']) ? (int)$_GET['a'] : 0;
$b = isset($_GET['b']) ? (int)$_GET['b'] : 0;

$sum = $a + $b;
$product = $a * $b;
$difference = $a - $b;
$quotient = ($b != 0) ? ($a / $b) : "Ділення на нуль неможливе";

?>
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Результати Завдання 2</title>
    <link rel="stylesheet" href="task2.css">
</head>
<body>
    <div class="container">
        <h1>Результати (GET)</h1>
        <div class="result">
            <p>Число a: <?php echo $a; ?></p>
            <p>Число b: <?php echo $b; ?></p>
            <hr>
            <p>Сума: <?php echo $sum; ?></p>
            <p>Добуток: <?php echo $product; ?></p>
            <p>Різниця: <?php echo $difference; ?></p>
            <p>Частка: <?php echo $quotient; ?></p>
        </div>
        <br>
        <a href="task2.html">Назад</a>
    </div>
</body>
</html>
