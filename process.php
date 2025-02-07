<?php
$number = $_POST['number'];
$message = $_POST['message'];

$command = escapeshellcmd("python3 calculate.py $number $message");

$output = shell_exec($command);

echo $output;
?>