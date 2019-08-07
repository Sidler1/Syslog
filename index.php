<?php

$mysqlhost = "192.168.0.234";
$mysqluser = "felix";
$mysqlpass = "mysql";
$mysqldb = "syslog_server";

$conn = new mysqli($mysqlhost, $mysqluser, $mysqlpass, $mysqldb);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sqlcode = "SELECT * FROM syslog_fw ORDER BY tstamp DESC";
$result = $conn->query($sqlcode);
echo "<tr><th>ID</th><th>Zeit</th><th>FW-ID</th><th>Von</th><th>Zu</th><th>Nachricht</th></tr>";
if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>" . $row["id"]. "</td><trd>" . $row["tstamp"]. "</td><td>" . $row["ip"]. "</td><td>" .$row["from_ip"]. "</td><td>".$row["to_ip"]."</td><td>".$row["msg"]."</tr>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>