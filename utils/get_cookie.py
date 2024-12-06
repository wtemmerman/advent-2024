import browser_cookie3


def get_aoc_session_cookie():
    """
    Fetch the Advent of Code session cookie from the default browser.
    Returns:
        str: The session cookie value for AoC.
    Raises:
        Exception: If the cookie is not found.
    """
    try:
        cj = browser_cookie3.load()
        for cookie in cj:
            if cookie.domain == "adventofcode.com" and cookie.name == "session":
                return cookie.value
        raise Exception("Advent of Code session cookie not found. Make sure you're logged in.")
    except Exception as e:
        raise Exception(f"Error fetching session cookie: {e}")
