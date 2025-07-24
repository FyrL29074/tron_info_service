from pydantic import BaseModel

class WalletRequest(BaseModel):
    address: str

class WalletResponse(BaseModel):
    address: str
    balance: float
    bandwidth: int
    energy: int
    
class PaginatedWallets(BaseModel):
    items: list[WalletResponse]
    total: int
    skip: int
    limit: int