from fastapi import FastAPI, Depends, Query

from app.api.schemas import WalletRequest, WalletResponse, PaginatedWallets
from app.storage.database import get_session, init_db
from app.storage.crud import create_or_update_wallet, get_wallets_paginated
from tronpy import Tron
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/api/wallet", response_model=WalletResponse)
async def fetch_wallet_info(
    request: WalletRequest,
    session: AsyncSession = Depends(get_session)
):
    wallet_info = get_wallet_info(request.address)

    await create_or_update_wallet(
        session,
        wallet_info.address,
        wallet_info.balance,
        wallet_info.bandwidth,
        wallet_info.energy
    )

    return wallet_info

def get_wallet_info(address: str) -> WalletResponse:
    try:
        client = Tron()

        balance = client.get_account_balance(address)
        bandwidth = client.get_bandwidth(address)
        energy = client.get_energy(address)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid TRON address or network error: {str(e)}")

    return WalletResponse(
        address=address,
        balance=float(balance),
        bandwidth=bandwidth,
        energy=energy
    )

@app.get("/api/wallet", response_model=PaginatedWallets)
async def read_wallets(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, gt=0),
    session: AsyncSession = Depends(get_session)
):
    return await get_wallets_paginated(session, skip=skip, limit=limit)