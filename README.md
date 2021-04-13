# flexo
UCI-compatible chess engine

# docs

[source of uci doc](https://www.shredderchess.com/download.html)

## how to use

make flexo executable

```
chmod +x flexo
```

start engine by running flexo to send UCI commands on the terminal

```
./flexo
```
or use a UCI program like `scid`. If using scid, make sure to set the "directory" as the directory that flexo is checked out in. To make the log file write, exit scid.

this runs in python without raising

```python
import chess
import chess.engine
engine = chess.engine.SimpleEngine.popen_uci("/home/dennis/flexo/flexo")
```

## next step

make flexo play based on the current position. lichess will send over a game like this, interpret and make a legal move.

```
uci
ucinewgame
isready
position startpos moves g1f3 e7e5 b1a3 d7d5 b2b3 d8h4 h2h3 e5e4 e2e3 e4f3
go wtime 290780 btime 312000 winc 8000 binc 8000
```