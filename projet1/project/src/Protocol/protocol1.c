#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#include "../global.h"
#include "../Message/message.h"
#include "protocol.h"



/*
void _ffsend_(int sock, char* path){

	printf("\nFilename (getfullpath): %s", path);
	
	int PATH_MAX = 64;
	char actualpath [PATH_MAX+1];
	char *ptr = realpath(path, actualpath);
	
	printf("\nFilename abs (getfullpath): %s", ptr);
	
	__send__(sock, ptr);
}



void _ffrcv_(int sock){

	char* response = __rcv__(sock);
	
	printf("\nRCV (_frcv_): %s", response);
	
	//char* __rcv__(int sock)
}
*/

/*****************************************************************************************/
void _fsend_(int sock, char* path){

	int FSIZE = 10;
	int STRSIZE = 128;
	
    	char buff[STRSIZE];
    	bzero(buff, STRSIZE);
    	strcpy(buff, path);
    	send(sock, buff, strlen(buff), 0); //__send__(sock, path);
    	bzero(buff, STRSIZE);

	printf("\nSEND: %s", path);
	
	//__send__(sock, ptr);

	FILE *fptr = fopen(path, "r");
	if (fptr == NULL){
	     perror("\n\033[0;91m[-]ERROR: Could not open input file.\033[0m");
	     exit(0);
	}
	
	int i;
   	char x;
    	char buffer[FSIZE];
	while(x != EOF){

		for(i=0;i<FSIZE;i++){
		    x = fgetc(fptr);
		    buffer[i] = x;            
		    if(x == EOF){
		        break;
		    }
		    //printf("%c",buffer[i]); // vers. with ./server > myprog.py
		}
		send(sock, buffer, strlen(buffer), 0); //__send__(sock, path);
		bzero(buffer, FSIZE);
	    }
    
    	fclose(fptr);
}


void _frcv_(int sock){

	//char* response = __rcv__(sock);
	
	int FSIZE = 10;
	int STRSIZE = 128;
	
	char buff[STRSIZE];  
	bzero(buff, STRSIZE);
    	recv(sock, buff, sizeof(buff), 0); //__rcv__(sock);
    	
    	char filename[STRSIZE];
    	strcpy(filename, buff);
    	strcat(filename,"-rcv.py");
    	bzero(buff, STRSIZE);
    	
    	printf("\nRCV: %s", filename);
    	
    	
    	FILE* fptr = fopen(filename, "w");
	printf("\n\nRcv file: %s\n\n", filename);
	if (fptr == NULL){
	     perror("\n\033[0;91m[-]ERROR: Could not open output file.\033[0m");
	     exit(0);
	}
	
	int i;
	int flag=1;
	char buffer[FSIZE];
	while(flag){
	
		bzero(buffer, FSIZE);
		recv(sock, buffer, sizeof(buffer), 0); //__rcv__(sock);
		
		for(i=0;i<FSIZE;i++){
            		if(buffer[i] == EOF){
            			flag=0;
                		break;
			}
		      //fputc(buffer[i], fptr); // vers. with file creation
	              printf("%c",buffer[i]); // vers. with ./server > myprog.py
	        }
	}
	fclose(fptr);
}
