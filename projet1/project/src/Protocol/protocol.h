#ifndef PROTOCOL
#define PROTOCOL

void _fsend_(int sock, char* msg);
void _frcv_(int sock);

void _send_(int sock, char* path);
void _rcv_(int sock);

#endif

