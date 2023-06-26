function adicionar() {
    const tarefa = document.getElementById('tarefa').value;
    const li = document.createElement('li');
  
    if (tarefa !== '') {
      li.textContent = tarefa;
      const ul = document.getElementById('pendentes');
      ul.appendChild(li);
    } else {
      alert('Informe uma tarefa!');
    }
  
    const btnRemove = document.createElement('button');
    btnRemove.textContent = 'Excluir';
    btnRemove.type = 'button';
    btnRemove.style.marginLeft = '20px';
    btnRemove.style.color= '#FFF'
    btnRemove.style.width= '100px'
    btnRemove.style.height='30px'
    btnRemove.style.background = '#191818'
    btnRemove.style.borderRadius = '5px'
    btnRemove.addEventListener('click', function () {
      li.remove();
    });
    li.appendChild(btnRemove);
  
    const btnConcluido = document.createElement('button');
    btnConcluido.textContent = 'Concluído';
    btnConcluido.type = 'button';
    btnConcluido.style.marginLeft = '20px';
    btnConcluido.style.color= '#FFF'
    btnConcluido.style.width= '100px'
    btnConcluido.style.height='30px'
    btnConcluido.style.background = '#191818'
    btnConcluido.style.borderRadius = '5px'
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

  function manipulandoClasseSun(){
    const body = document.querySelector('body')
    body.classList.add('fundobranco')

  }
  
  function manipulandoClasseMoon(){
    const body = document.querySelector('body')
    body.classList.remove('fundobranco')

  }



