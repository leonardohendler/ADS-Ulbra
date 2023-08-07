function somar(){
    const num1= Number(document.getElementById("num1").value)
    const num2= Number(document.getElementById("num2").value)

    if (num1 != "" && num2 != ""){
        let soma = num1 + num2
        document.getElementById("result").innerHTML = `Resultado: ${soma}`
    }
    else{
        alert("Preencha todos os campos")
    }
}
function subtrair(){
    const num1= Number(document.getElementById("num1").value)
    const num2= Number(document.getElementById("num2").value)
    if (num1 != "" && num2 != ""){
        let subtracao = num1 - num2
        document.getElementById("result").innerHTML = `Resultado: ${subtracao}`
    }
    else{
        alert("Preencha todos os campos")
    }
}


function multiplicar(){
    const num1= Number(document.getElementById("num1").value)
    const num2= Number(document.getElementById("num2").value)
    if (num1 != "" && num2 != ""){
        let multiplicacao = num1 * num2
        document.getElementById("result").innerHTML = `Resultado: ${multiplicacao}`
    }
    else{
        alert("Preencha todos os campos")
    }
}


function dividir(){
    const num1= Number(document.getElementById("num1").value)
    const num2= Number(document.getElementById("num2").value)
    if (num1 != "" != 0 && num2 != "" != 0){
        let soma = num1 / num2
        document.getElementById("result").innerHTML = `Resultado: ${soma}`
    }
    else{
        alert("Preencha todos os campos")
        alert("Informe um valor diferente de 0")
    }
}

function limpar(){
    document.getElementById("num1").value = ""
    document.getElementById("num2").value = ""
    document.getElementById("result").innerHTML="Resultado:"
}
