![Python](https://cafeinacodificada.com.br/wp-content/uploads/2018/04/Post1_pt21.png)
# Python Socket
Bem vindo! Espero que o conteúdo aqui apresentado lhe auxilie a entender melhor o funcionamento de um Socket e como implementá-lo em Python.

## O que é este repositório?
Este repositório é fruto de uma atividade avaliativa do curso de Análise e Desenvolvimento de Sistemas, na disciplina de Sistemas Distribuídos, ministrada pelo professor Eduardo Xavier. A intenção deste é explicar, na prática, o que é um socket e ensinar como implementá-lo utilizando a linguagem [Python](https://www.python.org/)

## O que é um socket?
O `socket` é um nó. É um ponto de comunicação entre dois sistemas distribuídos. Sistema é um software e sistema distribuído é uma aplicação que somente é completa com a utilização de mais de um programa localizado em máquinas diferentes (claro que podemos simular duas localizações distintas em uma mesma máquina, como é o caso dessa aplicação deste respositório). 

É legal pensar o ```socket``` como um container, dentro de um navio. Este navio sai de um ponto A para o ponto B e o container contém uma mensagem que precisamos trafegar entre os pontos A e B. Geralmente utilizamos o ```socket``` em conjunto com o protocolo IP, que é responsável por endereçar toda máquina dentro de uma rede. O IP é o endereço numérico de toda máquina conectada a uma rede. Assim, cada ```socket``` possui, como metadado, o endereço de ip, a porta de comunicação e protocolo de comunicação utilizado dos pontos A e B.

> OBS: metadado é um dado que não faz parte do conteúdo de uma informação, apenas representando uma informação complementar. Por exemplo: em uma carta, o seu conteúdo é um dado e as informações de endereço do remetente e do destinatário são metadados. 

## Onde utilizamos o socket?
Bom, utilizamos o socket em praticamente toda a internet. Praticamente toda a internet é baseada no modelo [cliente/servidor](https://www.tecmundo.com.br/internet/982-o-que-e-cliente-servidor-.htm). Então, quando você entra em qualquer site de internet, por baixo dos panos, você está utilizando o web socket.

## O que é TCP/IP e UDP?
Basicamente, entendemos que o `socket` é um conteiner dentro de um navio. O mapa que diz a rota que o navio deve percorrer para chegar do ponto A ao B é o protocolo IP. O navio onde esse container está trafegando é um `pacote do tipo TCP ou UDP`. Basicamente, o navio é do tipo TCP ou UDP. Os protocolos TCP e UDP são basicamente formas de trafegar pacotes, a maneira como carregamos a informação (com um pacote) através da rede. O protocolo TCP é um protocolo baseado na `confiança`, que exige a confirmação de chegada da informação, enquanto que o UDP é baseado na performance e velocidade, não se importando com perdas de informação no tráfego.

A imagem abaixo ilustra bem onde os protocolos TCP/UDP agem nesse fluxo de informação:
![Osi Models](https://www.freecodecamp.org/news/content/images/2021/10/osi-model-layers.png)

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
- [Whats the OSI model?](https://www.freecodecamp.org/news/osi-model-computer-networking-for-beginners/)
