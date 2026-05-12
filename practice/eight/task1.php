<?php
/**
 * «Веб-технології», О.О.Павлова, 2020 р., Практична робота 12-13
 * Завдання 1: Суперглобальні змінні PHP (Controller)
 */

// Ініціалізація сесії для можливості виводу $_SESSION
session_start();

// Встановлення тестових даних
if (!isset($_SESSION['sample_session_var'])) {
    $_SESSION['sample_session_var'] = 'Session value example';
}
setcookie('sample_cookie', 'Cookie value example', time() + 3600, "/");

$title = "Суперглобальні змінні PHP";
$header_info = "«Веб-технології», О.О.Павлова, 2020 р., Практична робота 12-13";

// Масив з характеристиками суперглобальних змінних
$superglobals_info = [
    '$GLOBALS' => [
        'desc' => 'Містить посилання на всі змінні, які на даний момент визначені в глобальній області видимості скрипта.',
        'data' => null 
    ],
    '$_SERVER' => [
        'desc' => 'Масив, що містить інформацію про заголовки, шляхи та місцеположення скриптів.',
        'data' => $_SERVER
    ],
    '$_GET' => [
        'desc' => 'Асоціативний масив змінних, переданих поточному скрипту через параметри URL.',
        'data' => $_GET
    ],
    '$_POST' => [
        'desc' => 'Асоціативний масив змінних, переданих поточному скрипту через HTTP метод POST.',
        'data' => $_POST
    ],
    '$_FILES' => [
        'desc' => 'Асоціативний масив елементів, завантажених в поточний скрипт через метод POST.',
        'data' => $_FILES
    ],
    '$_COOKIE' => [
        'desc' => 'Асоціативний масив змінних, переданих поточному скрипту через HTTP Cookies.',
        'data' => $_COOKIE
    ],
    '$_SESSION' => [
        'desc' => 'Асоціативний масив, що містить змінні сесії, доступні для поточного скрипта.',
        'data' => isset($_SESSION) ? $_SESSION : []
    ],
    '$_REQUEST' => [
        'desc' => 'Асоціативний масив, який за замовчуванням містить вміст $_GET, $_POST та $_COOKIE.',
        'data' => $_REQUEST
    ],
    '$_ENV' => [
        'desc' => 'Асоціативний масив змінних, переданих поточному скрипту через середовище виконання.',
        'data' => !empty($_ENV) ? $_ENV : ['INFO' => 'Масив $_ENV може бути порожнім, якщо в php.ini параметр variables_order не містить "E"']
    ]
];

/**
 * Функція для форматування виводу значень масиву
 */
function formatValue($name, $data) {
    if ($name === '$GLOBALS') {
        return "Масив \$GLOBALS містить рекурсивні посилання на самого себе та всі інші глобальні змінні.";
    }
    
    if (empty($data)) {
        return "Масив порожній або змінні не передані.";
    }

    $output = "";
    foreach ($data as $key => $value) {
        $display_val = is_array($value) ? "Array(...)" : (string)$value;
        $output .= htmlspecialchars($key) . " = " . htmlspecialchars($display_val) . "\n";
    }
    return rtrim($output);
}

// Підключення шаблону
include 'template1.php';
