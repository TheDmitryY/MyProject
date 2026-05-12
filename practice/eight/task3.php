<?php

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $c = isset($_POST['c']) ? (int)$_POST['c'] : 0;
    $d = isset($_POST['d']) ? (int)$_POST['d'] : 0;

    $sum = $c + $d;
    $product = $c * $d;
    $difference = $c - $d;
    $quotient = ($d != 0) ? ($c / $d) : "Ділення на нуль неможливе";
} else {
    header("Location: task3.html");
    exit;
}

?>
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Результати Завдання 3</title>
    <link rel="stylesheet" href="task3.css">
</head>
<body>
    <div class="container">
        <h1>Результати (POST)</h1>
        <div class="result">
            <p>Число c: <?php echo $c; ?></p>
            <p>Число d: <?php echo $d; ?></p>
            <hr>
            <p>Сума: <?php echo $sum; ?></p>
            <p>Добуток: <?php echo $product; ?></p>
            <p>Різниця: <?php echo $difference; ?></p>
            <p>Частка: <?php echo $quotient; ?></p>
        </div>
        <br>
        <a href="task3.html">Назад до форми</a>
    </div>
</body>
</html>
