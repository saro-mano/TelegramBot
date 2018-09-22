<?php

$botToken = "589993469:AAHfQ_HedQkc5sVDIUiwU_qzTcQ5qu37SbM";
$website = "https://api.telegram.org/bot".$botToken;

$update = file_get_contents($website."/getUpdates");

$update_array = json_decode($update, TRUE);

$text =  $update_array["result"][0]["message"]["text"];

print_r($text);

?>