from fastapi import HTTPException
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.storage import models


async def create_or_update_wallet(
    session: AsyncSession,
    address: str,
    balance: float,
    bandwidth: int,
    energy: int
) -> models.WalletInfo:
    try:
        result = await session.execute(
            select(models.WalletInfo).where(models.WalletInfo.address == address)
        )
        wallet = result.scalar_one_or_none()

        if wallet:
            wallet.balance = balance
            wallet.bandwidth = bandwidth
            wallet.energy = energy
        else:
            wallet = models.WalletInfo(
                address=address,
                balance=balance,
                bandwidth=bandwidth,
                energy=energy
            )
            session.add(wallet)

        await session.commit()
        await session.refresh(wallet)
        return wallet

    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

async def get_wallets_paginated(
    session: AsyncSession,
    skip: int = 0,
    limit: int = 10
) -> dict:
    total_result = await session.execute(select(func.count()).select_from(models.WalletInfo))
    total = total_result.scalar_one()

    data_result = await session.execute(
        select(models.WalletInfo).offset(skip).limit(limit)
    )
    items = data_result.scalars().all()

    return {
        "items": items,
        "total": total,
        "skip": skip,
        "limit": limit
    }