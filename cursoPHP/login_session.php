<?php 
$user='Victor';
$pass='123';


session_start();     // Iniciar sesion.
if($_POST['userName']==$user && $_POST['password']==$pass){
  $_SESSION['login']='Administrador';
  header('Location: index.php');
}else{
  echo 'Usuario y password incorrectos';
}
   
   ?>