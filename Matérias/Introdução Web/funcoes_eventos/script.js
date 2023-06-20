function alo(){
    alert("Alo")
}
function olaNome(nome){
    alert(`Ola ${nome} seja bem vindo ao curso`)
}
function saudacao(){
    const nome = document.getElementById("nome").value
    alert(`Ola ${nome}, como voce está?`)
}
function mouseSobre(){
    alert(`O mouse esta encima!`)
}
function mouseFora(){
    alert(`O mouse saiu`)
}
function textoMudou(){
    alert(`Texto mudou`)
}
function enFoco(){
    const user = document.getElementById('user')
    user.style.border = '5px blue solid'
    user.style.backgroundColor = 'black'
}
function perdeuFoco(){
    const user = document.getElementById("user")
    user.style.border = '1px black solid'
    user.style.backgroundColor = 'white'
}