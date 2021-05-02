<?php 

session_start(['name'=>'VICTOR']);
//session_destroy();  // Elimina la sesion
unset($_SESSION['login']);
// if(session_status()==PHP_SESSION_DISABLE){
  
// }
if(isset($_SESSION['login'])){
  echo 'Bienvenido '.$_SESSION['login'];
  $_SESSION['login']='Cliente';
}else{
  echo 'Sin session';
}

 ?>

<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <form action='login_session.php' method='post'>
      Usuario: <input type='text' name='userName'><br>
      Password: <input type='password' name='password'><br>
      <input type='submit' name='send' text='Enviar'>
    </form>
    
  </body>
</html>