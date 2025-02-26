import httpx

class ExternalAPIClient:
    def __init__(self, base_url='https://jsonplaceholder.typicode.com'):
        self.base_url = base_url
    
    async def get_user(self, user_id):
        async with httpx.AsyncClient() as client:
            response = await client.get(f'{self.base_url}/users/{user_id}')
            response.raise_for_status()
            return response.json()
    
    def get_post(self, post_id):
        with httpx.Client() as client:
            response = client.get(f'{self.base_url}/posts/{post_id}')
            response.raise_for_status()
            return response.json()