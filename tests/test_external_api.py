import pytest
from src.external_api import ExternalAPIClient

class TestExternalAPIClient:
    @pytest.mark.asyncio
    async def test_get_user_success(self, mocker):
        mock_response = {'id': 1, 'name': 'John Doe'}
        mocker.patch('httpx.AsyncClient.get', return_value=mocker.Mock(
            status_code=200,
            json=lambda: mock_response
        ))
        
        client = ExternalAPIClient()
        result = await client.get_user(1)
        assert result == mock_response
    
    def test_get_post_error(self, mocker):
        mocker.patch('httpx.Client.get', return_value=mocker.Mock(
            status_code=404,
            raise_for_status=lambda: exec('raise httpx.HTTPStatusError("Not found")')
        ))
        
        client = ExternalAPIClient()
        with pytest.raises(httpx.HTTPStatusError):
            client.get_post(999)