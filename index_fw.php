<html lang="de-DE">
<style>
table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}
</style>
<?php
header("Refresh: 5");
$mysqlhost = "localhost";
$mysqluser = "root";
$mysqlpass = "mysql";
$mysqldb = "syslog_server";

$conn = new mysqli($mysqlhost, $mysqluser, $mysqlpass, $mysqldb);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sqlcode = "SELECT * FROM syslog_fw ORDER BY tstamp DESC LIMIT 100";
$result = $conn->query($sqlcode);
echo "<table><tr><th>Zeit</th><th>FW-ID</th><th>Von</th><th>Zu</th><th>Nachricht</th></tr>";
if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>" . $row["tstamp"] . "</td><td>" . $row["ip"] . "</td><td>" .$row["from_ip"]. "</td><td>".$row["to_ip"]."</td><td>".$row["msg"]."</tr>";
    }
    echo "</table>";
} else {
    echo "</table>";
}
$conn->close();
?>
</html>