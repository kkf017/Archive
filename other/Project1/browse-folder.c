#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>



int is_file(const char* path){	
	struct stat statbuf;
   	if (stat(path, &statbuf) != 0){
       		return -1;
       	}
   	return S_ISDIR(statbuf.st_mode);
}


int browse(char* path){

    struct dirent *de;
     
    DIR *dir = opendir(path); 
  
    if (dir == NULL){ 
        printf("\nCould not open current directory" ); 
        return 0; 
    } 
    
    
    int SIZE = 120;
    char actualpath [SIZE+1];
    char* filename = realpath(path, actualpath);		
  
     printf("\n\n=============================================================\nfolder %s \n%s\n =============================================================\n\n", path, filename);
     
    int PATH = strlen(filename) + 128;
    char str[PATH];
    
    while ((de = readdir(dir)) != NULL) 
    		if(strcmp(de->d_name, ".")!=0 && strcmp(de->d_name, "..")!=0){
    		
			//char str[strlen(filename) + strlen(de->d_name)+1];
			bzero(str, PATH);
			strcpy(str, filename);
			strcat(str, "/");
			strcat(str, de->d_name);
			
            		printf("\n%d \t%s ", is_file(str), str); 
            		
            		printf("\n\n");
            		
            		if(is_file(str)==1){
            			 browse(str);
            			 // send folder
            		}else{
            			// send file
            		}
            	
            	}
  
    closedir(dir);
    return 1;

}


int main(int argc, char *argv[]){
	
	//char* path = "/home/ksys/project/Example";
	char* path = "./project/Example";
	browse(path);
	
	return 0;
}
