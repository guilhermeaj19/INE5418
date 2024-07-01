
# Espaço de Tuplas INE5418

Serviço de Descriptografia de Senhas em sha256

Zookeeper

Vá para o diretório do projeto

```bash
  cd T2
```

Instalar as dependências

```bash
  pip3 install -r requirements.txt
```

Inicializar os servidores

```bash
  source server.sh zk_start
```

Aplicação

Executar o archiver (vai guardar as senhas descriptografadas)

```bash
  python3 app_archiver.py
```

Executar 1 ou mais consumers (vai descriptografar as senhas)

```bash
  python3 app_consumer.py
```
  Coloque os endereços dos servidores Zookeeper. Por padrão é: 127.0.0.1:5551,127.0.0.1:5552,127.0.0.1:5553
  Pode alterar o endereço do archiver. Por padrão é: tcp://127.0.0.1:63000
  Clique em "Enviar" para ativar o consumer e deixar ele aguardando uma senha.

Executar 1 ou mais producers (envia as senhas pro zookeeper e indica o modo)

```bash
  python3 app_producer.py
```
  Coloque os endereços dos servidores Zookeeper. Por padrão é: 127.0.0.1:5551,127.0.0.1:5552,127.0.0.1:5553
  Selecione o arquivos com as senhas (há um passwords.txt como teste na pasta)
  Indique o modo:
    - Intervalos: testar de X a Y
    - Lista: se baseiar numa lista de senhas pré-estabelecida



  Coloque um nome de usuário e o endereço IP do Servidor
  Caso o servidor esteja na mesma máquina, pode colocar localhost ou 127.0.0.1
