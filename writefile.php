<?php

file_put_contents('gs://phpeste/hello.txt', 'Hello');

print file_get_contents('gs://phpeste/hello.txt');