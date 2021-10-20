![Python](https://cafeinacodificada.com.br/wp-content/uploads/2018/04/Post1_pt21.png)
# Python Socket
Bem vindo! Espero que o conteúdo aqui apresentado lhe auxilie a entender melhor o funcionamento de um Socket e como implementá-lo em Python.

## O que é este repositório?
Este repositório é fruto de uma atividade avaliativa do curso de Análise e Desenvolvimento de Sistemas, na disciplina de Sistemas Distribuídos, ministrada pelo professor Eduardo Xavier. A intenção deste é explicar, na prática, o que é um socket e ensinar como implementá-lo utilizando a linguagem [Python](https://www.python.org/)

## Integrantes da equipe/contribuintes
- João Gabriel Santos Neves - matrícula UNIFACS: 042191010 - [Github](https://github.com/jgsneves)

## Requerimentos Mínimos de Software
O que você precisa fazer para executar este software

## Instalação do Git
Caso você deseje baixar os arquivos deste respositório via git, você precisa ter o [git](https://git-scm.com/) caso deseje clonar este repositório para um diretório local. Siga o passo a passo abaixo a depender de qual sistema operacional você utilize:

### Windows
Faça o download do instalador na página oficial do git e instale em sua máquina normalmente.

### GNU/Linux
Siga este [manual](https://git-scm.com/download/linux) do site oficial do git

### MacOS
Siga este [manual](https://git-scm.com/download/mac) do site oficial do git

## Copiando este repositório para um diretório local
Há duas formas de fazer o download deste respositório:

### Download do ZIP
Dentro da [página deste repositório no github](https://github.com/jgsneves/python-socket) tem a opção de fazer download de um arquivo zipado, com todos os módulos py dentro dele, conforme imagem:
![Download Zip do github](https://br.atsit.in/wp-content/uploads/2021/06/como-baixar-arquivos-e-visualizar-o-codigo-do-github-9.png)

### Download via git
1) abra um terminal (powershell, cmd ou qualquer outro terminal do seu sistema operacional);

2) crie uma diretório (pasta) dentro do seu disco rígido através do comando:
```mkdir <nome_da_pasta>```

3) clone este repositório para seu diretório local:
Usando HTTPS:
```git clone https://github.com/jgsneves/python-socket.git```
Usando SSH:
```git clone git@github.com:jgsneves/python-socket.git```

## Instalação do Python
Você precisa ter o [Python](https://www.python.org/) instalado em sua máquina.

### Windows
Caso você utilize o sistema operacional windows, dirija-se ao site oficial da linguagem, faça download do compilador do `python3`.

### GNU/Linux
Siga as instruções contidas neste [manual](https://python.org.br/instalacao-linux/) criado pela python brasil.

### MacOS
Siga as instruções contidas neste [manual](https://python.org.br/instalacao-mac/) criado pela python brasil.

## Execução dos arquivos python
Depois do compilador Python instalado, executaremos cada arquivo do servidor e dos clientes, usando o seguinte comando:

```python <path_do_arquivo>```

Abra um terminal para cada socket (um para professor, outro para aluno e outro para servidor).

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
Falar de concorrência é falar de paralelismo. É a capacidade do computador processar mais de um dado ao mesmo tempo. Aqui não se fala apenas de velocidade de processamento (afinal, com o multithread, o computador conseguiria realizar mais de uma tarefa ao mesmo tempo, realizando aquilo que se propõe de forma mais célere), mas também na possibilidade de criar programas básicos.

Em um programa muito básico, onde todas as instruções ocorrem de cima para baixo, em sequência, o multithread não faz falta. O computador executa todas as instruções e chega ao fim. Porém, quando precisamos criar programas um pouco mais complexos, como é o caso desse repositório, precisamos que o computador reserve atenção a mais de uma execução (aqui, nós temos um servidor e 2 clientes conectando a ele ao mesmo tempo).

Para escutar dois clientes ao mesmo tempo, por exemplo, o processador deve reservar uma thread para cada requisição. Caso não houvesse o multithread, não seria possível conectar mais de um cliente no mesmo servidor, e ao mesmo tempo.

## Diferença entre ```thread``` e ```process```
Os dois referem-se a processamento. Porém, um `process` tem uma ou mais `threads`. O processo aloca recursos computacionais (processamento, memória, etc) para realizar uma ou mais `threads`, enquanto que esta última é uma unidade básica de processamento. Quando executamos um script python, por exemplo, utilizamos uma thread de um processo.

Nesse nosso repositório, criamos uma `thread` para processar o script e uma para cada conexão de cada cliente (professor e aluno). Caso não houvesse a possibilidade de fazer esse paralelismo, quando o professor se conectasse, seria necessário encerrar a conexão deste para que qualquer aluno pudesse se conectar e registrar sua presença. Não é esse o comportamento esperado.

## Vamos pro código!
Agora que abordamos os conceitos básicos, vamos para o código! 

### Estrutura de pastas (arquitetura)
```javascript
src--|
    clients---|
        student.py      //implementação do cliente-estudante
        teacher.py      //implementação do cliente-professor
    models----|
        classtype.py    //modelo de uma turma/classe
    server----|
        server.py       //implementação do servidor
    services--|
        service.py      //implementação do serviço de controle de chamada
    index.py            //o script que deve ser executado para abrir o servidor
```

### Explicando a aplicação
Cada equipe deve criar um aplicativo de CHAMADA para uma turma de alunos utilizando sockets. O aplicativo deve funcionar da seguinte maneira:

    • Há dois tipos de clientes: professor e aluno.
    • Um professor pode iniciar ou finalizar o processo de chamada.
    • Um aluno envia seu registro de presença em uma chamada ativa.
    • O servidor hospeda a lista de alunos que estão presentes em cada chamada e 
    atende clientes (alunos e professores).

Não há necessidade de implementar uma interface gráfica. Uma interface textual, desde que compreensível, pode ser usada sem que isso prejudique a pontuação do trabalho.

A aplicação pode ser desenvolvida em C++, Java, GoLang, Dart ou Python. As equipes devem enviar ao professor um relatório com o seguinte conteúdo:

    • Apresentação dos componentes da equipe
    • Descrição dos requerimentos mínimos de software necessários para execução da aplicação 
    (o que deve estar instalado no cliente e no servidor para a aplicação funcionar)
    • Todos os códigos-fonte da aplicação
    • Instruções de instalação da aplicação

### Detalhes das regras de negócio
Detalhes que devem estar presentes na implementação do projeto.

#### Cliente tipo “Professor”
• Dispara o início da chamada informando a identificação numérica da turma e recebe do servidor uma confirmação contendo a data e hora do início da chamada.

• Dispara o encerramento da chamada informando a identificação numérica da turma e recebe do servidor a data e a hora de encerramento da chamada, além de um vetor contendo todas as matrículas de alunos que responderam a chamada. Após o recebimento, deve exibir (na console da aplicação) uma lista
contendo as matrículas (alunos presentes) que recebeu.

#### Cliente tipo “Aluno”
• Responde à chamada enviando sua matrícula e a identificação numérica de sua turma. Recebe como resposta a identificação numérica da turma, a data e a hora em que sua presença foi registrada pelo servidor.

• Se a turma a qual o aluno enviou seu registro de presença não estiver com a chamada iniciada pelo professor, o aluno recebe a mesma resposta, mas com a identificação da turma zerada (indicando assim, que o registro de presença foi recusado pelo servidor).

#### Servidor de Chamada
• Aguarda solicitações de clientes (escuta)

• Recebe solicitação e identifica o tipo:

    • Se for um início de chamada se prepara para armazenar as matrículas de alunos que responderão 
    a chamada da turma informada e retorna confirmação adequada (data e hora) ao professor. 
    Lembre-se: pode haver mais de um professor fazendo chamada ao mesmo tempo para turmas diferentes. 
    Cabe à equipe implementar uma solução para isso.

    • Se for um encerramento de chamada retorna ao professor a confirmação adequada 
    (data, hora e vetor de matrículas) ao professor e apaga as informações referentes a chamada da 
    turma que foi encerrada. Lembre-se que podem haver outras turmas ainda fazendo chamada e isso não
    pode sofrer interferência. Cabe à equipe implementar uma solução para isso.

    • Se for um registro de presença, verifica se existe uma chamada ativa para a turma informada pelo aluno.

• Caso a chamada esteja ativa (professor já iniciou, mas não encerrou), insere a matrícula do aluno no armazenamento de alunos presentes e devolve a
confirmação adequada ao aluno (identificação da turma, a data e a hora em que a presença foi registrada).

• Caso a chamada não exista (professor não iniciou ou já encerrou a chamada da turma) apenas devolve a resposta adequada ao aluno ( zero em lugar da identificação da turma, a data e a hora em que a presença foi negada).

### Componentes da aplicação

#### **:gear: index.py**
É o script que deve ser executado para rodar o `server`. Rodar o comando na pasta root do projeto:
```
python src/index.py
```
No mais, o arquivo foi implementado da seguinte forma:

```python
from server.server import Server
from services.service import Service

class_service = Service()

new_server = Server(class_service)

new_server.run()
```
Ele importa o serviço e passa sua instância no construtor do servidor. Após o instanciamento do server, executa o método `run()` para rodar o servidor.

#### **:gear: src/clients/student.py**
Implementação do cliente de estudante.

```python
import socket

PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())
ADDRESS = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)
print('''
---------------[BEM VINDO]------------------

Olá Aluno,
Bem vindo ao sistema de registro de presença.

---------------------------------------------
''')

msg = ''
client_code = 'student'

def get_identified_msg(msg, client_code):
    return f'{msg},{client_code}'

while True:
    user_number = input('Informe seu número de matrícula: ')
    user_class = input('Informe o número da matéria em que deseja registrar presença: ')
    msg = str(user_number + '/' + user_class)
    encoded_package = str.encode(get_identified_msg(msg, client_code))
    client.send(encoded_package)
    response = client.recv(1024)
    decoded_response = response.decode()
    print(decoded_response)

```
Este módulo implementa um `socket` com as configuraçõe do servidor (tem que ser um match perfeito entre porta, endereço e tipo de socket). Depois solicita dois `inputs` do usuário: 1) número de matrícula e 2) número da matéria que ele deseja registrar a presença. Depois os `inputs` são parseados em uma `string` que os separa por uma barra `/`.

Após codificar esta `string` em `bytes` (o socket apenas aceita trafegar dados em `bytes`), o envia para o servidor e fica aguardando o feeedback (a resposta) do mesmo. Após a chegada da resposta, esta é decodificada de `bytes` para `string` e printada na tela.

Para executar este `client`, basta executar o seguinte comando da raiz do projeto:
```
python src/clients/student.py
```

#### **:gear: src/clients/teacher.py**
TO DO

#### **:gear: src/models/classtype.py**
TO DO

#### **:gear: src/server/server.py**
TO DO

#### **:gear: src/services/service.py**
TO DO

## Referências
- [Diferença entre thread e process](https://stackoverflow.com/questions/200469/what-is-the-difference-between-a-process-and-a-thread)
- [Como usar processamento concorrente (multithread) com Python](https://stackoverflow.com/questions/23828264/how-to-make-a-simple-multithreaded-socket-server-in-python-that-remembers-client)
- [Básico de Socket - wiki](https://wiki.python.org.br/SocketBasico)
- [Criar um socket básico em python](https://www.youtube.com/watch?v=vbUuJ2_6wqs) - [@bosontreina](https://twitter.com/bosontreina)
- [HOWTO: socket em python](https://docs.python.org/pt-br/3/howto/sockets.html)
- [Python Socket Programming Tutorial](https://www.youtube.com/watch?v=3QiPPX-KeSc) - [@TechWithTimm](https://twitter.com/TechWithTimm)
- [Whats the OSI model?](https://www.freecodecamp.org/news/osi-model-computer-networking-for-beginners/)
