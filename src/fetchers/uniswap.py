from typing import Optional

import aiohttp

from config import UNISWAP_API_KEY

DEPLOYMENT_ID = "5zvR82QoaXYFyDEKLZ9t6v9adgnptxYpKpSbxtgVENFV"
UNISWAP_GRAPH_URL = (
    f"https://gateway.thegraph.com/api/{UNISWAP_API_KEY}/subgraphs/id/{DEPLOYMENT_ID}"
)

ETH_USDT_POOL_ID = "0x4e68ccd3e89f51c3074ca5072bbac773960dfa36"

query_template = """
{
  pool(id: \"%s\") {
    token0 {
      symbol
    }
    token1 {
      symbol
    }
    token0Price
    token1Price
  }
}
"""


async def get_eth_price() -> Optional[float]:
    query = query_template % ETH_USDT_POOL_ID

    async with aiohttp.ClientSession() as session:
        async with session.post(UNISWAP_GRAPH_URL, json={"query": query}) as response:
            data = await response.json()
            return 1.0 / float(data["data"]["pool"]["token0Price"])
