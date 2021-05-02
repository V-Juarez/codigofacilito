<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>
  <form method='post' action='form.php'>
    <table>
      <?php
      $array= array('name'=>'Nombre','lastname'=>'Apellido','adress'=>'direccion','phone'=>'Telefono');
      foreach($array as $key=>$value):
      ?>
        <tr>
          <td><?php echo $value?>
          </td>
          <td>
            <input type='text' name=<? echo $key?> >
          </td>
        </tr>
      <?php endforeach; ?>
      <tr>
        <td>sexo
        </td>
        <td>
          <input type="radio" name='sex' value="Mujer"> Mujer
          <input type="radio" name='sex' value="Hombre"> Hombre
        </td>
      </tr>
      <tr>
        <td>
          <input type="submit" name='submit' value="Guardar">
        </td>
      </tr>
    </table>
  </form>
  <h1><?php echo "!!!!! {$_GET['answer']} gracias {$_GET['name']}";?></h1>
</body>

</html>