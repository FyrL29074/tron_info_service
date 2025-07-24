import pytest
from unittest.mock import patch, MagicMock

@pytest.mark.asyncio
@patch("app.api.main.Tron")
async def test_post_and_get_wallet(mock_tron_class, client):
    mock_tron = MagicMock()
    mock_tron.get_account_balance.return_value = 123.45
    mock_tron.get_bandwidth.return_value = 1000
    mock_tron.get_energy.return_value = 2000
    mock_tron_class.return_value = mock_tron

    # POST
    response_post = await client.post("/api/wallet", json={"address": "TUjx6w55Nx9G4GjjRNEB4e7w5BUH3WmJTZ"})
    assert response_post.status_code == 200
    data = response_post.json()
    assert data["balance"] == 123.45
    assert data["bandwidth"] == 1000
    assert data["energy"] == 2000

    # GET
    response_get = await client.get("/api/wallet?skip=0&limit=10")
    assert response_get.status_code == 200
    wallets = response_get.json()
    print(wallets)
    assert any(w["address"] == "TUjx6w55Nx9G4GjjRNEB4e7w5BUH3WmJTZ" for w in wallets["items"])
