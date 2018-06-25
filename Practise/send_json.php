<?php

$data = [ 'name' => 'Jane', 'age' => 17 ];
header('Content-Type: application/json');

echo json_encode($data);

?>

