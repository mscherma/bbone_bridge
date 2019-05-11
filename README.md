# Projeto de Sistemas Embarcados: Simulação de controle de acesso de uma ponte levadiça, utilizando a placa BeagleBone

Necessitamos da toolchain para gerar código de máquina compatível com a BeagleBone; para isso, abrimos o terminal e executamos:

- sudo apt-get update
- sudo apt-get install gcc-arm-linux-gnueabihf
- sudo apt-get install g++-arm-linux-gnueabihf

Feito isso, basta executarmos o seguinte comando para compilar:

- arm-linux-gnueabihf-gcc main.c -o main