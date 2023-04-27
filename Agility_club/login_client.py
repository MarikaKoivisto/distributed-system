import grpc
import user_pb2 as user_pb2
import user_pb2_grpc as user_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        #creates stub for user
        stub = user_pb2_grpc.UserStub(channel)

        #basic functionality to ask log in information
        print("Agility Club Lappeenranta!\nYou can browse site freely but for some features you need log in.")
        print("Please log in to proceed")
        while(True):
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            #cal for gRPC method via stub. parameters needs to be passed in format use=user, otherwise throws typeError
            response = stub.CheckUserCredentials(user_pb2.UserRequest(username=username, password=password))

            #prints server messages to the client
            if response.message == "Welcome to members only site!":
                print(response.message)
                break
            else:
                print(response.message)
                print("Please enter correct username/password")

if __name__ == '__main__':
    run()
