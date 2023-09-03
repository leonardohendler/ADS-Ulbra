<?php
// Fazer a junção de tudo.
const FOLDER= 'aula2';

if (isset($_GET['controller']) && isset($_GET['acao'])){
    $controller = $_GET['controller'];
    $metodo = $_GET['acao'];
    $controller .= "Controller";
    
   
    
    
    require_once $_SERVER ['DOCUMENT_ROOT'] . '/' . FOLDER . '/controller/'. $controller . '.php';
    
    
    $objeto = new $controller();
    $objeto->$metodo();
} else{
    require_once $_SERVER ['DOCUMENT_ROOT'] . '/' . FOLDER . '/view/home.php';
}


// require_once $_SERVER['DOCUMENT_ROOT'] . '/aula2/controller/' .$classe. '.php';
//require_once = dentro da pasta, eu quero que chame, como se fosse importar.