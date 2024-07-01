
# Espaço de Tuplas INE5418

Serviço de Descriptografia de Senhas em sha256

## Zookeeper

### Vá para o diretório do projeto

```bash
  cd T2
```

### Instalar as dependências

```bash
  pip3 install -r requirements.txt
```

### Inicializar os servidores

```bash
  source server.sh zk_start
```

### Finalizar os servidores

```bash
  source server.sh zk_stop
```

## Aplicação

### Executar o archiver (vai guardar as senhas descriptografadas)

```bash
  python3 app_archiver.py
```

### Executar um consumidor (vai descriptografar as senhas)

```bash
  python3 app_consumer.py
```
  Coloque os endereços dos servidores Zookeeper. Por padrão é: 127.0.0.1:5551,127.0.0.1:5552,127.0.0.1:5553 <br />
  Pode alterar o endereço do archiver. Por padrão é: tcp://127.0.0.1:63000 <br />
  Clique em "Enviar" para ativar o consumer e deixar ele aguardando uma senha. <br />

### Executar um producer (envia as senhas pro zookeeper e indica o modo)

```bash
  python3 app_producer.py
```
  Coloque os endereços dos servidores Zookeeper. Por padrão é: 127.0.0.1:5551,127.0.0.1:5552,127.0.0.1:5553 <br />
  Selecione o arquivos com as senhas (há diretório password_files com arquivos de teste) <br />
  Indique o modo: <br />
    - Intervalos: testar de X a Y <br />
    - Lista: se baseiar numa lista de senhas pré-estabelecida <br />
