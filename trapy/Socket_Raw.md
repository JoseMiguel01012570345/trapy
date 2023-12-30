# Socket de forma cruda sin nada
```python
import socket
import struct

# Crea un objeto de socket
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

# Define los campos del encabezado IP
version = 4
ihl = 5  # Longitud de la cabecera en palabras de 32 bits (mínimo: 5 palabras)
tos = 0  # Tipo de servicio
total_length = 0  # Se calculará automáticamente
identification = 54321  # Identificación del paquete
flags = 0  # No se establecen indicadores de fragmentación
fragment_offset = 0  # Desplazamiento del fragmento
ttl = 255  # Tiempo de vida
protocol = socket.IPPROTO_TCP  # Protocolo de la capa superior (por ejemplo, TCP)
checksum = 0  # Se calculará automáticamente
source_address = '192.168.0.1'  # Dirección IP de origen
destination_address = '192.168.0.2'  # Dirección IP de destino

# Construye el encabezado IP
ip_header = struct.pack('!BBHHHBBH4s4s', (version << 4) + ihl, tos, total_length, identification, (flags << 13) + fragment_offset, ttl, protocol, checksum, socket.inet_aton(source_address), socket.inet_aton(destination_address))

# Envía el encabezado IP al destino
sock.sendto(ip_header, (destination_address, 0))

# Cierra el socket
sock.close()
```

En este ejemplo, se utiliza el socket SOCK_RAW para crear un socket de red sin procesar que permite enviar paquetes IP personalizados. Se definen los diferentes campos del encabezado IP, como la versión, la longitud de la cabecera, el tipo de servicio, la longitud total, la identificación, las banderas y el desplazamiento del fragmento, el tiempo de vida, el protocolo, las direcciones IP de origen y destino, y el checksum.

Luego, se empaquetan estos campos en una estructura de bytes utilizando struct.pack() y se envía el encabezado IP al destino utilizando sendto().

Es importante destacar que trabajar con headers de capa de red y enviar paquetes personalizados puede tener implicaciones de seguridad y requerir privilegios administrativos en algunos sistemas. Los estudiantes deben tener precaución al utilizar este tipo de funcionalidad y asegurarse de cumplir con las políticas y regulaciones correspondientes.

Aqui tienen una explicación de cada uno de los argumentos utilizados en el ejemplo de implementación del header de capa de red:

```python
# Crea un objeto de socket
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
```

- socket.AF_INET: Especifica que se utilizará el protocolo de direcciones IP.
- socket.SOCK_RAW: Indica que se utilizará un socket de tipo RAW, lo que permite enviar y recibir paquetes IP sin procesar.
- socket.IPPROTO_RAW: Indica que se utilizará el protocolo de red IP sin procesar.

```python
# Define los campos del encabezado IP
version = 4
ihl = 5  # Longitud de la cabecera en palabras de 32 bits (mínimo: 5 palabras)
tos = 0  # Tipo de servicio
total_length = 0  # Se calculará automáticamente
identification = 54321  # Identificación del paquete
flags = 0  # No se establecen indicadores de fragmentación
fragment_offset = 0  # Desplazamiento del fragmento
ttl = 255  # Tiempo de vida
protocol = socket.IPPROTO_TCP  # Protocolo de la capa superior (por ejemplo, TCP)
checksum = 0  # Se calculará automáticamente
source_address = '192.168.0.1'  # Dirección IP de origen
destination_address = '192.168.0.2'  # Dirección IP de destino
```
- version: Especifica la versión del protocolo IP. En este caso, se utiliza la versión 4 (IPv4).
- ihl: Indica la longitud de la cabecera IP en palabras de 32 bits. En este caso, se establece en 5, que es el valor mínimo válido.
- tos: Representa el tipo de servicio, que se utiliza para indicar la prioridad o el tipo de tráfico.
- total_length: Es la longitud total del paquete IP, incluyendo la cabecera y los datos. En este ejemplo, se establece en 0, ya que se calculará automáticamente.
- identification: Es un número de identificación único asignado al paquete IP.
- flags y fragment_offset: Estos campos se utilizan para indicar si el paquete IP puede ser fragmentado y para especificar la posición del fragmento, en caso de que se fragmente.
- ttl: Representa el tiempo de vida del paquete IP, que indica cuántos saltos puede realizar antes de ser descartado.
- protocol: Especifica el protocolo de la capa superior que se utilizará después del procesamiento de IP. En este ejemplo, se utiliza socket.IPPROTO_TCP para indicar el protocolo TCP.
- checksum: Es el campo de verificación de integridad del encabezado IP. En este caso, se establece en 0, ya que se calculará automáticamente.
- source_address y destination_address: Son las direcciones IP de origen y destino, respectivamente.

```python
# Construye el encabezado IP
ip_header = struct.pack('!BBHHHBBH4s4s', (version << 4) + ihl, tos, total_length, identification, (flags << 13) + fragment_offset, ttl, protocol, checksum, socket.inet_aton(source_address), socket.inet_aton(destination_address))
```
- struct.pack(): Esta función se utiliza para empaquetar los valores de los campos del encabezado IP en una estructura de bytes según el formato especificado.
- '!BBHHHBBH4s4s': Es el formato de empaquetado utilizado por la función struct.pack(). Cada letra y símbolo representa un tipo de dato y su tamaño en bytes.
- socket.inet_aton(): Esta función se utiliza para convertir las direcciones IP de origen y destino de su representación en formato de cadena a un formato binario de 4 bytes.

```python
# Envía el encabezado IP al destino
sock.sendto(ip_header, (destination_address, 0))
```
- sock.sendto(): Se utiliza para enviar los datos del encabezado IP al destino especificado. Los datos se envían como un mensaje UDP sin procesar.

```python
# Cierra el socket
sock.close()
```
- sock.close(): Se utiliza para cerrar el socket después de enviar el encabezado IP.

