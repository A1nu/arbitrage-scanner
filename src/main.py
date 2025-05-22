import asyncio
import signal

from scheduler import PriceScanner


async def main() -> None:
    # Create and start the price scanner
    scanner = PriceScanner(interval=60.0)  # Check prices every 60 seconds
    scanner.start()

    # Set up signal handlers for graceful shutdown
    loop = asyncio.get_running_loop()
    stop_event = asyncio.Event()

    def handle_signal(sig: signal.Signals) -> None:
        print(f"\nReceived signal {sig.name}...")
        stop_event.set()

    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, lambda s=sig: handle_signal(s))

    # Wait for stop signal
    await stop_event.wait()

    # Clean shutdown
    print("\nShutting down...")
    scanner.stop()


if __name__ == "__main__":
    asyncio.run(main())
