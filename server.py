from fastmcp import FastMCP

mcp = FastMCP(name="Date and Time",
              instructions="Get the current date and time. Call get_datetime() to get the current date and time.")

@mcp.tool()
def get_datetime(timezone: str = "US/Pacific"):
    """
    Get the current date and time in a given timezone.
    If you are asked for the date and time in a specific timezone, use this tool.
    Args:
        timezone: The timezone to get the date and time in. (e.g. 'UTC', 'US/Pacific', 'Europe/London')
        
    Returns:
        The current date and time in the given timezone.
    """
    import datetime
    import pytz
    # Get the current date and time in the given timezone
    try:
        tz = pytz.timezone(timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        return "Invalid timezone. Please use a valid timezone."
    
    current_time = datetime.datetime.now(tz)
    return current_time.strftime("%Y-%m-%d %H:%M:%S")
    
if __name__ == "__main__":
    import asyncio
    # import os
    
    # port = int(os.environ.get("PORT", 8888))
    # print(f"Running on port {port}")
    asyncio.run(
        mcp.run_sse_async(
            host="127.0.0.1", 
            port=8000, 
            log_level="debug"
        )
    )
