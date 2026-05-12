<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $title; ?></title>
    <link rel="stylesheet" href="style1.css">
</head>
<body>

    <div class="header-text"><?php echo $header_info; ?></div>

    <h1><?php echo $title; ?></h1>

    <div class="task-description">
        <p>Завдання 1. Створіть сторінку під назвою «Суперглобальні змінні PHP» і виведіть значення наступних змінних у табличній формі:</p>
        <ul>
            <li>$GLOBALS</li>
            <li>$_SERVER</li>
            <li>$_GET</li>
            <li>$_POST</li>
            <li>$_FILES</li>
            <li>$_COOKIE</li>
            <li>$_SESSION</li>
            <li>$_REQUEST</li>
            <li>$_ENV</li>
        </ul>
        <p>Приклад оформлення інформації показано нижче (табл.1):</p>
    </div>

    <table>
        <thead>
            <tr>
                <th>Позначення змінної</th>
                <th>Характеристика</th>
                <th>Отримане значення</th>
            </tr>
        </thead>
        <tbody>
            <tr class="placeholder-row">
                <td colspan="3">...</td>
            </tr>
            <?php foreach ($superglobals_info as $name => $info): ?>
                <tr>
                    <td class="designation"><?php echo $name; ?></td>
                    <td class="characteristic"><?php echo $info['desc']; ?></td>
                    <td class="value">
                        <pre><?php echo formatValue($name, $info['data']); ?></pre>
                    </td>
                </tr>
            <?php endforeach; ?>
            <tr class="placeholder-row">
                <td colspan="3">...</td>
            </tr>
        </tbody>
    </table>

    <div class="table-caption">Таблиця 1 – Приклад оформлення інформації завдання 1</div>

</body>
</html>
