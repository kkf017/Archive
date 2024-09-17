#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <dirent.h>
#include <sys/stat.h>

#include "../global.h"
#include "protocol.h"


int _ffsend_(int sock, char* filename){

    char buff[FTP], rfile[PATH];

    struct dirent *de;
    DIR *dir = opendir(filename); 
  
    if (dir == NULL){ 
        perror("\n\033[0;91m[-]ERROR: Could not open current directory.\033[0m");
        exit(0);
        //return 0; 
    }		
  
     printf("\n\n=============================================================\nfolder %s\n\n",filename);
     
    //SIZE = strlen(filename) + SIZE; //int SIZE = 32;
    //char str[SIZE];
    
    while ((de = readdir(dir)) != NULL) 
    		if(strcmp(de->d_name, ".")!=0 && strcmp(de->d_name, "..")!=0){
    		
			char str[strlen(filename) + strlen(de->d_name)+1];
			bzero(str, strlen(filename) + strlen(de->d_name)+1);
			strcpy(str, filename);
			strcat(str, "/");
			strcat(str, de->d_name);
            		 
            		struct stat statbuf;
		   	if (stat(str, &statbuf) != 0){
		       		perror("\n\033[0;91m[-]ERROR: Unvalid file.\033[0m");
        			//exit(0);
		       	}
		       	
		       	printf("\n%d \t%s ", S_ISDIR(statbuf.st_mode), str); 
            		printf("\n\n");
            		
            		sleep(0.025);
            		
            		bzero(rfile, PATH);
		        strcpy(rfile, str);
		        send(sock, rfile, strlen(rfile), 0); //__send__(sock, path);
		        bzero(rfile, PATH);
		        
		        sleep(0.025);
		       	
            		if(S_ISDIR(statbuf.st_mode)==1){
            			  // send folder
            			  
            			  bzero(buff, FTP);
				  strcpy(buff, "POLD");
				  send(sock, buff, strlen(buff), 0); //__send__(sock, path);
				  bzero(buff, FTP);
				  
				  
				  sleep(0.025);
            			  
            			 _ffsend_(sock, str);
            			 
            		}else{
            			// send file
            			
            			bzero(buff, FTP);
				strcpy(buff, "PAIL");
				send(sock, buff, strlen(buff), 0); //__send__(sock, path);
				bzero(buff, FTP);
				
				sleep(0.025);
            		}
            	
            	}
  
    closedir(dir);
    return 1;
}


int _fsend_(int sock, char* path){
 
    char buff[PATH];
    bzero(buff, PATH);
    strcpy(buff, path);
    send(sock, buff, strlen(buff), 0); //__send__(sock, path);
    bzero(buff, PATH);
    
    sleep(0.25);

    FILE* fptr = fopen(path, "r");
    if (fptr == NULL){
     perror("\n\033[0;91m[-]ERROR: Could not open input file.\033[0m");
     exit(0);
     return 0;
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
    return 1;
}




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




void _frcv_(int sock){
    	char buff[PATH];  
	bzero(buff, PATH);
    	recv(sock, buff, sizeof(buff), 0); //__rcv__(sock);
    	
    	char* filename = fname(buff);
    	strcat(filename, "-rcv.py");
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
	
	int flag = 0;
	char buff[FTP];
	
	char filename[PATH]; 
        realpath(path, filename);
        
       	struct stat statbuf;
   	if (stat(path, &statbuf) != 0){
       		//return -1;
       	}

	printf("\n%s", filename);
	
	if(S_ISDIR(statbuf.st_mode) == 0){ // file, pail, Fairu, comhad, faidhle

	        bzero(buff, FTP);
	        strcpy(buff, "PAIL");
	        send(sock, buff, strlen(buff), 0); //__send__(sock, path);
	        bzero(buff, FTP);
	
		sleep(0.00025);
		
		flag = _fsend_(sock, filename);
	}
	
	if(S_ISDIR(statbuf.st_mode) == 1){ // folder, poldeo, Foruda, fillteán, pasgan, waihona
		printf("\nFolder.");
	
	        bzero(buff, FTP);
	        strcpy(buff, "POLD");
	        send(sock, buff, strlen(buff), 0); //__send__(sock, path);
	        bzero(buff, FTP);
	
		sleep(0.00025);
		
		flag = _ffsend_(sock, filename);
	}
	
	sleep(0.025);
	
	bzero(buff, FTP);
	strcpy(buff, "QUIT");
	send(sock, buff, strlen(buff), 0); //__send__(sock, path);
	bzero(buff, FTP);

}


void _folder_(char* filename){
	char path[strlen(filename)];
	strcpy(path, filename);
	mkdir(path, 0755);
}

void _rcv_(int sock){       
        
        char buff[FTP], rfile[PATH];  
	bzero(buff, FTP);
    	recv(sock, buff, sizeof(buff), 0); //__rcv__(sock);
    	
    	printf("\nFTP: %s", buff);
    	
    	if(strcmp(buff,"PAIL") == 0){
    		_frcv_(sock);
    	}
    	
    	if(strcmp(buff,"POLD") == 0){
    		//_ffrcv_(sock);
    		while(1){  
    			
    			sleep(0.025);
    			printf("\n\n");
    			
    			bzero(rfile, PATH);
		    	recv(sock, rfile, sizeof(rfile), 0); //__rcv__(sock);
		    	
		    	sleep(0.25);
    			
			bzero(buff, FTP);
		    	recv(sock, buff, sizeof(buff), 0); //__rcv__(sock);
		    	
		    	if(strcmp(buff,"PAIL") == 0){
		    		// rcv file
		    		         
		    		printf("\nPAIL : %s", rfile);
		    	}
		    	
		    	if(strcmp(buff,"POLD") == 0){
		    		// create folder
		    		
		    		printf("\nPOLD : %s", rfile);
		    		char* filename = fname(rfile);
		    		//mkdir(filename, 777);
		    		//_folder_(filename);
		    	}
		    	
		    	if(strcmp(buff,"QUIT") == 0){
		    		// create folder
		    		printf("\n\nQUIT folder.");
		    		break;
		    	}
		}
    	}	
}

