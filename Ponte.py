import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
from time import sleep

#####################################################################
# Definição da pinagem utilizada para controle. Descrição:
#
# serpino: Pino utilizado na interface PWM, para controle do
# motor do tipo servomotor Tower Pro MG
#
# psen: Pino do tipo INPUT, que recebe o sinal do sensor de
# barreira responsável pela detecção de embarcação
#
# led: Pino responsável pelo controle dos leds de indicação de 
# embarcação, conectado também ao buzzer para acionamento
# simultâneo deste.
#
# in1, in2, in3, in4: Pinos de entrada dos motores a serem
# controlados pelo driver L298N. Motores DC utilizam 2 pinos,
# enquanto motores de passo utilizam os 4 pinos. Assim, cada
# driver controla um motor de passo ou dois motores DC. Neste
# caso, os pinos in1 a in4 são utilizados no motor de passo.
#
# Mais informações em: 
# https://www.arduinoecia.com.br/2014/08/ponte-h-l298n-motor-de-passo.html
#
# dc3, dc4: Análogo aos pinos in1 a in4, porém agora, para o
# controle do motor DC utilizado. Observe, portanto, que apenas
# dois foram necessários.
#
# pwmdc: Pino utilizado na entrada Enable, que ao mandar um
# sinal PWM, é responsável pelo controle de velocidade do motor.
#####################################################################

serpino = "P9_14"
psen = "P9_15"
led = "P9_12"

in1 = "P8_8"
in2 = "P8_10"
in3 = "P8_12"
in4 = "P8_14"

dc4 = "P8_7"
dc3 = "P8_9"
pwmdc = "P8_13"

#####################################################################
# Declaração de alguns parâmetros de controle do projeto:
#
# tp => Tempo de sleep entre o chaveamento das bobinas.
# Quanto maior a espera para chavear, maior o tempo para dar um
# passo. Sendo assim, a alteração desse parâmetro influencia na
# velocidade do motor de passo.
#
# dr => Quantidade de passos dados. Os motores de passo estão
# acoplados ao mecanismo de abertura e fechamento da ponte.
# Assim, mediante testes, determinamos que 50 passos seriam
# suficientes para a abertura de um ângulo razoável da ponte
#
# ct => Flag de controle para o controle da ponte. A mudança
# para 0 significa que ela deve abrir, e para 1, indica que 
# a ponte deve fechar. Inicializada como 2, para não assumir
# nenhum estado default.
#####################################################################

tp = 0.01
dr = 50
ct = 2


#####################################################################
# Inicialização das pinagens supracitadas.
#
# Todos os pinos exceto o sensor e o PWM são do tipo OUTPUT,
# ou seja, em que é possível fazer escrita. O pino do sensor é
# do tipo INPUT, portanto, é possível fazer apenas leitura.
#
# O pino de PWM é inicializado de forma diferente: Recebe o pino
# em que está conectado, o duty cycle e a frequência da onda
# que será modulada, respectivamente. O duty cycle foi levantado
# de forma empírica, e corresponde aos seguintes estados:
# 3.45: Cancela na posição aberta
# 1.35: Cancela na posição fechada
#####################################################################

GPIO.setup(dc4, GPIO.OUT)
GPIO.setup(dc3, GPIO.OUT)

PWM.start(serpino, 3.45, 25)
GPIO.setup(psen, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)


##############################################################
# Aqui reside a lógica principal do programa, dividida
# em 3 blocos:
#
# Sensor == 0 && ct == 1 => Há presença, e a ponte está fechada
# Nesse caso, ela deve abrir.
#
# Sensor == 0 && ct == 0 => Há presença, e a ponte está aberta
# Nesse caso, ela fica em loop , pois não é seguro fechá-la,
# caso tenha uma possível embarcação embaixo. Assim, o loop
# será quebrado apenas quando a presença não for mais detectada,
# assim o fechamento será feito de forma segura
#
# Sensor == 1 && ct == 0 => Não há presença, e a ponte está aberta
# Nesse caso, ela deve fechar.
#
# Sensor == 1 && ct == 1 => Não há presença, e a ponte está fechada
# Nada acontece, portanto este caso não é contemplado.
##############################################################

while(True):
    
    #Primeiro caso. Abra a ponte
    if(GPIO.input(psen) == 0 and ct != 0):
        #Altera a flag de estado
        ct = 0
        
        #Pisca um LED por 6 vezes, com intervalo de 0.5 segundo entre apagar e acender.
        #Vale lembrar que o buzzer está na mesma porta, assim ele apitará exatamente
        #na mesma frequência, e pelo mesmo tanto de vezes.
        for i in range(6):
            GPIO.output(led, GPIO.LOW)
            sleep(.5)
            GPIO.output(led, GPIO.HIGH)
            sleep(.5)
        
        #Apaga o LED e cessa o buzzer
        GPIO.output(led, GPIO.LOW)

        #A ponte abriu, portanto as cancelas devem ser fechadas para impedir fluxo de veículos

        #Cancela controlada pelo servo.
        PWM.set_duty_cycle(serpino, 1.35)
	
        #Cancela controlada pelo motor DC.
        #Setamos suas configurações iniciais e inicializamos seu PWM.
        GPIO.output(dc4, GPIO.LOW)
        GPIO.output(dc3, GPIO.LOW)
        PWM.start(pwmdc, 100, 500)
        
        #Gire o motor na direção de fechar a cancela. O tempo de espera foi calibrado de forma a
        #obter a angulação correta no fechamento.
        GPIO.output(dc4, GPIO.LOW)
        GPIO.output(dc3, GPIO.HIGH)
        sleep(.545)

        #Pare o motor.
        GPIO.output(dc4, GPIO.LOW)
        GPIO.output(dc3, GPIO.LOW)

        #Observe que o controle do servo é feito via posição, cessando o movimento quando a posição
        #é atingida. O motor DC não. Portanto, sua parada deve ser feita de forma manual.        

        #Espere e gire os motores de passo na direção de efetivamente abrir a ponte. Espere novamente
        sleep(3)

        for i in range(dr):
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            sleep(tp)

            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            sleep(tp)

            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            GPIO.output(in3, GPIO.HIGH)
            GPIO.output(in4, GPIO.LOW)
            sleep(tp)

            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            GPIO.output(in3, GPIO.HIGH)
            GPIO.output(in4, GPIO.LOW)
            sleep(tp)

        sleep(8)
	
    #Segundo caso, loop até que a presença suma.
    while(GPIO.input(psen) == 0 and ct == 0):
		sleep(0.1)

    #Terceiro caso, feche a ponte.
    if(GPIO.input(psen) == 1 and ct == 0):
        #Altera de volta a flag de estado.
        ct = 1

        #Para o fechamento não há LEDs e buzzer. Então executamos diretamente a rotina
        #para os motores de passo. Observe que os estados lógicos escritos nos pinos 
        #são os opostos para quando a ponte se abre. Isso faz com que se inverta o sentido de rotação.
        for i in range(dr):
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            sleep(tp)

            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            sleep(tp)

            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            GPIO.output(in3, GPIO.HIGH)
            GPIO.output(in4, GPIO.LOW)
            sleep(tp)

            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            GPIO.output(in3, GPIO.HIGH)
            GPIO.output(in4, GPIO.LOW)
            sleep(tp)

        sleep(4)

        #Abra a cancela controlada pelo servo.
        PWM.set_duty_cycle(serpino, 3.45)	

        #Abra a cancela controlada pelo motor DC. Gire no sentido correto durante o tempo de espera
        #A seguir, pare o motor.
        GPIO.output(dc4, GPIO.HIGH)
        GPIO.output(dc3, GPIO.LOW)
        sleep(.545)

        GPIO.output(dc4, GPIO.LOW)
        GPIO.output(dc3, GPIO.LOW)

        #O programa retorna ao início, repetindo todo o funcionamento descrito, enquanto estiver rodando.