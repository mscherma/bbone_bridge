# Projeto de Sistemas Embarcados: Simulação de controle de acesso de uma ponte levadiça, utilizando a placa BeagleBone

O código utilizado para controle é escrito em python, não necessitando de toolchain para geração de código de máquina, já que trata-se de uma linguagem interpretada, cujo interpretador é software default de distribuições linux, das quais o Debian, sistema operacional instalado na BeagleBone faz parte.

Para execução deste código, basta clonar este repositório, abrir um terminal, e executar os seguintes comandos dentro da pasta em que ele se encontra:

```ssh 192.168.7.2 -l root```. Com isso, é solicitada ao usuário a senha para realizar a conexão. A senha padrão é ```temppwd```. Feito isso, estamos conectados ao terminal da placa. Devemos abrir outro terminal agora, navegar novamente para a pasta do repositório e executar: ```scp Ponte.py debian@192.168.7.2:/home/debian/``` e retornando ao terminal conectado à placa, basta rodar com ```python Ponte.py``` e o programa começará a execução.