# Project Hermes
Project Hermes é (um dia vai ser) um sistema de rastreamento, telemetria e multimídia veicular projetado para Raspberry

### Hardware
- Raspberry Pi 4 Model B
- Ublox Neo 6m

![1_s06WPQoV6DVHDmgAGRy-3g](https://user-images.githubusercontent.com/54728889/177448944-284540b9-5988-4507-9144-a4adfe348ae7.png)

### OS
Rapberry Pi OS Legacy (2022-04-04)

## Configuração GPS

Certifique-se de que o sistema esteja atualizado
```sh
sudo apt update
sudo apt upgrade
```

Primeiro é preciso verificar as opções de boot para se certificar de que a porta serial não está em uso.
Acesse o arquivo ```/boot/cmdline.txt``` com o comando abaixo e verifique se existe somente uma entrada ```console=``` e que ela seja somente ```console=tty1```
```sh
sudo nano /boot/cmdline.txt
```

Exemplo de como estava
```
console=serial0,115200 console=tty1 root=PARTUUID=821cc72d-02 rootfstype=ext4 fsck.repair=yes rootwait
```

Como deve ficar
```
console=tty1 root=PARTUUID=821cc72d-02 rootfstype=ext4 fsck.repair=yes rootwait
```

Agora acesse o arquivo ```/boot/config.txt```
```sh
sudo nano /boot/config.txt
```

Adicione as seguintes linhas ao final do arquivo
```
dtparam=spi=on
dtoverlay=pi3-disable-bt
core_freq=250
enable_uart=1
force_turbo=1
```

Reinicie o Raspberry
```sh
sudo reboot
```

Utilize os seguintes comandos para desativar o serviço de "terminal"
```sh
sudo systemctl stop serial-getty@ttyAMA0.service
sudo systemctl disable serial-getty@ttyAMA0.service
```

Se tudo deu certo até aqui, ao executar ```sudo cat /dev/ttyAMA0``` você deve ter um retorno parecido com
```
$GPGGA,015415.00,2319.27218,S,05132.96098,W,1,05,1.85,729.5,M,-0.7,M,,*41
$GPGSA,A,3,29,05,15,18,26,,,,,,,,3.00,1.85,2.35*0E
$GPGSV,3,1,11,05,22,137,18,10,20,341,,12,11,033,13,15,16,072,15*74
$GPGSV,3,2,11,16,04,217,20,18,61,211,25,23,49,358,16,25,50,020,*73
$GPGSV,3,3,11,26,30,225,25,29,48,136,20,31,21,283,*45
$GPGLL,2319.27218,S,05132.96098,W,015415.00,A,A*6E
$GPRMC,015416.00,A,2319.27227,S,05132.96096,W,0.601,,060722,,,A*70
$GPVTG,,T,,M,0.601,N,1.112,K,A*27
$GPGGA,015416.00,2319.27227,S,05132.96096,W,1,05,1.85,729.7,M,-0.7,M,,*42
$GPGSA,A,3,29,05,15,18,26,,,,,,,,3.00,1.85,2.35*0
$GPGSV,3,1,11,05,22,137,18,10,20,341,,12,11,033,12,15,16,073,14*7
$GPGSV,3,2,11,16,04,217,20,18,61,211,25,23,49,358,15,25,50,020,*70
$GPGSV,3,3,11,26,30,225,25,29,48,136,20,31,21,283,*45     
```

Instale os pacotes do GPSD
```sh
sudo apt-get install gpsd gpsd-clients python-gps
```

Para configurar o início do serviço do gpsd corretamente abra o arquivo ```/etc/default/gpsd```
```sh
sudo nano /etc/default/gpsd
```

Encontre a linha ```DEVICES=""``` e adicione o caminho da porta serial do gps
```
DEVICES="/dev/ttyAMA0"
```

Certifique-se que o processo está configurado para iniciar automaticamente
```
START_DAEMON="true"
```

Reinicie o Raspberry
```
sudo reboot
```

## Python

Python 3.7.3

Instale a biblioteca [gpsd-py3](https://github.com/MartijnBraam/gpsd-py3)
```sh
$ pip3 install gpsd-py3
```
