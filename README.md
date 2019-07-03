# Projeto de Sistemas Embarcados: Simulação de controle de acesso de uma ponte levadiça, utilizando a placa BeagleBone

O código utilizado para controle é escrito em python, não necessitando de toolchain para geração de código de máquina, já que trata-se de uma linguagem interpretada, cujo interpretador é software default de distribuições linux, das quais o Debian, sistema operacional instalado na BeagleBone, faz parte.

Para execução deste código, basta clonar este repositório, abrir um terminal, e executar os seguintes comandos dentro da pasta em que ele se encontra:

```ssh 192.168.7.2 -l root```. Com isso, é solicitada ao usuário a senha para realizar a conexão. A senha padrão é ```temppwd```. Feito isso, estamos conectados ao terminal da placa. Devemos abrir outro terminal agora, navegar novamente para a pasta do repositório e executar: ```scp ponte.py debian@192.168.7.2:/home/debian/``` e retornando ao terminal conectado à placa, basta rodar com ```python ponte.py``` e o programa começará a execução.








Projeto Ponte levadiça

Sensores:
Sensor de barreira (fotoelétrico):
A detecção da altura crítica do barco para levantar a ponte levadiça será feita por meio de um sensor de barreira, também conhecido como fotoelétrico. Utilizaremos o W16 da marca SICK, que possui distanciamento máximo de 45m, com emissão de luz de led do tipo infravermelho.


Fotodiodo e receptor:
Utilizaremos um fotodiodo e um receptor em cada extremidade da ponte, para detectarmos o sentido do movimento, permitindo sua elevação.


Célula de Carga:
Para determinar a presença de carros em contato com a ponte, utilizaremos uma célula de carga de 50kg, que se comunicará com a placa a partir de jumpers.


Motores:
Servomotor Tower Pro MG995:
	Em cada uma das folhas da ponte, por meio de uma estrutura de transmissão de movimento (mecanismo quatro barras), estará conectado um servomotor, que desenvolve torque de stall de até 8.5 kgf·cm (4.8 V) ou 10 kgf·cm (6 V), tensão de 4.8 à 7.2 V.

	O servomotor recebe um sinal PWM da placa, que faz o controle do seu movimento. Além disso, sua energização será por meio de uma fonte de alimentação DC.


Motor DC:
Em cada entrada e saída haverá um motor DC operando as cancelas, que receberá sinal da placa BeagleBone, intermediado por um driver fornecido pelos professores (o mesmo usado no carro de controle remoto mostrado em sala).





Funcionamento:
A ponte será baseada no modelo basculante, com cancelas em suas extremidades movidas por motores DC; já o sistema de acionamento será movido por servomotores.

A partir dos estímulos captados pelos sensores dos tráfegos rodoviário e náutico, a ponte poderá estar dois estados; levantado e estático, e as cancelas em três estados: ambas abertas, uma aberta e a outra fechada, e ambas fechadas.

Caso o sensor de barreira seja acionado, a placa verificará se há algum carro na ponte através da célula de carga, detectando a presença, e dos fotodiodos e receptores, detectando por onde o carro veio (e assim descendo a cancela desta extremidade) e por onde ele sairá (descendo a cancela após detectada a saída).

A ascensão e descida das cancelas será determinada por contatos nas posições abaixadas e levantadas, que após acionados enviarão ou cessarão o sinal enviado aos motores DC.

Averiguada a saída do carro, a ponte mudará da posição estática até a posição levantada, por meio de uma contagem específica de passos do servomotor.

A ponte será abaixada a partir de um sinal de um botão do navio, mas para evitar acidentes, somente após certo período de tempo a ponte descerá com o sinal enviado do botão.

		
