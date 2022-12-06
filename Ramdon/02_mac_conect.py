# Importamos las clases "Ether", "ARP" y "srp" de la biblioteca scapy,
# y la clase "SSHClient" de la biblioteca paramiko.
from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp
from paramiko import SSHClient

# Creamos un paquete ARP con la dirección IP del dispositivo como destino
# y la dirección IP de nuestra interfaz de red como origen.
packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.0.1", psrc="192.168.0.2")

# Enviamos el paquete y esperamos una respuesta del dispositivo.
response = srp(packet, timeout=1, verbose=False)[0]

# Obtenemos la dirección MAC del dispositivo de la respuesta.
device_mac = response[0][1].hwsrc

# Creamos un cliente SSH y establecemos la dirección IP y la dirección MAC
# del dispositivo como valores de conexión.
client = SSHClient()
client.load_system_host_keys()
client.connect("192.168.0.1", port=22, username="user", password="password",
               look_for_keys=False, allow_agent=False,
               banner_timeout=60, mac_addr=device_mac)

# Una vez conectados, podemos ejecutar comandos en el dispositivo
# mediante el método "exec_command" del cliente SSH.
stdin, stdout, stderr = client.exec_command("uptime")
print(stdout.read())

# Cuando hayamos terminado, cerramos la conexión SSH.
client.close()
#Ten en cuenta que para utilizar las bibliotecas scapy y paramiko, es posible que necesites instalarlas primero en tu sistema. Puedes hacerlo ejecutando los comandos pip install scapy y pip install paramiko en una consola o terminal. También es posible que necesites tener permisos de administrador para instalar y utilizar las bibliotecas.




