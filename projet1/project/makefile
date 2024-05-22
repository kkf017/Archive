COMPILATEUR=gcc
EXEC=exec
SRC=src/main
GLOBAL=src/global
CLIENT=src/Client/client
SERVER=src/Server/server
FILE=src/Protocol/protocol
	


all: main clean

main: main.o client.o server.o protocol.o
	gcc *.o -o $(EXEC)

main.o: $(SRC).c $(CLIENT).h $(SERVER).h
	gcc -g -Wall -c $(SRC).c


server.o: $(SERVER).c $(SERVER).h $(FILE).h
	gcc -g -Wall -c $(SERVER).c

client.o: $(CLIENT).c $(CLIENT).h $(FILE).h
	gcc -g -Wall -c $(CLIENT).c

	
protocol.o: $(FILE).c $(FILE).h $(GLOBAL).h
	gcc -g -Wall -c $(FILE).c

clean:
	rm -rf *.o


