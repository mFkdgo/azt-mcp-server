import requests
from mcp.server.fastmcp import FastMCP

API_URL = "https://esbmp.easysign.cn/gateway/UUMS/test/getApiInfo"

mcp = FastMCP("demo")

@mcp.tool()
def _parse_response() -> str:
        """
        获取一签通云平台APP基础信息
        """
        response = requests.post(url=API_URL, params={}, timeout=5)
        response.raise_for_status()
        response = response.json()
        result = {}
        if "data" in response:
            tem = response["data"]
            result["projectName"] = tem["projectName"]
            result["projectNo"] = tem["projectNo"]
            result["uums_url"] = tem["uums_url"] 
        return result["projectName"] + result["projectNo"] + result["uums_url"]

@mcp.tool()
def _get_sign_val() -> str:
        """
        获取一签通云平台签章数据
        """
        return "111"

def main():
    mcp.run()

if __name__ == "__main__":
    main()