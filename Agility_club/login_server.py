from concurrent import futures
import grpc
import user_pb2 as user_pb2
import user_pb2_grpc as user_pb2_grpc
import mysql.connector
#database has: (phil, password123) & (mary, password987)

class UserService(user_pb2_grpc.User):

    def __init__(self):
        #creates connection to the local database
        self.conn = mysql.connector.connect(
            host="localhost",
            user="server",
            password="1234",
            database="agility_members"
        )
        self.cursor = self.conn.cursor()

    def __del__(self):
        #Check when disconnecting all atributes and close them if needed
        if hasattr(self, 'cursor'):
            self.cursor.close()
        if hasattr(self, 'conn'):
            self.conn.close()

    def CheckUserCredentials(self, request, context):
        #Gets data from database and checks if there is a match and if not returns None
        query = "SELECT * FROM member_info WHERE username=%s AND password=%s"
        self.cursor.execute(query, (request.username, request.password))
        result = self.cursor.fetchone()
        #Returns answer to client
        if result:
            return user_pb2.UserResponse(message='Welcome to members only site!')
        else:
            return user_pb2.UserResponse(message='Incorrect username or password')

def serve():
    #setting server up
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Listening port...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
