<?php $professores = $_REQUEST ["professores"]; ?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de professores</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">


</head>
<body class="bg-dark">
<nav class="navbar navbar-expand-lg bg-body-tertiary" data-bs-theme="dark">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Meu site</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="/<?php echo FOLDER; ?>/">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link active" href="/<?php echo FOLDER; ?>/?controller=Estudante&acao=listar">Estudantes</a>
              </li>
              <li class="nav-item">
                <a class="nav-link active" href="/<?php echo FOLDER; ?>/?controller=Professor&acao=listar">Professores</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Cadastrar</a>
              </li>
            </ul>
            <form class="d-flex" role="search">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
          </div>
        </div>
      </nav>  
<div class="container text-center text-white">
<div>
  <h2 class='m-5 p-3' >Semana da acessibilidade</h2>
  <img class='w-50 h-50' src="https://www.politize.com.br/wp-content/uploads/2022/03/acessibilidade-1280x720-1-1024x576.png.webp" alt="imagem grafica demonstrativa sobre acessibilidade para diversas deficiencias">
</div>
  <br>
  <h3>Tabela de Alunos</h3>
  <br>
  <a href="/aula2/?controller=Professor&acao=salvar" class="btn btn-secondary"> Cadastrar professor</a>
  <br>
  <br>          
  <table class="table table-striped table-dark text-center">
    <thead>
      <tr>
        <th>Id</th>
        <th>Nome</th>
        <th>Idade</th>
      </tr>
    </thead>
    <tbody>
    <?php foreach ($professores as $professorAtual) { ?>
        <tr>
        <td> <?php echo $professorAtual ['id']; ?></td>
        <td> <?php echo $professorAtual ['nome']; ?></td>
        <td> <?php echo $professorAtual ['idade']; ?></td>      
        </tr>
    <?php } ?>
    </tbody>
  </table>
</div>
</body>
</html>

