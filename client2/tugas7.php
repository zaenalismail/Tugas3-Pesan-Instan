<?php
    date_default_timezone_set('Asia/Jakarta');

    $now = new DateTime();
    $minutes = $now -> getOffset()/60;

    $tanda = ($minutes < 0 ? -1 : 1);
    $minutes = abs($minutes);
    $hour = floor($minutes/60);
    $minutes = $hour * 60;

    $offset = sprintf('%+d:%02d', $tanda*$hour, $minutes);

    mysql_connect($server, $username, $password);
    mysql_select_db($database);

    mysql_query("SET time_zone = '$offset'");
?>