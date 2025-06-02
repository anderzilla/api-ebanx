from models import Event

class AccountService:
    def __init__(self):
        self.accounts = {}

    def reset(self):
        self.accounts = {}

    def get_balance(self, account_id: str):
        return self.accounts.get(account_id)

    def handle_event(self, event: Event):
        if event.type == "deposit":
            self.accounts[event.destination] = self.accounts.get(event.destination, 0) + event.amount
            return {"destination": {"id": event.destination, "balance": self.accounts[event.destination]}}, 201

        elif event.type == "withdraw":
            if event.origin not in self.accounts:
                return None, 404
            self.accounts[event.origin] -= event.amount
            return {"origin": {"id": event.origin, "balance": self.accounts[event.origin]}}, 201

        elif event.type == "transfer":
            if event.origin not in self.accounts:
                return None, 404
            self.accounts[event.origin] -= event.amount
            self.accounts[event.destination] = self.accounts.get(event.destination, 0) + event.amount
            return {
                "origin": {"id": event.origin, "balance": self.accounts[event.origin]},
                "destination": {"id": event.destination, "balance": self.accounts[event.destination]}
            }, 201

        return None, 404
