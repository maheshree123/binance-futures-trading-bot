import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

symbol = args.symbol.upper()
side = validate_side(args.side)
order_type = validate_order_type(args.type)

print("\n===== ORDER SUMMARY =====")
print(f"Symbol: {symbol}")
print(f"Side: {side}")
print(f"Type: {order_type}")
print(f"Quantity: {args.quantity}")
print(f"Price: {args.price}")

try:

    if order_type == "MARKET":

        response = place_market_order(
            symbol,
            side,
            args.quantity
        )

    elif order_type == "LIMIT":

        if not args.price:
            raise ValueError("LIMIT order requires --price")

        response = place_limit_order(
            symbol,
            side,
            args.quantity,
            args.price
        )

    print("\n===== ORDER RESPONSE =====")

    if "orderId" in response:

        print("Order ID:", response["orderId"])
        print("Status:", response["status"])
        print("Executed Qty:", response["executedQty"])

        if "avgPrice" in response:
            print("Avg Price:", response["avgPrice"])

        print("\nOrder placed successfully.")

    else:
        print("API Error Response:", response)

except Exception as e:

    print("\nOrder failed:", str(e))