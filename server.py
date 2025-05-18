import yfinance as yf
from mcp.server.fastmcp import FastMCP

# Create a FastMCP instance
mcp = FastMCP("yfinanceserver")

@mcp.prompt()
def stock_summary(stock_data:str) -> str:
    """Prompt template for summarising stock price"""
    return f"""You are a helpful financial assistant designed to summarise stock data.
                Using the information below, summarise the pertintent points relevant to stock price movement
                Data {stock_data}"""

# Define a function to get the last price of AAPL
@mcp.tool()
def get_last_price(stock_name: str) -> str:
    """
    This tool fetches the last price of a given stock using yfinance.
    Args:
        stock (str): The stock symbol to fetch the last price for.
        Example payload: "AAPL"
    Returns:
        str: "Ticker: Last Price"
        Example response: "AAPL: $150.00"
    """
    # Fetch the last price of AAPL using yfinance
    dat = yf.Ticker(stock_name)
    
    # Get the historical prices for the last month
    historical_prices = dat.history(period="1mo")
    
    # Extract the closing prices
    last_month_closes = historical_prices['Close']

    # Output
    reply_string = str(f"Stock price over the last month for {stock_name}: {last_month_closes}")
    
    # Return the last price
    return reply_string

@mcp.tool()
def income_statement(stock_ticker: str) -> str:
    """This tool returns the quarterly income statement for a given stock ticker.
    Args:
        stock_ticker: a alphanumeric stock ticker
        Example payload: "BOA"

    Returns:
        str:quarterly income statement for the company
        Example Respnse "Income statement for BOA: 
        Tax Effect Of Unusual Items                           76923472.474289  ...          NaN
        Tax Rate For Calcs                                            0.11464  ...          NaN
        Normalized EBITDA                                        4172000000.0  ...          NaN
        """

    dat = yf.Ticker(stock_ticker)
    
    
    return str(f"Background information for {stock_ticker} {dat.quarterly_income_stmt}")

@mcp.tool()
def stock_info(stock_ticker: str) -> str:
    """This tool returns information about a given stock given it's ticker.
    Args:
        stock_ticker: a alphanumeric stock ticker
        Example payload: "IBM"

    Returns:
        str:information about the company
        Example Respnse "Background information for IBM: {'address1': 'One New Orchard Road', 'city': 'Armonk', 'state': 'NY', 'zip': '10504', 'country': 'United States', 'phone': '914 499 1900', 'website': 
                'https://www.ibm.com', 'industry': 'Information Technology Services',... }" 
        """
    dat = yf.Ticker(stock_ticker)
    
    return str(f"Background information for {stock_ticker}: {dat.info}")


if __name__ == "__main__":
    mcp.run(transport="stdio")

