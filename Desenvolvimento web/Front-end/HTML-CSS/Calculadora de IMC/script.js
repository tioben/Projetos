
const calculatorButton = document.getElementById('calculator-button');
document.getElementById('imc-number').textContent = 0;
document.getElementById('imc-text').textContent = '';

calculatorButton.addEventListener('click', function () {
    const weight = document.getElementById('weight-value').value;
    const height = document.getElementById('height-value').value;

    function calculator(weight, height){
        const imc = weight/(height**2);
        let string = '';
        if (imc < 18.5) {
            string = 'Abaixo do peso'

        }else if (18.5 <= imc && imc < 25) {
            string = 'Peso ideal';

        }else if (25 <= imc && imc < 30){
            string = 'Levemente acima do peso';

        }else if (30 <= imc && imc < 35){
            string = 'Obesidade grau I';
        
        }else if (35 <= imc && imc < 40){
            string = 'Obesidade grau II (Severa)';
        
        }else if (40 <= imc){
            string = 'Obesidade grau III (Mórbida)';
        }

        document.getElementById('imc-number').textContent = imc.toFixed(2);
        document.getElementById('imc-text').textContent = string;
    }

    calculator(weight, height);
});


console.log(weight.value);