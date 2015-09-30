<?php

session_start();
$_SESSION['count']++;

print $_SESSION['count'];
