<?php

$botToken = "589993469:AAHfQ_HedQkc5sVDIUiwU_qzTcQ5qu37SbM";
$website = "https://api.telegram.org/bot".$botToken;

$update = file_get_contents($website."/getUpdates");

$update_array = json_decode($update, TRUE);

$chat_id =  $update_array["result"][0]["message"]["chat"]["id"];

file_get_contents($website."/sendMessage?chat_id=".$chat_id."&text=test");

?>
