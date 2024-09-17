#ifndef PROTOCOL
#define PROTOCOL

int _fsend_(int sock, char* msg);
void _frcv_(int sock);

void _send_(int sock, char* path);
void _rcv_(int sock);

int _ffsend_(int sock, char* filename);
void _ffrcv_(int sock);


#endif

