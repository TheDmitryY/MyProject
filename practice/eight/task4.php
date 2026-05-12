<?php

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $e = isset($_POST['e']) ? htmlspecialchars($_POST['e']) : "";
    $f = isset($_POST['f']) ? htmlspecialchars($_POST['f']) : "";
} else {
    header("Location: task4.html");
    exit;
}

?>
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Результати Завдання 4</title>
    <link rel="stylesheet" href="task4.css">
</head>
<body>
    <div class="container">
        <h1>Результати роботи з рядками</h1>
        
        <div class="result-box">
            <div class="variant">
                <h2>а) Перша змінна, потім друга:</h2>
                <p><?php echo "$e $f"; ?></p>
            </div>

            <div class="variant">
                <h2>б) Друга змінна, потім перша:</h2>
                <p><?php echo "$f $e"; ?></p>
            </div>
        </div>
        
        <br>
        <a href="task4.html">Повернутися</a>
    </div>
</body>
</html>
