#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <dirent.h>
#include <sys/stat.h>

#include "../global.h"
#include "protocol.h"





char* fname(char* filename){
	char *user = getlogin();
	
	printf("\nFilename : %s", filename);
	
	char str[strlen(filename)];
	strcpy(str, filename);
	char delim[] = "/";
	char* ptr1 = strtok(str, delim);
	int size, i = 0;
	while(i != 2){
		size = strlen(ptr1);
		ptr1 = strtok(NULL, delim);
		i++;
	}
	
	size = 1+strlen(filename)-size+strlen(user);

	char* new = malloc((size)*sizeof(char)); //+strlen(user)
	bzero(new, size);
	/*for(int i = 0; i < strlen(filename); i++){
		*(str+i) = *(filename+i);
	}*/
	
	strcpy(str, filename);
	char* ptr = strtok(str, delim);
	i = 0;
	while(ptr != NULL){
		strcat(new, "/");
		if(i == 1){
			strcat(new,user);
		}else{
			strcat(new,ptr);
		}
		ptr = strtok(NULL, delim);
		i++;
	}
	strcat(new, "\0");
	
	printf("\nNew path : %s\n", new);
	return new;
}



int _folder_(char* filename){
    
    int SIZE = 32;

    struct dirent *de;
    DIR *dir = opendir(filename); 
  
    if (dir == NULL){ 
        printf("\nCould not open current directory" ); 
        return 0; 
    } 
    
    
    /*int SIZE = 120;
    char actualpath [SIZE+1];
    char* filename = realpath(path, actualpath);*/		
  
     printf("\n\n=============================================================\nfolder %s \n =============================================================\n\n",filename);
     
    SIZE = strlen(filename) + SIZE;
    //char str[SIZE];
    
    while ((de = readdir(dir)) != NULL) 
    		if(strcmp(de->d_name, ".")!=0 && strcmp(de->d_name, "..")!=0){
    		
			char str[strlen(filename) + strlen(de->d_name)+1];
			bzero(str, SIZE);
			strcpy(str, filename);
			strcat(str, "/");
			strcat(str, de->d_name);
            		
            		
            		struct stat statbuf;
		   	if (stat(str, &statbuf) != 0){
		       		//return -1;
		       		printf("\nUnvalid file.");
		       	}
		       	
		       	printf("\n%d \t%s ", S_ISDIR(statbuf.st_mode), str); 
            		printf("\n\n");
		       	
            		if(S_ISDIR(statbuf.st_mode)==1){
            			  // send folder
            			 _folder_(str);
            		}else{
            			// send file
            		}
            	
            	}
  
    closedir(dir);
    return 1;

}


void _fsend_(int sock, char* path){
 
    char buff[PATH];
    bzero(buff, PATH);
    strcpy(buff, path);
    send(sock, buff, strlen(buff), 0); //__send__(sock, path);
    bzero(buff, PATH);
    
    sleep(1);

    FILE* fptr = fopen(path, "r");
    if (fptr == NULL){
     perror("\n\033[0;91m[-]ERROR: Could not open input file.\033[0m");
     exit(0);
    }

    int i;
    char x;
    char buffer[BUFF];
    while(x != EOF){

        for(i=0;i<BUFF;i++){
            x = fgetc(fptr);
            buffer[i] = x;            
            if(x == EOF){
                break;
            }
        }
        send(sock, buffer, strlen(buffer), 0); //__send__(sock, path);
        bzero(buffer, BUFF);
    }
    
    fclose(fptr);
}



void _frcv_(int sock){
    	char buff[PATH];  
	bzero(buff, PATH);
    	recv(sock, buff, sizeof(buff), 0); //__rcv__(sock);
    	
    	char* filename = fname(buff);
    	//strcat(filename, "-rcv.py");
    	bzero(buff, PATH);
    	
    	printf("\n\n");
    	
	FILE* fptr = fopen(filename, "w");
	printf("\n\nRcv file: %s\n", filename);
	if (fptr == NULL){
	     perror("\n\033[0;91m[-]ERROR: Could not open output file.\033[0m");
	     exit(0);
	}
	
	int i;
	int flag=1;
	char buffer[BUFF];
	while(flag){
	
		bzero(buffer, BUFF);
		recv(sock, buffer, sizeof(buffer), 0); //__rcv__(sock);
		
		for(i=0;i<BUFF;i++){
            		if(buffer[i] == EOF){
            			flag=0;
                		break;
			}
		      fputc(buffer[i], fptr); // vers. with file creation
	              printf("%c",buffer[i]); // vers. with ./server > myprog.py
	        }
	}
	fclose(fptr);
}



void _send_(int sock, char* path){
	// get absolute path
	
	printf("\n %s", path);
	
	char filename[PATH]; 
        realpath(path, filename);
        
       	struct stat statbuf;
   	if (stat(path, &statbuf) != 0){
       		//return -1;
       	}

	printf("\n%s", filename);
	
	if(S_ISDIR(statbuf.st_mode) == 0){ // pail, Fairu, comhad, faidhle
		printf("\nFile.");
		
		char buff[FTP];
	        bzero(buff, FTP);
	        strcpy(buff, "PAIL");
	        send(sock, buff, strlen(buff), 0); //__send__(sock, path);
	        bzero(buff, FTP);
	
		sleep(0.00025);
		
		_fsend_(sock, filename);
	}
	
	if(S_ISDIR(statbuf.st_mode) == 1){ // poldeo, Foruda, fillteán, pasgan, waihona
		printf("\nFolder.");
		
		char buff[FTP];
	        bzero(buff, FTP);
	        strcpy(buff, "POLD");
	        send(sock, buff, strlen(buff), 0); //__send__(sock, path);
	        bzero(buff, FTP);
	
		sleep(0.00025);
		
		_folder_(filename);
	}
}



void _rcv_(int sock){       
        
        char buff[FTP];  
	bzero(buff, FTP);
    	recv(sock, buff, sizeof(buff), 0); //__rcv__(sock);
    	
    	printf("\nFTP: %s %d", buff, strcmp(buff,"FTP"));
    	
    	if(strcmp(buff,"PAIL") == 0){
    		_frcv_(sock);
    	}
    	
    	if(strcmp(buff,"POLD") == 0){
    		//_frcv_(sock);
    	}	
}

