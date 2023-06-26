function adicionar() {
    const tarefa = document.getElementById('tarefa').value;
    const li = document.createElement('li');
  
    if (tarefa !== '') {
      li.textContent = tarefa;
      const ol = document.getElementById('pendentes');
      ol.appendChild(li);
    } else {
      alert('Informe uma tarefa!');
    }
  
    const btnRemove = document.createElement('button');
    btnRemove.textContent = 'remover';
    btnRemove.type = 'button';
    btnRemove.style.marginLeft = '20px';
    btnRemove.addEventListener('click', function () {
      li.remove();
    });
    li.appendChild(btnRemove);
  
    const btnConcluido = document.createElement('button');
    btnConcluido.textContent = 'Concluído';
    btnConcluido.type = 'button';
    btnConcluido.style.marginLeft = '20px';
    btnConcluido.addEventListener('click', function () {
        concluido(li);
    });
    li.appendChild(btnConcluido);
  
    document.getElementById('tarefa').value = '';
    document.getElementById('tarefa').focus();
  }
  
  function concluido(li) {
    const concluidos = document.getElementById('concluidas');
    concluidos.appendChild(li); 
    
  }
  




