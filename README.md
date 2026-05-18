# Sistem Distribuit de Livrare a Mesajelor


# Descriere proiect

Acest proiect implementeaza un sistem distribuit de livrare a mesajelor intre domenii, inspirat de functionarea unui sistem de e-mail simplificat.

Aplicatia este dezvoltata in Python folosind socket-uri TCP si arhitectura client-server.

Sistemul permite:
- trimiterea mesajelor catre unul sau mai multi destinatari
- rutarea mesajelor intre servere diferite
- salvarea mesajelor pe serverul responsabil de domeniul destinatarului
- tratarea erorilor si a serverelor indisponibile
  

# Functionalitati implementate

## Client
- compune si trimite mesaje
- poate trimite mesaje catre mai multi destinatari
- primeste raspuns de confirmare sau eroare

## Server
- accepta conexiuni concurrente de la clienti
- accepta mesaje de la alte servere
- analizeaza destinatarii si domeniile
- realizeaza rutarea mesajelor catre alte servere
- salveaza mesajele local in mailbox-uri
- trateaza erorile si serverele indisponibile


# Arhitectura aplicatiei

Proiectul contine:
- doua servere:
  - alpha.ro
  - beta.ro
- un client TCP
- comunicare server-server
- persistenta pe disc pentru mailbox-uri


# Tehnologii folosite

- Python 3
- TCP sockets
- threading
- JSON
- Docker
- docker-compose

# Instructiuni de rulare

## Pornirea serverelor

docker compose up --build

## Pornirea clientului

python client/client.py

## Oprirea serverelor

docker compose down


