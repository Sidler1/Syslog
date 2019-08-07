<html>
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

$sqlcode = "SELECT * FROM syslog_switch ORDER BY tstamp DESC LIMIT 100";
$result = $conn->query($sqlcode);
echo "<table><tr><th>Zeit</th><th>Switch</th><th>Nachricht</th></tr>";
if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "</td><td>" . $row["tstamp"] . "</td><td>" . $row["from_ip"] . "</td><td>".$row["msg"]."</tr>";
    }
    echo "</table>";
} else {
    echo "</table>";
    echo "0 results";
}
$conn->close();
?>
</html>