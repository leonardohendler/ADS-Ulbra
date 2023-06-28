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
    // const icon= document.createElement("i")
    // icon.classList.add("gg-trash")
    // btnRemove.appendChild(icon)
    btnRemove.textContent = 'Excluir';
    btnRemove.type = 'button';
    btnRemove.style.marginLeft = '20px';
    btnRemove.style.color= '#FFF'
    btnRemove.style.width= '70px'
    btnRemove.style.height='25px'
    btnRemove.style.background = '#191818'
    btnRemove.style.color='#d8d1d183'
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
    btnConcluido.style.width= '75px'
    btnConcluido.style.height='25px'
    btnConcluido.style.textAlign='center'
    btnConcluido.style.background = '#191818'
    btnConcluido.style.color='#d8d1d183'
    btnConcluido.style.borderRadius = '5px'
    btnConcluido.addEventListener('click', function () {
        concluido(li);
    });
    li.appendChild(btnConcluido);

    

    document.getElementById('tarefa').value = '';
    document.getElementById('tarefa').focus();

    li.style.margin='25px'
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



