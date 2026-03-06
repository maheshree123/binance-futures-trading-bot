# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot that interacts with the Binance Futures Testnet (USDT-M).
It allows users to place **Market** and **Limit** orders through a command-line interface while maintaining a clean project structure, logging, and proper error handling.

The application demonstrates a simple and reusable architecture for automated trading systems.

---

## Features

* Place **MARKET orders**
* Place **LIMIT orders**
* Support for **BUY and SELL**
* CLI input using `argparse`
* Input validation
* Logging of API responses and errors
* Structured project architecture

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
└── trading_bot.log
```

---

## Installation

Install dependencies:

```
pip install -r requirements.txt
```

---

## Setup

1. Create a Binance Futures Testnet account.

https://testnet.binancefuture.com

2. Generate API credentials from **API Management**.

3. Create a `.env` file in the project root:

```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key
```

---

## Usage

### MARKET Order Example

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

---

### LIMIT Order Example

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 65000
```

Example Output:

```
===== ORDER SUMMARY =====
Symbol: BTCUSDT
Side: SELL
Type: LIMIT
Quantity: 0.002
Price: 65000.0

===== ORDER RESPONSE =====
Order ID: 12661120763
Status: NEW
Executed Qty: 0.000
Avg Price: 0.00

Order placed successfully.
```

---

## Logging

All API requests, responses, and errors are logged in:

```
trading_bot.log
```

Example log entry:

```
2026-03-06 21:17:40 - INFO - Limit Order Response
```

---

## Error Handling

The application handles:

* Invalid CLI parameters
* Missing arguments
* Binance API errors
* Network failures

Errors are logged and displayed in the CLI output.

---

## Notes

This bot uses **Binance Futures Testnet**, not the live Binance environment.
Orders placed are simulated and use test funds.

---

## Author

Maheshree Katla
