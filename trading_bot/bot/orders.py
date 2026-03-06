import logging
from .client import get_client


def place_market_order(symbol, side, quantity):

    client = get_client()

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logging.info(f"Market Order Response: {order}")
        return order

    except Exception as e:
        logging.error(f"Market Order Error: {str(e)}")
        print("API ERROR:", e)
        return {}


def place_limit_order(symbol, side, quantity, price):

    client = get_client()

    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logging.info(f"Limit Order Response: {order}")
        return order

    except Exception as e:
        logging.error(f"Limit Order Error: {str(e)}")
        print("API ERROR:", e)
        return {}