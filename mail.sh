#!/bin/bash

cd /home/dorin/Python/mail_automatation

mail_add=$(zenity --entry --title="Adresa mail" --text="Introduceti adresa de mail")
password=$(zenity --password --title="Parola" --text="Introduceti parola")
subiect=$(zenity --entry --title="Subiect" --text="Introduceti subiectul mail-ului")
mail=$(zenity --entry --title="Mail" --text="Introduceti numele fisierului")
lista=$(zenity --entry --title="Lista" --text="Introduceti numele listei")
find=$(find / -type f -name $mail)
find_lista=$(find / -type f -name $lista)



python3 main.py $find $find_lista $mail_add $password $subiect
