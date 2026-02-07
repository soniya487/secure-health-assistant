#!/usr/bin/env bash
if command -v ganache >/dev/null 2>&1; then
  ganache --deterministic --port 8545
else
  echo "Run Ganache via docker..."
  docker run -it -p 8545:8545 --name ganache trufflesuite/ganache-cli -d
fi
