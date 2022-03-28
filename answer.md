i. Find the first three TCP messages exchanged between the psql client and the postgres server. Which TCP flags were set on each of these messages?
The first three messages exchanged had set the following flags, respectively: syn, syn and ack, ack. 
<img width="551" alt="syn" src="https://user-images.githubusercontent.com/43149404/160499601-de76c937-8f01-4e7b-9afe-b7586dcf1223.png">
<img width="353" alt="syn:ack" src="https://user-images.githubusercontent.com/43149404/160499631-0a0ed729-6c78-4c82-8274-a13c14491cef.png">
<img width="511" alt="ack" src="https://user-images.githubusercontent.com/43149404/160499645-f454b791-d3e1-44c7-ac25-525ceb4e28ac.png">

ii. In the PostgreSQL startup message sent from the client to the server, what were the values for the protocol version, user, and database?
The protocol version was 6. The databas was called postgres and the user was called asaneedle.
<img width="912" alt="protocol_version" src="https://user-images.githubusercontent.com/43149404/160499919-196caade-65c1-4ebf-a917-39302f911cf4.png">
<img width="391" alt="database_and_user_name" src="https://user-images.githubusercontent.com/43149404/160499931-99b1cda7-ae6e-4931-ad5c-3067d4a56446.png">

iii. How many total bytes were sent over the socket for the SELECT query and corresponding response?
100 bytes were sent for the query, and 290 bytes were received for the response.

<img width="906" alt="query_response" src="https://user-images.githubusercontent.com/43149404/160501629-6fad4434-ea12-4546-b402-8de428d8d588.png">
