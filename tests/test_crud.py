import pytest
from app.storage import crud


@pytest.mark.asyncio
async def test_create_wallet(async_session):
    wallet = await crud.create_or_update_wallet(
        async_session, "address", 100.0, 200, 300
    )
    assert wallet.address == "address"
