function exercise_1() {
    let num = Number(prompt("Digite um numero"));
    let num1 = Number(prompt("Digite outro numero"));

    let calculo = num * num1;

    alert(` Resultado do calculo apresentado é: ${calculo}  `)
    return

}

function exercise_2() {
    let num = Number(prompt("Digite um numero"));
    if (num % 2 == 0 && num > 0) {
        alert("O numero é Par!")
        alert("O numero é positivo")
    }
    else if (num % 2 == 0 && num < 0) {
        alert("O numero é Par!")
        alert("O numero é negativo")
    }
    else {
        alert("O numero é impar!")
    }
    return
}

function exercise_3() {

    let nome = prompt("Digite seu nome");
    let idade = prompt("Digite sua idade!");

    if (idade >= 18) {
        alert(`${nome} você tem ${idade}, é maior de idade`)
    }
    else {
        alert(`${nome} você tem ${idade}, é menor de idade`)
    }
    return
}

function exercise_4() {

    let num = Number(prompt("Digite um numero!"));
    console.log("Tabuada de " + num);
    for (let i = 1; i <= 10; i++) {
        let resultado = num * i
        console.log(`${num} x ${i} = ${resultado}`)
    }

    return
}

function exercise_5() {
    let nota1 = Number(prompt("Informe uma nota:"));
    let nota2 = Number(prompt("Informe uma nota:"));
    let nota3 = Number(prompt("Informe uma nota:"));

    let media = (nota1 + nota2 + nota3) / 3;

    if (media >= 6) {
        alert(`Aprovado! ${media}`)
    }
    else {
        alert("REPROVADO")
    }
    return
}

function exercise_6() {
    let num = Number(prompt("Digite um numero"));
    switch (num) {
        case 1:
            alert("Domingo")
            break;
        case 2:
            alert("Segunda-feira")
            break;
        case 3:
            alert("Terça-feira")
            break;
        case 4:
            alert("Quarta-feira")
            break;
        case 5:
            alert("Quinta-feira")
            break;
        case 6:
            alert("Sexta-feira")
            break;
        case 7:
            alert("Sábado")
            break;
        default:
            alert("Digite um numero de 1 a 7!")

    }
    return
}

function exercise_7() {

    let num = 0;

    for (let i = 0; i <= 100; i++) {
        if (i % 3 === 0) {
            num += i;
        }
    }

    console.log(`A soma dos numeros multiplos de 3 entre 0 e 100 são: ${num}`)
    return
}

function exercise_8() {
    let soma = 0;
    let quantidade = 0;
    while (true) {
        const num = Number(prompt("Digite um numero inteiro, ou um numero negativo para sair"));
        if (num < 0) {
            break
        }


        soma += num;
        quantidade++;

    }

    if (quantidade === 0) {
        alert("Nenhum número foi digitado.");
    }
    else {
        const media = soma / quantidade;
        alert("A média dos números digitados é: " + media);
    }
    return
}


function calcula() {

    document.addEventListener('click', (event) => {
        const el = event.target;
        if(el.classList.contains('btn1')) exercise_1();
        if(el.classList.contains('btn2')) exercise_2();
        if(el.classList.contains('btn3')) exercise_3();
        if(el.classList.contains('btn4')) exercise_4();
        if(el.classList.contains('btn5')) exercise_5();
        if(el.classList.contains('btn6')) exercise_6();
        if(el.classList.contains('btn7')) exercise_7();
        if(el.classList.contains('btn8')) exercise_8();
    })

}