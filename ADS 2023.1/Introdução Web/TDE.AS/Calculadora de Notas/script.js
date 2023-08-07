function calcular(){
    const ap1= Number(document.getElementById("ap1").value)
    const ap2= Number(document.getElementById("ap2").value)
    const as= Number(document.getElementById("as").value)
        let calculo = ap1 + ap2 + as

        if (calculo >=6){
            document.getElementById("nota").innerHTML = `Nota:${calculo}! Aprovado. Parabéns. `
        }
        else{
            document.getElementById("nota").innerHTML = `Nota:${calculo}! Reprovado. Reforce seus estudos para realização da AF.`
        }  
}

function verificaAp1(){
    const ap1= Number(document.getElementById("ap1").value)
    if (ap1 <0 || ap1 >1.5){
        document.getElementById("ap1").value =''
        alert ("Nota invalida.Digite uma nota entre 0 e 1,5")
        document.getElementById("ap1").focus()

    }
}
function verificaAp2(){
    const ap2= Number(document.getElementById("ap2").value)
    if (ap2 <0 || ap2 >1.5){
        document.getElementById("ap2").value =''
        alert ("Nota invalida.Digite uma nota entre 0 e 1,5")
        document.getElementById("ap2").focus()

    }
    
}
function verificaAs(){
    const as= Number(document.getElementById("as").value)
    if (as <0 || as >6){
        document.getElementById("as").value =''
        alert ("Nota invalida.Digite uma nota entre 0 e 6")
        document.getElementById("as").focus()

    }
    
}