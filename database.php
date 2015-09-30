<?php

$db = new pdo('mysql:unix_socket=/cloudsql/hello-phpeste:db1',
  'root',  // username
  ''       // password
);

var_dump($db);
