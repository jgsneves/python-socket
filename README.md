![Python](https://cafeinacodificada.com.br/wp-content/uploads/2018/04/Post1_pt21.png)
# Python Socket

## O que é este repositório?
Este repositório tem o objetivo de explicar, na prática, o que é um socket e ensinar como implementá-lo utilizando o [Python](https://www.python.org/)

## O que é um socket?
O ```socket``` é um nó. É um ponto de comunicação entre dois sistemas distribuídos. Sistema é um software e sistema distribuído é uma aplicação que somente é completa com a utilização de mais de um programa localizado em máquinas diferentes (claro que podemos simular duas localizações distintas em uma mesma máquina, como é o caso dessa aplicação deste respositório). 

É legal pensar o ```socket``` como um container, dentro de um navio. Este navio sai de um ponto A para o ponto B e o container contém uma mensagem que precisamos trafegar entre os pontos A e B. Geralmente utilizamos o ```socket``` em conjunto com o protocolo IP, que é responsável por endereçar toda máquina dentro de uma rede. O IP é o endereço numérico de toda máquina conectada a uma rede. Assim, cada ```socket``` possui, como metadado, o endereço de ip, a porta de comunicação e protocolo de comunicação utilizado dos pontos A e B.

> OBS: metadado é um dado que não faz parte do conteúdo de uma informação, apenas representando uma informação complementar. Por exemplo: em uma carta, o seu conteúdo é um dado e as informações de endereço do remetente e do destinatário são metadados. 

## Onde utilizamos o socket?

## O que é TCP/IP e UDP?

## O que é concorrência (multithread)?

## Diferença entre ```thread``` e ```process```

## Vamos pro código

### Explicando a aplicação

### Estrutura de pastas (arquitetura)

### Componentes

## Referência
- [Diferença entre thread e process](https://stackoverflow.com/questions/200469/what-is-the-difference-between-a-process-and-a-thread)
- [Como usar processamento concorrente (multithread) com Python](https://stackoverflow.com/questions/23828264/how-to-make-a-simple-multithreaded-socket-server-in-python-that-remembers-client)
- [Básico de Socket - wiki](https://wiki.python.org.br/SocketBasico)
- [Criar um socket básico em python](https://www.youtube.com/watch?v=vbUuJ2_6wqs) - [@bosontreina](https://twitter.com/bosontreina)
- [HOWTO: socket em python](https://docs.python.org/pt-br/3/howto/sockets.html)
- [Python Socket Programming Tutorial](https://www.youtube.com/watch?v=3QiPPX-KeSc) - [@TechWithTimm](https://twitter.com/TechWithTimm)
