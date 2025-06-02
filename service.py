from models import Event
from typing import Optional, Tuple, Dict, Union

class AccountService:
    def __init__(self):
        # Dicionário para armazenar os saldos das contas
        self.accounts: Dict[str, int] = {}

    def reset(self) -> None:
        """
        Limpa todas as contas (zera o estado da aplicação).
        """
        self.accounts = {}

    def get_balance(self, account_id: str) -> Optional[int]:
        """
        Retorna o saldo da conta informada ou None se não existir.
        """
        return self.accounts.get(account_id)

    def handle_event(self, event: Event) -> Tuple[Union[Dict, None], int]:
        """
        Processa um evento de tipo 'deposit', 'withdraw' ou 'transfer'.
        Retorna um dicionário com o novo estado da(s) conta(s) e o status HTTP.
        """
        if event.type == "deposit":
            self.accounts[event.destination] = self.accounts.get(event.destination, 0) + event.amount
            return {
                "destination": {
                    "id": event.destination,
                    "balance": self.accounts[event.destination]
                }
            }, 201

        elif event.type == "withdraw":
            if event.origin not in self.accounts:
                return None, 404
            self.accounts[event.origin] -= event.amount
            return {
                "origin": {
                    "id": event.origin,
                    "balance": self.accounts[event.origin]
                }
            }, 201

        elif event.type == "transfer":
            if event.origin not in self.accounts:
                return None, 404
            self.accounts[event.origin] -= event.amount
            self.accounts[event.destination] = self.accounts.get(event.destination, 0) + event.amount
            return {
                "origin": {
                    "id": event.origin,
                    "balance": self.accounts[event.origin]
                },
                "destination": {
                    "id": event.destination,
                    "balance": self.accounts[event.destination]
                }
            }, 201

        return None, 404

# 🔁 Instância global única da classe AccountService
service_instance = AccountService()
