<!DOCTYPE html>
<html>
<head>
	<title></title>
	<script type="text/javascript" src="k.js"></script>
</head>
<body>
	<form id="myForm" >
   <input type="text" name="fname">
 
  <input type="button" onclick="myFunction()" value="Submit form">
</form>
</body>
</html>

function myFunction() 
{
  document.getElementById("myForm").submit();
}
