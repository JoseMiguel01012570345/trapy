class Conn:

    host_addr="localhost"

    connected=False

    client_addr="0.0.0.0"
    
    connection_request=False

    pass

class ConnException(Exception):

    pass

def parse_addr(address):
    
    conn = Conn()
    conn.host_addr = address

    return conn
    
def listen(address: str) -> Conn:

   try:
        conn = Conn()

        conn=parse_addr(address=address)

        import os
        # Specify the directory path
        directory_path = "./connections/"

        # Get the filename from the user
        filename = address

        # Combine directory path and filename
        filepath = os.path.join(directory_path, filename)

        content = ""

        with open(filepath, "w") as file:
            # Write data to the file
            file.write(content + "\n")
    
   except KeyboardInterrupt :
       close(conn=conn)
    
   except  Exception as e:
        close(conn=conn)
        print("server error: ", e )
        return ConnException()
            
    
   return conn

def search_client(addr,file):

    for device in list(file):
        if device == addr:
            return True 

    return False

def accept(conn) -> Conn:

    try:

        if type(conn) != Conn:
            print("internal server error: invalid argument")
            return ConnException()

        if not conn.connection_request:
            return conn

        import os
        directory_path = "./connections"

        # Get the filename from the user
        filename = conn.host_addr
        # Combine directory path and filename
        filepath = os.path.join(directory_path, filename)

        with open(filepath, "r") as file:
                # read data
                content = file.read().split("\n")
        
        status = search_client(conn.client_addr , content )
        
        if status:
            conn.connected=True            
        
        else:
            with open(filepath, "a") as file:
                # Write data to the file
                content = file.write( conn.client_addr + "\n" )        
                conn.connected=True
                print(conn.connected)
    
    except KeyboardInterrupt:
        close(conn)    
    
    except  Exception as e:
        close(conn=conn)
        print("an error arose from the accept() function: ", e )
        return ConnException()
    
    return conn    

def dial(address) -> Conn:
    
    conn=Conn()
    
    try:
        conn.host_addr=address
    
    
    except KeyboardInterrupt:
        close(conn=conn)
    
    pass

def send(conn: Conn, data: bytes) -> int: 
    pass

def recv(conn: Conn, length: int) -> bytes:
    pass

def remove_device(content,addr_client):

    new_content=""
    for device in content:
        if device == addr_client:
            list(content).remove(addr_client)
            continue
        if device != "":
            new_content += device + "\n"

    return new_content

def close(conn: Conn):

    import os

    # Specify the file path
    directory_path = "./connections/"

    # Get the filename from the user
    file_path = directory_path + conn.host_addr

    try:
        new_content=""
        with open(file_path, "r") as file:
                # Write data to the file
                content = file.read().split("\n")            
                new_content = remove_device(content=content, addr_client= conn.client_addr )

        with open(file_path,"w") as file:
            file.write(str(new_content))
    
    except Exception as e:
        print("an error ocurred from the close() function: ",e)

    pass

addr="127.0.0.1"

#listen(addr)
conn=Conn()

conn.host_addr="127.0.0.1"
conn.connection_request=True
conn.client_addr="192.168.120.101"

#accept(conn=conn)
close(conn)