<?php
// Database configuration
$servername = "localhost"; // Change this to your server address
$username = "root"; // Change this to your database username
$password = ""; // Change this to your database password
$database = "advert"; // Change this to your database name

// Create connection
$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} else {
    //echo "Connected successfully";
}

// Close connection
$conn->close();
?>
