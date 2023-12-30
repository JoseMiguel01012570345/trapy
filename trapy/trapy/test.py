import os

class Conn:

    host_addr="localhost"
    host_port=0

    pass


# def isDigit_isDot():
    
#     if str(string).isdigit() or str(string) == ".":
#         return True
    
#     return False

# test_conn=Conn()

# test_conn.host_addr="127.0.0.2"
# test_conn.host_port=3306

# # Specify the directory path
# directory_path = "./"

# # Get the filename from the user
# filename = "myConn"

# # Combine directory path and filename
# filepath = os.path.join(directory_path, filename)

# try:
#     content = test_conn.host_addr+ ":" + str(test_conn.host_port)

#     file_size = os.stat(directory_path+filename).st_size

#     if file_size == 0 :

#         with open(filepath, "w") as file:
#             # Write data to the file
#             file.write(content+"\n")
#     else : 
#         # Open the file in write mode
#         with open(filepath, "a") as file:
#             # Write data to the file
#             file.write(content +"\n")

# except Exception as e:
#     print("server error: ",e)

# content=""

# try:
#         # Open the file in write mode
#     with open(filepath, "r") as file:
#             # Write data to the file
#        content = file.read().split("\n")
#     content=filter()

# except Exception as e:
#     print("server error: ",e)

# print("showing content:",content)

# items = os.listdir("./connections/")

# print(len(items))


x=10
print(type(x) == Conn)