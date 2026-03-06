# Binance Futures Testnet Trading Bot

A CLI-based Python trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.

## Features
- Market orders
- Limit orders
- BUY and SELL support
- CLI input using argparse
- Input validation
- Logging of API responses
- Error handling

## Installation

Install dependencies:

pip install -r requirements.txt

## Setup

Create a `.env` file:

BINANCE_API_KEY=your_api_key  
BINANCE_API_SECRET=your_secret_key

Use Binance Futures Testnet:
https://testnet.binancefuture.com

## Usage

Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 65000

## Logs

All requests and responses are stored in:

trading_bot.log
